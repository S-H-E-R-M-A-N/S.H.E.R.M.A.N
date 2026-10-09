#!/usr/bin/env python3
import os, sys, json, time, urllib.parse, urllib.request, http.cookiejar

BASE = "https://www.space-track.org"
OUT = "snapshot.json"
GP = "/basicspacedata/query/class/gp"
FIELDS = "/predicates/NORAD_CAT_ID,OBJECT_NAME,EPOCH,TLE_LINE1,TLE_LINE2/format/json"
PAUSE = 3

QUERIES = [
    ("NASA", GP + "/NORAD_CAT_ID/25544,20580,25994,27424,49260" + FIELDS),
    ("SpaceX", GP + "/OBJECT_NAME/STARLINK~~/EPOCH/%3Enow-3/orderby/NORAD_CAT_ID%20asc/limit/150" + FIELDS),
    ("SpaceX", GP + "/OBJECT_NAME/CREW%20DRAGON~~/EPOCH/%3Enow-10/limit/3" + FIELDS),
    ("Other", GP + "/OBJECT_TYPE/PAYLOAD/DECAY_DATE/null-val/EPOCH/%3Enow-3/orderby/NORAD_CAT_ID%20asc/limit/150" + FIELDS),
] + [
    ("Junk", GP + "/OBJECT_NAME/" + urllib.parse.quote(n) + "~~/EPOCH/%3Enow-30/limit/15" + FIELDS)
    for n in ("COSMOS 2251 DEB", "FENGYUN 1C DEB", "IRIDIUM 33 DEB")
]


def main():
    user, pw = os.environ.get("SPACETRACK_USER"), os.environ.get("SPACETRACK_PASS")
    if not user or not pw:
        sys.exit("Set SPACETRACK_USER and SPACETRACK_PASS first.")
    if os.path.exists(OUT) and "--force" not in sys.argv and time.time() - os.path.getmtime(OUT) < 4 * 3600:
        sys.exit("snapshot.json is under 4 hours old. Space-Track data updates no faster than that; use --force to override.")

    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
    login = urllib.parse.urlencode({"identity": user, "password": pw}).encode()
    reply = opener.open(BASE + "/ajaxauth/login", login).read().decode()
    if "Failed" in reply:
        sys.exit("Login failed. Check your username and password.")

    seen, objects = set(), []
    try:
        for group, path in QUERIES:
            try:
                rows = json.loads(opener.open(BASE + path).read().decode())
            except Exception as e:
                print("Query failed:", path[:80], e)
                rows = []
            for r in rows:
                if r.get("NORAD_CAT_ID") in seen or not r.get("TLE_LINE1"):
                    continue
                seen.add(r["NORAD_CAT_ID"])
                objects.append({"name": r["OBJECT_NAME"], "group": group, "norad": r["NORAD_CAT_ID"],
                                "epoch": r["EPOCH"], "line1": r["TLE_LINE1"], "line2": r["TLE_LINE2"]})
            time.sleep(PAUSE)
    finally:
        try:
            opener.open(BASE + "/ajaxauth/logout")
        except Exception:
            pass

    with open(OUT, "w") as f:
        json.dump({"fetched": time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime()), "objects": objects}, f)
    print(f"Saved {len(objects)} objects to {OUT}")


if __name__ == "__main__":
    main()
