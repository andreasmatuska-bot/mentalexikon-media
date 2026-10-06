"""Baut Karussells für die Seite Mindsetologie (Spiegel von Mentalexikon, leicht umgeschrieben).
Aufruf in karussells/_engine:  python3 mindsetologie_bauen.py <plan.json> [slug ...]
plan.json: Liste von {nr, slug, farbe, termin, art, mentalexikon_termin, slides}.
Ergebnis: Bilder in ../../mindsetologie/<slug>/01.jpg ..., dazu slides.json und caption.txt im selben Ordner.
"""
import json, os, re, subprocess, sys
HANDLE = "@mindsetologie"
def caption(slides):
    out = []
    for s in slides:
        lines = []
        for p in s:
            if p.startswith("Mehr davon"): continue
            head = re.fullmatch(r"<b>([^<:.?!]+)</b>", p)
            t = re.sub(r"<br>", " ", p); t = re.sub(r"<[^>]+>", "", t).strip()
            if head: lines.append(("h", t + ":"))
            elif re.match(r"^\d+\.\s", t): lines.append(("n", t))
            else: lines.append(("t", t))
        txt = ""
        for k, (typ, t) in enumerate(lines):
            if k == 0: txt = t
            elif typ == "n" or lines[k-1][0] == "n": txt += "\n" + t
            else: txt += " " + t
        if txt: out.append(txt)
    return "\n\n".join(out) + "\n\nMehr davon: folge " + HANDLE + "."
if __name__ == "__main__":
    plan = json.load(open(sys.argv[1])); nur = set(sys.argv[2:])
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "mindsetologie")
    env = dict(os.environ, HANDLE=HANDLE)
    for e in plan:
        if nur and e["slug"] not in nur: continue
        slides = e["slides"]; assert len(slides) <= 10, e["slug"]
        assert slides[-1][-1] == "Mehr davon:<br><b>Folge @mindsetologie.</b>", e["slug"]
        d = os.path.join(root, e["slug"]); os.makedirs(d, exist_ok=True)
        cap = caption(slides)
        full = json.dumps(slides, ensure_ascii=False) + cap
        for bad in ["–", "—", " - ", "AMATUSKA", "mentalexikon"]:
            assert bad not in full, (e["slug"], bad)
        json.dump(slides, open(f"{d}/slides.json", "w"), ensure_ascii=False, indent=1)
        open(f"{d}/caption.txt", "w").write(cap)
        for f in os.listdir(d):
            if f.endswith(".jpg"): os.remove(os.path.join(d, f))
        r = subprocess.run(["node", "build.js", d, f"{d}/slides.json", e["farbe"]], capture_output=True, text=True, env=env)
        print(e["slug"], e["farbe"], len(slides), len(cap), r.stdout.strip().replace("\n", " | "), r.stderr[:200])
