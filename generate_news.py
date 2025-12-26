import feedparser
from datetime import datetime
import random

RSS_URL = "https://news.google.com/rss/search?q=artificial+intelligence+stocks+OR+AI+policy"

# -----------------------------
# SATIRE BY CONTEXT
# -----------------------------
SATIRE_LINES = {
    "finance": [
        "Investors are bullish, bearish, and confused simultaneously.",
        "Analysts upgraded the stock, downgraded expectations, and raised eyebrows.",
        "Retail investors discovered AI after the stock peaked.",
    ],
    "policy": [
        "Lawmakers promised clarity after a 300-page document.",
        "Regulation arrived faster than expected — understanding did not.",
        "AI asked for clearer requirements from humans.",
    ],
    "engineering": [
        "Engineers nodded politely and opened Stack Overflow.",
        "The demo worked perfectly, once.",
        "Production was not consulted.",
    ]
}

# -----------------------------
# CARTOON PROMPTS BY CONTEXT
# -----------------------------
PROMPTS = {
    "finance": [
        "Editorial cartoon, Wall Street investors staring at AI stock chart going straight up then crashing, exaggerated expressions, satire, newspaper comic style",
        "Political tech cartoon, AI robot inflating stock market bubble, confused traders, bold ink lines, classic finance satire",
    ],
    "policy": [
        "Editorial political cartoon, government regulating AI, lawmakers confused by robot, speech bubbles, classic newspaper style",
        "Satirical cartoon, AI testifying before politicians, exaggerated caricatures, ink drawing",
    ],
    "engineering": [
        "Satirical tech cartoon, engineers vs AI in office, sarcastic tone, flat colors, thick outlines",
        "Editorial cartoon, AI deploying itself to production, panicking engineers",
    ]
}

def detect_context(title):
    title = title.lower()
    if "stock" in title or "finance" in title or "market" in title:
        return "finance"
    if "regulation" in title or "policy" in title or "law" in title:
        return "policy"
    return "engineering"

feed = feedparser.parse(RSS_URL)
items = feed.entries[:5]

cards = ""
today = datetime.now().strftime("%B %d, %Y")

for item in items:
    context = detect_context(item.title)
    satire = random.choice(SATIRE_LINES[context])
    prompt = random.choice(PROMPTS[context])

    cards += f"""
    <div class="card">
        <h2>{item.title}</h2>
        <p class="satire"><i>{satire}</i></p>

        <div class="prompt">
            <b>🎨 Cartoon Prompt ({context.capitalize()}):</b>
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
.card {{ background:white; padding:30px; margin-bottom:40px;
        box-shadow:0 10px 25px rgba(0,0,0,.15); }}
.prompt {{ background:#eee; padding:15px; margin-top:15px; }}
pre {{ white-space:pre-wrap; }}
.satire {{ font-size:15px; color:#444; }}
</style>
</head>
<body>
<header>
<h1>🗞️ AI Cartoon Chronicle</h1>
<p>{today} — Finance • Policy • Engineering Satire</p>
</header>
<div class="container">
{cards}
</div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
