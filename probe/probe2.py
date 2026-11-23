"""Probe: 18 Idaho cities - robots.txt, platform, meeting/council links."""
import json, re, sys
from pathlib import Path
from urllib.parse import urljoin
sys.path.insert(0, str(Path(__file__).parent / "pipeline"))
import build
CANDS = {
 "Middleton": ["https://middleton.id.gov/"],
 "Payette": ["https://www.cityofpayette.com/", "https://payette.id.gov/", "https://www.payetteidaho.gov/"],
 "Fruitland": ["https://www.fruitland.org/", "https://fruitland.id.gov/", "https://www.fruitlandidaho.org/"],
 "Rupert": ["https://www.rupert-idaho.com/"],
 "Weiser": ["https://www.cityofweiser.net/"],
 "Preston": ["https://www.prestonidaho.net/", "https://prestonid.gov/", "https://www.prestonidaho.org/"],
 "Rigby": ["https://cityofrigby.gov/"],
 "Kimberly": ["https://www.cityofkimberly.org/", "https://kimberly.id.gov/", "https://www.kimberlyidaho.org/"],
 "Shelley": ["https://www.shelleyidaho.org/", "https://shelley.id.gov/", "https://www.cityofshelley.org/", "https://shelleyid.gov/"],
 "American Falls": ["https://cityofamericanfalls.com/"],
 "Buhl": ["https://www.cityofbuhl.us/"],
 "St. Anthony": ["https://www.cityofstanthony.org/"],
 "Gooding": ["https://www.goodingidaho.org/"],
 "Heyburn": ["https://heyburn.id.gov/"],
 "Grangeville": ["https://grangeville.us/"],
 "Orofino": ["https://www.cityoforofino.org/", "https://orofino.id.gov/", "https://www.orofino-id.gov/", "https://orofinoidaho.org/"],
 "Salmon": ["https://www.cityofsalmon.com/"],
 "Soda Springs": ["https://www.sodaspringsid.com/", "https://sodasprings.id.gov/", "https://www.sodaspringsidaho.gov/"],
}
MARK = {"civicplus": "AgendaCenter|Calendar.aspx|civicplus", "civicplus_new": "/m/calendar", "revize": "revize", "wordpress": "wp-content",
        "municipalimpact": "municipalimpact", "heygov": "heygov", "apptegy": "thrillshare|apptegy", "duda": "irp.cdn-website|dudamobile",
        "dnn": "Portals/0|DotNetNuke|dnn", "vertical": "vertical/sites", "civicclerk": "civicclerk", "municode": "municodemeetings",
        "squarespace": "squarespace", "weebly": "weebly|uploads/\\d/\\d/\\d", "wix": "wixstatic|wix.com", "govoffice": "govoffice", "granicus": "granicus|govdelivery"}
out = {}
for city, urls in CANDS.items():
    res = []
    for u in urls:
        r = {"url": u}
        try:
            build.check_robots(u)
            resp = build.get(u)
            h = resp.text
            r["final"] = resp.url
            r["status"] = resp.status_code
            r["title"] = (re.search(r"<title[^>]*>([^<]*)", h, re.I) or [None, ""])[1].strip()[:80]
            r["platform"] = [k for k, v in MARK.items() if re.search(v, h, re.I)]
            links = re.findall(r'href="([^"#]+)"[^>]*>(.*?)</a>', h, re.S | re.I)
            seen, keep = set(), []
            for href, txt in links:
                t = re.sub(r"<[^>]+>|\s+", " ", txt).strip()
                if re.search(r"agenda|council|meeting|calendar|mayor|minutes|planning|elected|government|event", t + " " + href, re.I):
                    a = urljoin(resp.url, href)
                    if a not in seen:
                        seen.add(a); keep.append([t[:40], a])
            r["links"] = keep[:25]
            res.append(r)
            break
        except Exception as exc:
            r["error"] = (type(exc).__name__ + ": " + str(exc))[:160]
            res.append(r)
    out[city] = res
Path(__file__).with_name("report2.json").write_text(json.dumps(out, indent=1))
print(json.dumps(out, indent=1)[:60000])
