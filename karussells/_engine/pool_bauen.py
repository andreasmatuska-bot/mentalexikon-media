#!/usr/bin/env python3
"""Baut und aktualisiert vorlagen_pool.json: die gemeinsame Bestenliste aller Vorbildseiten.

Aufruf:  python3 pool_bauen.py <seite>=<datei.json> [<seite>=<datei.json> ...]

<datei.json> ist das Ergebnis von get-dataset-items (Objekt mit "items") oder eine reine Liste.
Benötigte Felder je Beitrag: shortCode, type, likesCount, commentsCount, timestamp, caption.
Optional: url, paidPartnership.

Der Pool wird nie verkleinert: neue Beiträge kommen dazu, Zahlen bekannter Beiträge werden
aufgefrischt, "verwendet" wird aus verwendet.json gesetzt.
"""
import json, re, statistics, sys, os, datetime

HIER = os.path.dirname(os.path.abspath(__file__))
POOL = os.path.join(HIER, "vorlagen_pool.json")
VERWENDET = os.path.join(HIER, "verwendet.json")

RE_TIERE = re.compile(r"\b(hund|hunde|hunden|katze|katzen|haustier)")
RE_KRANK = re.compile(r"(krankheit|erkrankung|diagnos|krebs|demenz|depression|adhs|autis|symptom|medikament|burnout|trauma)")
RE_WERBUNG = re.compile(r"(\[anzeige\]|\[empfehlung\]|link in (der )?bio|gewinnspiel|webinar|schreib(e)? .{0,30}nachricht mit|künstliche[rn]? intelligenz|\bki\b.{0,60}(geld|verdien|einkommen)|digitale fähigkeiten|werke? über wohlstand|ortsunabhängig arbeiten)")


def saeubern(c):
    c = re.sub(r"#\S+", "", c or "")
    c = re.sub(r"👉.*?👈", "", c)
    return c.strip()


def laden(pfad):
    d = json.load(open(pfad, encoding="utf-8"))
    return d["items"] if isinstance(d, dict) else d


def auswerten(seite, items):
    items = sorted(items, key=lambda x: x["timestamp"])
    sicht = [i for i in items if (i.get("likesCount") or 0) > 0]
    # Verhältnis Likes zu Kommentaren der Seite, um verborgene Likes zu schätzen
    paare = [(i["likesCount"], i["commentsCount"]) for i in sicht if (i.get("commentsCount") or 0) > 0]
    lpk = statistics.median(l / k for l, k in paare) if paare else 0
    out = []
    for n, i in enumerate(items):
        if i.get("type") != "Sidecar":
            continue
        text = saeubern(i.get("caption"))
        if len(text) < 100 or text.startswith(("Kommentiere", "Folge")):
            continue
        fenster = [j["likesCount"] for j in items[max(0, n - 40): n + 41] if (j.get("likesCount") or 0) > 0]
        med = statistics.median(fenster) if fenster else 0
        likes = i.get("likesCount") or 0
        geschaetzt = False
        if likes <= 0:
            likes = int((i.get("commentsCount") or 0) * lpk)
            geschaetzt = True
        faktor = round(likes / med, 2) if med else 0
        klein = text.lower()
        hinweise = []
        if i.get("paidPartnership") or RE_WERBUNG.search(klein):
            hinweise.append("werbung")
        if RE_KRANK.search(klein):
            hinweise.append("krankheit_pruefen")
        if RE_TIERE.search(klein):
            hinweise.append("tiere")
        if geschaetzt:
            # verborgene Likes: nur über Kommentare geschätzt, deshalb nie Stufe A
            stufe = "B" if likes >= 4000 else "C"
        elif likes >= 10000 or (faktor >= 3 and likes >= 3000):
            stufe = "A"
        elif likes >= 4000 or (faktor >= 1.5 and likes >= 1500):
            stufe = "B"
        else:
            stufe = "C"
        out.append({
            "quelle": i["shortCode"], "seite": seite,
            "url": i.get("url") or f"https://www.instagram.com/p/{i['shortCode']}/",
            "datum": i["timestamp"][:10], "likes": likes, "likes_geschaetzt": geschaetzt,
            "kommentare": i.get("commentsCount") or 0, "faktor": faktor, "stufe": stufe,
            "hinweise": hinweise, "verwendet": False, "caption": text,
        })
    return out


def schluessel(text):
    return re.sub(r"\W", "", text.lower())[:70]


def main():
    pool = {p["quelle"]: p for p in json.load(open(POOL, encoding="utf-8"))["vorlagen"]} if os.path.exists(POOL) else {}
    for arg in sys.argv[1:]:
        seite, pfad = arg.split("=", 1)
        for p in auswerten(seite, laden(pfad)):
            alt = pool.get(p["quelle"])
            if alt:  # Zahlen auffrischen, beste Stufe behalten
                p["stufe"] = min(alt["stufe"], p["stufe"])
                p["likes"] = max(alt["likes"], p["likes"]) if not p["likes_geschaetzt"] else alt["likes"] if not alt["likes_geschaetzt"] else p["likes"]
                p["likes_geschaetzt"] = alt["likes_geschaetzt"] and p["likes_geschaetzt"]
            pool[p["quelle"]] = p
    benutzt = {e["quelle"] for e in json.load(open(VERWENDET, encoding="utf-8"))} if os.path.exists(VERWENDET) else set()
    liste = sorted(pool.values(), key=lambda p: (p["stufe"], -p["likes"]))
    # gleiche Beiträge (Reposts der Seite) zusammenfassen, bester bleibt
    gesehen, fertig = {}, []
    for p in liste:
        k = schluessel(p["caption"])
        if k in gesehen:
            gesehen[k].setdefault("doppelt", [])
            if p["quelle"] not in gesehen[k]["doppelt"]:
                gesehen[k]["doppelt"].append(p["quelle"])
            if p["quelle"] in benutzt:
                gesehen[k]["verwendet"] = True
            continue
        p["verwendet"] = p["quelle"] in benutzt or any(q in benutzt for q in p.get("doppelt", []))
        gesehen[k] = p
        fertig.append(p)
    json.dump({"stand": datetime.date.today().isoformat(), "vorlagen": fertig},
              open(POOL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    frei = [p for p in fertig if not p["verwendet"] and "werbung" not in p["hinweise"]]
    for s in "ABC":
        print(f"Stufe {s}: {sum(1 for p in fertig if p['stufe'] == s)} gesamt, {sum(1 for p in frei if p['stufe'] == s)} frei")
    for seite in sorted({p['seite'] for p in fertig}):
        print(seite, {s: sum(1 for p in frei if p['stufe'] == s and p['seite'] == seite) for s in 'ABC'})


if __name__ == "__main__":
    main()
