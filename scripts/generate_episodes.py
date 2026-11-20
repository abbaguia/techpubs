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
    ("en-short-architectural-flaws-outages", "en", "EN • Short", "How Architectural Flaws Cause System Outages", "Short edition on why architectural blind spots trigger outages.", f"{base_oci}0-En_Short_How_Architectural_Flaws_Cause_System_Outages.mp3"),
    ("fr-face-cachee-pannes-informatiques", "fr", "FR • Édition française", "La face cachée des pannes informatiques", "Édition en français sur les causes profondes des pannes systèmes.", f"{base_oci}1-Fr_La_face_cach%C3%A9e_des_pannes_informatiques.mp3"),
    ("en-why-redundant-systems-still-fail", "en", "EN • Long", "Why Redundant Systems Still Fail", "Why redundancy alone does not prevent end-to-end service failures.", f"{base_oci}2-En_Why_Redundant_Systems_Still_Fail.mp3"),
    ("en-why-redundancy-does-not-guarantee-resilience", "en", "EN • Long", "Why Redundancy Does Not Guarantee Resilience", "Protecting components versus protecting the complete service.", f"{base_oci}3-En_Why_Redundancy_Does_Not_Guarantee_Resilience.mp3"),
    ("en-how-single-failures-cause-global-outages", "en", "EN • Long", "How Single Failures Cause Global Outages", "How localized faults propagate across interconnected systems.", f"{base_oci}4-En_How_Single_Failures_Cause_Global_Outages.mp3"),
]

for slug, lang, tag, title, summary, mp3_url in episodes:
    (out_dir / f"{slug}.html").write_text(
        template.format(lang=lang, tag=tag, title=title, summary=summary, mp3_url=mp3_url),
        encoding="utf-8",
    )
print("Wrote 5 episode HTML files to podcasts/")
