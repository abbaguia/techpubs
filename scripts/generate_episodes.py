from pathlib import Path

out_dir = Path("podcasts")
out_dir.mkdir(parents=True, exist_ok=True)

base_oci = "https://objectstorage.us-ashburn-1.oraclecloud.com/n/idmpn7naypvj/b/mmpodcast/o/audio%2F"

template = """<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>The Mahamat Minute — {title}</title>
  <style>
    body {{ font-family: system-ui, -apple-system, sans-serif; background: #0f172a; color: #f8fafc; margin: 0; padding: 2rem 1rem; display: flex; justify-content: center; }}
    .card {{ background: #1e293b; border: 1px solid #334155; border-radius: 12px; padding: 1.75rem; max-width: 640px; width: 100%; }}
    .tag {{ font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.08em; color: #38bdf8; margin-bottom: 0.4rem; }}
    h1 {{ font-size: 1.35rem; margin: 0 0 0.5rem 0; }}
    p {{ color: #cbd5e1; line-height: 1.6; margin: 0.5rem 0 1.25rem 0; }}
    audio {{ width: 100%; }}
    .footer {{ margin-top: 1.25rem; font-size: 0.85rem; color: #94a3b8; }}
    .footer a {{ color: #38bdf8; text-decoration: none; }}
  </style>
</head>
<body>
  <article class="card">
    <div class="tag">The Mahamat Minute • {tag}</div>
    <h1>{title}</h1>
    <p>{summary}</p>
    <audio controls preload="metadata">
      <source src="{mp3_url}" type="audio/mpeg" />
      Your browser does not support the audio element.
    </audio>
    <div class="footer">
      <a href="./index.html">← All Podcast Editions</a>
    </div>
  </article>
</body>
</html>
"""

episodes = [
    (
        "En-Long_Why_Fast_Deployments_Break_Cloud_Infrastructure_v02",
        "en",
        "EN • Long (v02)",
        "Why Fast Deployments Break Cloud Infrastructure",
        "Long episode on why fast deployments and redundancy still leave cloud infrastructure vulnerable.",
        f"{base_oci}En-Long_Why_Fast_Deployments_Break_Cloud_Infrastructure_v02.mp3",
    ),
    (
        "En-Short_How_Architectural_Flaws_Cause_System_Outages_v02",
        "en",
        "EN • Short (v02)",
        "How Architectural Flaws Cause System Outages",
        "Short edition on why architectural blind spots trigger outages.",
        f"{base_oci}En-Short_How_Architectural_Flaws_Cause_System_Outages_v02.mp3",
    ),
    (
        "Fr-Long_La_face_cachee_des_pannes_informatiques_v02",
        "fr",
        "FR • Long (v02)",
        "La face cachee des pannes informatiques",
        "Edition en francais sur les causes profondes des pannes systemes.",
        f"{base_oci}Fr-Long_La_face_cachee_des_pannes_informatiques_v02.mp3",
    ),
]

for slug, lang, tag, title, summary, mp3_url in episodes:
    (out_dir / f"{slug}.html").write_text(
        template.format(lang=lang, tag=tag, title=title, summary=summary, mp3_url=mp3_url),
        encoding="utf-8",
    )

index_items = "\n".join(
    f'      <li><a href="./{slug}.html">[{tag}] {title}</a> — {summary}</li>'
    for slug, lang, tag, title, summary, mp3_url in episodes
)

index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>The Mahamat Minute — Podcast Hub</title>
  <style>
    body {{ font-family: system-ui, -apple-system, sans-serif; background: #0f172a; color: #f8fafc; margin: 0; padding: 2rem 1rem; display: flex; justify-content: center; }}
    .card {{ background: #1e293b; border: 1px solid #334155; border-radius: 12px; padding: 1.75rem; max-width: 640px; width: 100%; }}
    .tag {{ font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.08em; color: #38bdf8; margin-bottom: 0.4rem; }}
    h1 {{ font-size: 1.35rem; margin: 0 0 0.75rem 0; }}
    ul {{ padding-left: 1.25rem; line-height: 1.7; color: #cbd5e1; }}
    a {{ color: #38bdf8; text-decoration: none; }}
  </style>
</head>
<body>
  <main class="card">
    <div class="tag">The Mahamat Minute • Podcast Hub</div>
    <h1>Podcast Editions</h1>
    <ul>
{index_items}
    </ul>
  </main>
</body>
</html>
"""

(out_dir / "index.html").write_text(index_html, encoding="utf-8")
print("Wrote 3 episode HTML files and index.html to podcasts/")
