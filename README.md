# Moodify — AI Mood Music Visualizer v2

## Quick Start (3 commands)

    pip install flask pandas numpy spotipy
    cd mood_visualizer
    python app.py

Open: http://127.0.0.1:5000


## Spotify Integration (Optional but Recommended)

### Step 1 — Create a Spotify App
1. Go to https://developer.spotify.com/dashboard
2. Log in with your Spotify account (free account works)
3. Click "Create App"
4. Fill in:
   - App name: Moodify
   - App description: Mood based music recommender
   - Redirect URI: http://127.0.0.1:5000/callback
5. Click Save
6. Click "Settings" — copy your Client ID and Client Secret

### Step 2 — Add credentials

Windows (Command Prompt):
    set SPOTIFY_CLIENT_ID=your_client_id_here
    set SPOTIFY_CLIENT_SECRET=your_client_secret_here
    python app.py

Mac/Linux (Terminal):
    export SPOTIFY_CLIENT_ID=your_client_id_here
    export SPOTIFY_CLIENT_SECRET=your_client_secret_here
    python app.py

### What Spotify adds:
- Real-time song recommendations (not just local database)
- Album artwork on every song card
- 30-second preview playback (▶ button on cards)
- Direct "Open in Spotify" links
- Genre-based recommendations using Spotify's algorithm


## Deploy Online (Share with a Link)

### Option A — Render.com (Free, easiest)
1. Push your project to GitHub
2. Go to https://render.com and sign up free
3. New → Web Service → connect your GitHub repo
4. Settings:
   - Build command: pip install -r requirements.txt
   - Start command: python app.py
5. Add environment variables (Spotify keys) in the Render dashboard
6. Deploy — you get a live URL like https://moodify.onrender.com

### Option B — Railway.app (Free tier)
1. Go to https://railway.app
2. New Project → Deploy from GitHub
3. Add environment variables for Spotify
4. Done — live URL in seconds

### Option C — PythonAnywhere (Free)
1. Go to https://pythonanywhere.com
2. Upload your project files
3. Set up a Web App pointing to app.py
4. Free subdomain: yourusername.pythonanywhere.com


## Project Files

    app.py               — Flask server (run this)
    mood_classifier.py   — AI mood detection
    music_engine.py      — Song recommendations (local + Spotify)
    data/mood_music.csv  — 120 songs across 6 moods
    templates/index.html — Full animated UI
    requirements.txt     — Python dependencies


## Features
- Dark / Light mode toggle
- 6 moods: Happy, Sad, Calm, Energetic, Angry, Romantic
- 120 local songs + unlimited Spotify recommendations
- Adjustable song count (5–20 songs)
- Live waveform animation per mood
- Floating particle system
- Ambient color-shifting background
- 30-second Spotify preview playback
- Direct Spotify links on every song
- Album artwork from Spotify
- Quick mood chips for fast demo
- Fully responsive on mobile
