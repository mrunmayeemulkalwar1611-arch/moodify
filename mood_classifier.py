import re

MOOD_KEYWORDS = {
    "happy": [
        "happy","joy","joyful","excited","great","awesome","wonderful","amazing",
        "cheerful","elated","thrilled","ecstatic","glad","pleased","fantastic",
        "delighted","overjoyed","blissful","good","excellent","brilliant","celebrate",
        "positive","smile","laugh","fun","yay","blessed","grateful","content",
        "pumped","energized","alive","free","light","sunshine","bright","euphoric"
    ],
    "sad": [
        "sad","depressed","lonely","unhappy","crying","heartbroken","miserable",
        "gloomy","down","upset","broken","lost","hopeless","grief","pain","hurt",
        "tears","sorrow","melancholy","disappointed","empty","numb","miss","missing",
        "alone","blue","devastated","ache","mourning","regret","somber","heavy"
    ],
    "calm": [
        "calm","peaceful","relaxed","chill","serene","tranquil","quiet","easy",
        "mellow","still","gentle","soft","soothing","meditate","meditation",
        "breathe","rest","resting","slow","cozy","comfortable","zen","mindful",
        "focus","study","reading","sleeping","sleepy","tired","lazy","unwind","recharge"
    ],
    "energetic": [
        "energetic","pumped","motivated","hyped","active","fired","workout","run",
        "running","gym","exercise","training","powerful","strong","intense","dynamic",
        "fast","speed","adrenaline","rush","power","unstoppable","beast","grind",
        "hustle","drive","push","lift","sweat","sprint","determined","focused"
    ],
    "angry": [
        "angry","furious","annoyed","mad","frustrated","rage","irritated","enraged",
        "livid","irate","hostile","aggressive","outraged","bitter","resentful","hate",
        "hating","pissed","fed up","sick","done","over it","infuriated","stressed",
        "overwhelmed","anxious","tense","pressure","boiling","exploding","venting"
    ],
    "romantic": [
        "romantic","love","crush","miss","affection","heart","date","tender",
        "passionate","intimate","devoted","adore","darling","sweetheart","valentine",
        "cherish","kiss","partner","relationship","couple","together","soulmate",
        "longing","desire","warmth","connection","beautiful","caring","butterflies"
    ]
}

MOOD_META = {
    "happy":    {"label":"Happy",      "emoji":"✨","color":"#FFD93D","bg_light":"#FFFBEB","bg_dark":"#1C1A00","desc":"Upbeat & feel-good tracks"},
    "sad":      {"label":"Melancholic","emoji":"🌧","color":"#6B9BF2","bg_light":"#EEF4FF","bg_dark":"#000D1C","desc":"Emotional & heartfelt songs"},
    "calm":     {"label":"Calm",       "emoji":"🌿","color":"#4ECBA0","bg_light":"#EDFAF4","bg_dark":"#001812","desc":"Soothing & peaceful vibes"},
    "energetic":{"label":"Energetic",  "emoji":"⚡","color":"#FF6B35","bg_light":"#FFF4EF","bg_dark":"#1C0800","desc":"High-energy workout bangers"},
    "angry":    {"label":"Intense",    "emoji":"🔥","color":"#FF4757","bg_light":"#FFF0F1","bg_dark":"#1C0003","desc":"Raw & powerful anthems"},
    "romantic": {"label":"Romantic",   "emoji":"💫","color":"#FF6B9D","bg_light":"#FFF0F7","bg_dark":"#1C0010","desc":"Love songs & ballads"},
}

def classify_mood(text):
    text_clean = re.sub(r'[^a-z\s]', '', text.lower())
    words = set(text_clean.split())
    scores = {mood: 0 for mood in MOOD_KEYWORDS}
    for mood, keywords in MOOD_KEYWORDS.items():
        for kw in keywords:
            if kw in words:
                scores[mood] += 3
            # partial: keyword is multi-word or root match (min 5 chars)
            elif len(kw) >= 5:
                for word in words:
                    if len(word) >= 5 and (word.startswith(kw[:4]) or kw.startswith(word[:4])):
                        scores[mood] += 1
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "calm"

def get_mood_meta(mood):
    return MOOD_META.get(mood, MOOD_META["calm"])
