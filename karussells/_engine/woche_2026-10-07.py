"""Woche vom 07.10.2026: 4 Karussells für die freien Termine 12:00 und 16:00 am 13.10. und 14.10.2026.
Aufruf in karussells/_engine:  python3 woche_2026-10-07.py [Ausgabeordner]
Je Eintrag: (Ordnername, Quelle, Seite, Farbe, Termin, Art, Slides)
"""
import json, os, re, subprocess, sys
CTA = "Mehr davon:<br><b>Folge @mentalexikon.</b>"
B = lambda n: f"<b>{n}.</b> "
K = [
("37_freundschaft_lagerfeuer", "DbQwF_Egnbx", "erfolgsart", "beige", "2026-10-13 12:00", "Geschichte oder Szene", [
 ["Eine Freundschaft endet selten mit einem Knall.", "Meistens wird sie einfach leiser.", "<b>Ein Bild, das es leichter macht:</b>"],
 ["Erst antwortet jemand später.", "Dann seltener. Irgendwann schreibt ihr euch nur noch zum Geburtstag."],
 ["Du suchst den Fehler bei dir.", "Was habe ich gesagt? Was habe ich übersehen?"],
 ["Oft gibt es keinen Fehler.", "Ein Umzug, ein Kind, eine neue Arbeit. Das Leben des anderen hat sich verschoben."],
 ["Stell dir dein Leben als Lagerfeuer vor.", "Manche setzen sich für fünf Minuten dazu. Andere bleiben die halbe Nacht und erzählen."],
 ["Einige stehen früher auf, weil sie weitermüssen.", "Dein Feuer ist deshalb nicht weniger wert."],
 ["Dass jemand gegangen ist, nimmt den Abenden nichts, an denen ihr zusammen dort gesessen habt."],
 ["Du musst niemanden überreden, sitzen zu bleiben.", "Du musst nur das Feuer am Brennen halten."],
 ["Rück ein Stück, wenn jemand Neues kommt.", "<b>Wer Wärme sucht, findet den Weg zu dir.</b>", CTA]]),
("38_liebe_im_kleinen", "DdwVTn0AhOn", "erfolgsart", "hell", "2026-10-13 16:00", "Liste mit Zahl", [
 ["Blumen und Schmuck erkennt jeder als Liebesbeweis.", "Die ehrlichsten Liebesbeweise sehen anders aus.", "<b>Woran du sie erkennst:</b>"],
 [B(1)+"Auf deinem Platz liegt ein neues Ladekabel. Deins war seit Monaten kaputt, und du hast es nur einmal erwähnt."],
 [B(2)+"Dein Mittagessen steht fertig im Kühlschrank. Genau an dem Morgen, an dem du keine Zeit hast."],
 [B(3)+"Dein Lieblingsjoghurt liegt im Einkaufswagen, obwohl er nicht auf dem Zettel stand.", B(4)+"Die Heizung im Bad läuft schon, wenn du aufstehst."],
 [B(5)+"Jemand merkt sich, wovor du Angst hattest, und fragt am Tag danach, wie es war."],
 [B(6)+"Das letzte Stück Kuchen bleibt für dich liegen.", B(7)+"Du wirst zugedeckt, wenn du auf dem Sofa einschläfst."],
 ["Keiner dieser Momente taugt für ein Foto.", "Aber in jedem steckt dieselbe Botschaft."],
 ["Ich sehe dich. Ich habe mir gemerkt, was du gesagt hast.", "Und was dich beschäftigt, ist mir nicht egal."],
 ["Achte diese Woche darauf, was jemand still für dich erledigt.", "<b>Und sag Danke dafür.</b>", CTA]]),
("39_was_wir_bereuen", "DWHN04BAj9M", "erfolgsart", "schwarz", "2026-10-14 12:00", "Liste mit Zahl", [
 ["Kaum jemand bereut am Ende, zu wenig gearbeitet zu haben.", "<b>4 Dinge, die sich Menschen im Rückblick oft wünschen:</b>"],
 [B(1)+"Gesagt zu haben, was sie fühlten.", "Die Zuneigung war da. Ausgesprochen wurde sie zu selten."],
 [B(2)+"Mehr Zeit mit den Menschen, die ihnen wichtig waren.", "Mit Freunden, bei denen sie sich immer melden wollten."],
 [B(3)+"Sich erlaubt zu haben, zufrieden zu sein.", "Statt zu warten, bis alles perfekt ist."],
 [B(4)+"Weniger Kritik an dem Menschen neben ihnen.", "Fehler fallen uns schneller auf als das, was gut läuft."],
 ["Von einer sehr alten Frau wird dieser Satz erzählt:", "Ich wünschte, ich hätte ihn öfter geküsst und weniger kritisiert."],
 ["Die Wäsche, der Abwasch und die offene Rechnung kommen in solchen Rückblicken kaum vor."],
 ["Für nichts davon ist es zu spät.", "Ein Anruf. Eine Umarmung an der Tür. Ein Satz, den du sonst herunterschluckst."],
 ["Du musst dafür nicht alt werden.", "<b>Du kannst heute Abend damit anfangen.</b>", CTA]]),
("40_nicht_alles_tragen", "DdCDN3SgmYa", "erfolgsart", "beige", "2026-10-14 16:00", "Sätze zum Nachsprechen", [
 ["Du hilfst so zuverlässig, dass niemand mehr fragt, ob du kannst.", "Es wird einfach vorausgesetzt.", "<b>Sätze, mit denen du Last abgibst:</b>"],
 ["Diesmal kann ich das nicht übernehmen.", "Dafür habe ich diese Woche keine Kraft."],
 ["Wer von euch kümmert sich darum?", "Ich habe es die letzten Male gemacht."],
 ["Ich helfe dir gern, aber heute nicht.", "Das musst du diesmal bitte selbst klären."],
 ["Ich brauche dabei Unterstützung.", "Allein schaffe ich das nicht mehr."],
 ["Am Anfang fühlen sich solche Sätze wie Verrat an.", "Das kennen viele, die immer die Verlässlichen waren."],
 ["Alle haben sich an deine Hilfe gewöhnt.", "Dass sie sich auf dich verlassen, heißt nicht, dass du alles tragen musst."],
 ["Du darfst etwas abstellen, das du lange getragen hast.", "<b>Es bricht weniger zusammen, als du denkst.</b>", CTA]]),
]
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
    return "\n\n".join(out) + "\n\nMehr davon: folge @mentalexikon."
if __name__ == "__main__":
    OUT = sys.argv[1] if len(sys.argv) > 1 else "w_2026-10-07"
    os.makedirs(OUT, exist_ok=True)
    meta = []
    for slug, src, seite, th, termin, art, slides in K:
        assert len(slides) <= 10
        d = f"{OUT}/{slug}"; os.makedirs(d, exist_ok=True)
        json.dump(slides, open(f"{d}/slides.json", "w"), ensure_ascii=False, indent=1)
        cap = caption(slides); open(f"{d}/caption.txt", "w").write(cap)
        full = json.dumps(slides, ensure_ascii=False) + cap
        for bad in ["–", "—", " - ", "AMATUSKA"]:
            assert bad not in full, (slug, bad)
        r = subprocess.run(["node", "build.js", f"{d}/img", f"{d}/slides.json", th], capture_output=True, text=True)
        print(slug, th, len(slides), len(cap), r.stdout.strip().replace("\n", " | "), r.stderr[:200])
        meta.append({"slug": slug, "quelle": src, "seite": seite, "farbe": th, "termin": termin, "art": art, "slides": len(slides)})
    json.dump(meta, open(f"{OUT}/meta.json", "w"), ensure_ascii=False, indent=1)
