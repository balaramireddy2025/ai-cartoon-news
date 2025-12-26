import feedparser
from datetime import datetime
import random

RSS_URL = "https://news.google.com/rss/search?q=artificial+intelligence"

SATIRE_TEMPLATES = [
    "Experts claim this will change everything, again.",
    "Engineers are cautiously optimistic and already updating resumes.",
    "Management says it’s revolutionary; developers say it’s broken.",
    "AI promises productivity gains; meetings increase by 40%."
]

PROMPT_TEMPLATES = [
    "Political cartoon, AI robot debating humans, exaggerated expressions, editorial satire, bold ink lines, newspaper comic style",
    "Satirical tech cartoon, engineers vs AI, office setting, sarcastic tone, flat colors, thick outlines",
    "Editorial cartoon, government regulating AI, humorous caricatures, speech bubbles, classic newspaper style"
]

feed = feedparser.parse(RSS_URL)
items = feed.entries[:5]

cards = ""
today = datetime.now().strftime("%B %d, %Y")

for item in items:
    satire = random.choice(SATIRE_TEMPLATES)
    prompt = random.choice(PROMPT_TEMPLATES)

    cards += f"""
    <div class="card">
        <h2>{item.title}</h2>
        <p><i>{satire}</i></p>

        <div class="prompt">
            <b>🎨 Cartoon Prompt:</b>
            <pre>{prompt}</pre>
        </div>

        <a href="{item.link}" target="_blank">Read original →</a>
    </div>
    """

html = f"""
<html>
<head>
<title>AI Cartoon News</title>
<style>
body {{ font-family: Georgia; background:#f4f1ec; }}
header {{ background:black; color:white; padding:30px; text-align:center; }}
.container {{ max-width:1100px; margin:auto; padding:40px; }}
.card {{ background:white; padding:25px; margin-bottom:30px;
        box-shadow:0 8px 20px rgba(0,0,0,.15); }}
.prompt {{ background:#eee; padding:15px; margin-top:15px; }}
pre {{ white-space:pre-wrap; }}
</style>
</head>
<body>
<header>
<h1>🗞️ AI Cartoon Chronicle</h1>
<p>{today}</p>
</header>
<div class="container">
{cards}
</div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
