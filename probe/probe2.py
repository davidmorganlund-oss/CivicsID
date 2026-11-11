"""Third pass: remaining counties (Gem, Lewis, Oneida, Lincoln, Blaine) and their seat cities."""
import json, re
from pathlib import Path
import requests

UA = "CivicsID/0.1 (BarNone nonprofit civic calendar; contact via barnoneinc.org)"
S = requests.Session(); S.headers["User-Agent"] = UA
OUT = {}

def get(url, **kw):
    try:
        r = S.get(url, timeout=25, **kw); return r.status_code, r.url, r.text
    except Exception as e:
        return 0, url, f"ERR {e}"[:200]

def text(h):
    h = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", h, flags=re.S | re.I)
    return " ".join(re.sub(r"<[^>]+>", " ", h).split())

KEY = re.compile(r"[^.]{0,160}(?:regular(?:ly)? (?:meeting|scheduled|session)|meets? (?:on|every|the)|(?:1st|2nd|3rd|4th|first|second|third|fourth|every) (?:and (?:1st|2nd|3rd|4th|first|second|third|fourth) )?(?:Monday|Tuesday|Wednesday|Thursday|Friday))[^.]{0,200}", re.I)

urls = {
 "gem agendas": "https://www.gemcounty.org/government/county_commissioners/agendas_and_minutes.php",
 "gem commissioners": "https://www.gemcounty.org/government/county_commissioners/index.php",
 "gem robots": "https://www.gemcounty.org/robots.txt",
 "lewis home": "https://www.lewiscountyid.us/",
 "lewis robots": "https://www.lewiscountyid.us/robots.txt",
 "lewis commissioners": "https://www.lewiscountyid.us/commissioners",
 "oneida home": "https://oneidacountyid.com/",
 "oneida commissioners": "https://oneidacountyid.com/commissioners/",
 "lincoln us": "https://www.lincolncountyid.us/",
 "emmett home": "https://www.cityofemmett.org/",
 "emmett council": "https://www.cityofemmett.org/citycouncil",
 "emmett robots": "https://www.cityofemmett.org/robots.txt",
 "malad home": "https://www.maladidaho.org/",
 "nezperce home": "https://www.cityofnezperce.com/",
 "kamiah home": "https://www.kamiahidaho.org/",
 "kamiah alt": "https://kamiah.org/",
 "shoshone city": "https://www.shoshonecity.com/",
 "hailey meetings": "https://www.haileycityhall.org/public-meetings/",
 "hailey robots": "https://www.haileycityhall.org/robots.txt",
 "hailey tribe": "https://www.haileycityhall.org/wp-json/tribe/events/v1/events?per_page=30",
 "blaine us": "https://www.co.blaine.id.us/",
}
for k, u in urls.items():
    c, f, h = get(u)
    t = text(h)
    links = sorted(set(re.findall(r'href="([^"]*(?:agenda|meeting|calendar|ics|feed|event)[^"]*)"', h, re.I)))[:40]
    OUT[k] = {"status": c, "final": f, "len": len(h), "robots": h[:600] if "robots" in k else "",
              "schedule": [m.strip() for m in KEY.findall(t)][:8], "links": links,
              "head": t[:500], "gen": re.findall(r'<meta name="generator" content="([^"]+)"', h)[:2],
              "hint": "tribe" if "tribe-events" in h else ("revize" if "revize" in h.lower() else ("wix" if "wix" in h.lower() else ""))}
    print("=" * 8, k); print(json.dumps(OUT[k], indent=1)[:2500])
Path("probe/report2.json").write_text(json.dumps(OUT, indent=1))
