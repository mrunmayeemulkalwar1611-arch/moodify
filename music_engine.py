import pandas as pd
import os
import random

DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "mood_music.csv")

MOOD_GENRES = {
    "happy":     ["pop","happy","feel-good","summer","party"],
    "sad":       ["sad","emo","indie","heartbreak","acoustic"],
    "calm":      ["chill","ambient","sleep","study","acoustic"],
    "energetic": ["workout","hip-hop","power-workout","metal","running"],
    "angry":     ["metal","punk","hip-hop","rock","heavy-metal"],
    "romantic":  ["romance","love","r-n-b","soul","jazz"],
}

def get_local_songs(mood, n=10):
    df = pd.read_csv(DATA_PATH)
    matches = df[df['mood'] == mood].copy()
    if matches.empty:
        matches = df[df['mood'] == 'calm'].copy()
    sample = matches.sample(min(n, len(matches)))
    return sample.to_dict('records')

def get_spotify_songs(mood, n=10, sp=None):
    if sp is None:
        return []
    try:
        genres = MOOD_GENRES.get(mood, ["pop"])
        genre = random.choice(genres)
        results = sp.recommendations(seed_genres=[genre], limit=n)
        tracks = []
        for t in results['tracks']:
            tracks.append({
                'song':   t['name'],
                'artist': ', '.join([a['name'] for a in t['artists']]),
                'genre':  genre.replace('-',' ').title(),
                'bpm':    0,
                'year':   t['album']['release_date'][:4] if t['album']['release_date'] else '?',
                'spotify_url':  t['external_urls'].get('spotify',''),
                'preview_url':  t['preview_url'] or '',
                'image':        t['album']['images'][0]['url'] if t['album']['images'] else '',
                'source': 'spotify'
            })
        return tracks
    except Exception as e:
        print(f"Spotify error: {e}")
        return []

def get_songs(mood, n=10, sp=None):
    spotify_songs = get_spotify_songs(mood, n, sp)
    if spotify_songs:
        return spotify_songs
    local = get_local_songs(mood, n)
    for s in local:
        s['source'] = 'local'
        s['spotify_url'] = f"https://open.spotify.com/search/{s['song'].replace(' ','%20')}%20{s['artist'].replace(' ','%20')}"
        s['preview_url'] = ''
        s['image'] = ''
    return local
