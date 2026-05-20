from flask import Flask, render_template, request, jsonify, session, redirect
import os, json

app = Flask(__name__)
app.secret_key = os.urandom(24)

from mood_classifier import classify_mood, get_mood_meta
from music_engine import get_songs

# ── Spotify (optional) ──────────────────────────────────────────────────────
SPOTIFY_CLIENT_ID     = os.environ.get("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET", "")
SPOTIFY_REDIRECT_URI  = os.environ.get("SPOTIFY_REDIRECT_URI", "http://127.0.0.1:5000/callback")
SPOTIFY_ENABLED       = bool(SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET)

sp = None
if SPOTIFY_ENABLED:
    try:
        import spotipy
        from spotipy.oauth2 import SpotifyClientCredentials
        sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
            client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIFY_CLIENT_SECRET
        ))
        print("  Spotify connected!")
    except Exception as e:
        print(f"  Spotify not available: {e}")

# ── Routes ───────────────────────────────────────────────────────────────────
@app.route('/')
def index():
    return render_template('index.html', spotify_enabled=SPOTIFY_ENABLED)

@app.route('/analyze', methods=['POST'])
def analyze():
    data  = request.get_json()
    text  = data.get('text', '').strip()
    count = int(data.get('count', 10))
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    mood  = classify_mood(text)
    meta  = get_mood_meta(mood)
    songs = get_songs(mood, n=count, sp=sp)
    return jsonify({
        'mood':     mood,
        'label':    meta['label'],
        'emoji':    meta['emoji'],
        'color':    meta['color'],
        'bg_light': meta['bg_light'],
        'bg_dark':  meta['bg_dark'],
        'desc':     meta['desc'],
        'songs':    songs,
        'spotify':  SPOTIFY_ENABLED
    })

@app.route('/mood/<mood>')
def mood_page(mood):
    meta  = get_mood_meta(mood)
    songs = get_songs(mood, n=10, sp=sp)
    return jsonify({'mood': mood, 'meta': meta, 'songs': songs})

if __name__ == '__main__':
    print("\n" + "="*45)
    print("  Mood Music Visualizer v2 — Running!")
    print(f"  Spotify: {'Connected' if SPOTIFY_ENABLED else 'Not configured (using local DB)'}")
    print("  Open: http://127.0.0.1:5000")
    print("="*45 + "\n")
    app.run(debug=True, host='0.0.0.0', port=5000)
