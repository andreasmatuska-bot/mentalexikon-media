"""Woche vom 05.10.2026: 14 Karussells für die freien Termine 12:00 und 16:00 vom 06.10. bis 12.10.2026.
Aufruf in karussells/_engine:  python3 woche_2026-10-05.py [Ausgabeordner]
Je Eintrag: (Ordnername, Quelle, Seite, Farbe, Termin, Art, Slides)
"""
import json, os, re, subprocess, sys
CTA = "Mehr davon:<br><b>Folge @mentalexikon.</b>"
B = lambda n: f"<b>{n}.</b> "
K = [
("23_paare_gewohnheiten", "DVRLsxZgrDt", "erfolgsart", "hell", "2026-10-06 12:00", "Liste mit Zahl", [
 ["Paare, die nach Jahrzehnten noch glücklich sind, hatten selten einfach Glück.", "<b>8 Gewohnheiten, die sie verbinden:</b>"],
 [B(1)+"Sie bedanken sich für das Selbstverständliche. Für den Kaffee, den Einkauf, den vollen Tank."],
 [B(2)+"Sie streiten über die Sache und lassen den Menschen in Ruhe.", B(3)+"Sie strafen einander nie mit tagelangem Schweigen."],
 [B(4)+"Sie berühren sich im Vorbeigehen. Eine Hand auf der Schulter, ein kurzer Kuss an der Tür."],
 [B(5)+"Sie sagen, was sie brauchen, und warten nicht darauf, dass der andere es errät."],
 [B(6)+"Sie fragen abends nach dem Tag und hören bei der Antwort wirklich zu.", B(7)+"Sie lachen miteinander, auch in schweren Wochen."],
 [B(8)+"Sie entscheiden sich füreinander. Auch an Tagen, an denen es Mühe kostet."],
 ["Fehlen diese Kleinigkeiten, passiert lange nichts Sichtbares.", "Bis man merkt, dass man sich nichts mehr erzählt."],
 ["Große Gesten sieht man auf Fotos.", "<b>Getragen wird eine Liebe von dem, was an einem gewöhnlichen Dienstag passiert.</b>", CTA]]),
("24_witz_als_tarnung", "DcbdLvlgphB", "erfolgsart", "schwarz", "2026-10-06 16:00", "Sätze zum Nachsprechen", [
 ["War doch nur Spaß.", "Mit diesem Satz wird aus einer Beleidigung ein Witz und aus dir jemand, der keinen Humor hat.", "<b>Das kannst du darauf antworten:</b>"],
 ["Manche Sprüche sind Sticheleien mit Hintertür.", "Lachst du mit, sitzt der Hieb. Wehrst du dich, war alles nur Spaß."],
 ["Ich finde das nicht lustig.", "Erklär mir den Witz. Ich verstehe ihn nicht."],
 ["Über wen lachen wir da gerade?", "Sag es bitte so, wie du es meinst."],
 ["Darüber lache ich nicht mit.", "Lass uns über etwas anderes reden."],
 ["Am Tisch lachen oft alle mit, damit die Stimmung hält.", "Geschützt wird so der, der austeilt. Allein bleibt, wer getroffen wurde."],
 ["Sitzt du daneben, kannst du das drehen.", "Ein einziger Satz genügt: Ich fand das gerade nicht in Ordnung."],
 ["Niemand muss über die eigene Demütigung lachen, damit der Abend angenehm bleibt.", "<b>Deine Würde wiegt mehr als die gute Stimmung am Tisch.</b>", CTA]]),
("25_ich_brauche_nichts", "DdMUiwOAgk7", "erfolgsart", "beige", "2026-10-07 12:00", "Gegenüberstellung", [
 ["Ich brauche nichts.", "Kaum ein Satz wird so oft gesagt und so selten gemeint.", "<b>Was oft damit gemeint ist:</b>"],
 ["<b>Gesagt:</b> Ich brauche nichts.", "<b>Gemeint:</b> Ich wünsche mir, dass du von allein darauf kommst."],
 ["<b>Gesagt:</b> Mach dir keine Umstände.", "<b>Gemeint:</b> Ich würde mich freuen, wenn sich einmal jemand Mühe für mich gibt."],
 ["<b>Gesagt:</b> Ist schon gut, ich mach das.", "<b>Gemeint:</b> Ich möchte ein einziges Mal nicht an alles denken müssen."],
 ["<b>Gesagt:</b> Mir ist alles recht.", "<b>Gemeint:</b> Ich traue mich nicht, etwas zu wollen."],
 ["Mit Bescheidenheit hat das wenig zu tun.", "Viele haben früh gelernt, dass man mit Wünschen zur Last fällt. Also wurden sie pflegeleicht."],
 ["Der andere kann aber keine Gedanken lesen.", "Er hört: Ich brauche nichts. Und glaubt es."],
 ["Wer Wünsche ausspricht, ist weder egoistisch noch anstrengend.", "Du musst dich für niemanden kleiner machen, um liebenswert zu sein."],
 ["Fang mit einem einzigen Satz an.", "<b>Ja. Das wünsche ich mir.</b>", CTA]]),
("26_stille_helfer", "DboHMZXgnaZ", "erfolgsart", "hell", "2026-10-10 16:00", "Geschichte", [
 ["Jeden Donnerstag hängt eine Tüte mit Einkäufen an einer Tür im dritten Stock.", "Kein Zettel. Kein Name.", "<b>Seit zwei Jahren:</b>"],
 ["Der Mann, der dort wohnt, ist 84.", "Seit seine Frau gestorben ist, schafft er die Treppen nur noch an guten Tagen."],
 ["Er hat nie jemanden um Hilfe gebeten.", "Er hätte auch nicht gewusst, wen."],
 ["Die Tüte kommt von der Nachbarin aus dem Erdgeschoss.", "Sie hat einmal gesehen, wie er auf halber Treppe stehen blieb und sich am Geländer festhielt."],
 ["Mehr war da nicht.", "Sie hat nicht lange gefragt, ob er etwas braucht. Sie hat hingesehen und eingekauft."],
 ["Im Haus weiß es bis heute niemand.", "Sie erzählt es nicht. Wozu auch."],
 ["Solche Menschen gibt es überall.", "Sie räumen den Schnee vom fremden Gehweg und warten, bis du sicher im Bus sitzt."],
 ["Menschlichkeit ist meistens leise.", "<b>Sie hängt donnerstags an einer Tür im dritten Stock.</b>", CTA]]),
("27_eifersucht", "DV6ZUv1Amhz", "erfolgsart", "schwarz", "2026-10-08 12:00", "Gegenüberstellung", [
 ["Uns wurde beigebracht, Eifersucht für einen Liebesbeweis zu halten.", "<b>Woran du Kontrolle und Liebe auseinanderhältst:</b>"],
 ["<b>Kontrolle fragt:</b> Wo warst du? Mit wem? Warum so lange?", "<b>Liebe fragt:</b> Wie war dein Abend?"],
 ["<b>Kontrolle</b> liest heimlich deine Nachrichten.", "<b>Liebe</b> legt das Handy weg, wenn du erzählst."],
 ["<b>Kontrolle</b> braucht jeden Tag einen neuen Beweis.", "<b>Liebe</b> glaubt dir beim ersten Mal."],
 ["<b>Kontrolle</b> macht deine Welt kleiner. Weniger Freunde, weniger Abende, weniger du.", "<b>Liebe</b> freut sich, wenn du aufblühst."],
 ["Hinter starker Eifersucht steckt oft eine Angst.", "Die Angst, nicht zu genügen und deshalb verlassen zu werden."],
 ["Kein Beweis der Welt macht diese Angst satt.", "Ruhiger wird es meist erst, wenn jemand spürt: Ich bin auch ohne Bestätigung genug."],
 ["Wer jeden Tag gehen könnte und trotzdem bleibt, hat sich wirklich entschieden."],
 ["Festhalten kann man nur Dinge.", "<b>Ein Mensch bleibt, weil er will.</b>", CTA]]),
("28_kleine_gesten", "DcEPUCbgs-I", "erfolgsart", "beige", "2026-10-08 16:00", "Geschichte", [
 ["Ihr Vater hat in vierzig Jahren kein einziges Mal gesagt, dass er sie liebt.", "<b>Er hatte dafür andere Sätze:</b>"],
 ["Hast du schon gegessen?", "Ich hab dir was mitgebracht."],
 ["Ruf an, wenn du angekommen bist.", "Zieh dir was an, es ist kalt draußen."],
 ["Nimm das mit, du hast doch nichts im Kühlschrank.", "Dann stand wieder eine volle Tasche im Flur."],
 ["Früher hat sie das genervt.", "Sie war erwachsen. Sie konnte selbst einkaufen."],
 ["Heute weiß sie, was er gemeint hat.", "Über Gefühle zu reden hatte er nie gelernt. Also hat er sich gekümmert."],
 ["Viele Menschen lieben so.", "Sie rufen ohne Grund an. Sie heben dir das letzte Stück auf. Sie bleiben wach, bis du zu Hause bist."],
 ["Sieh hin, solange sie da sind.", "<b>Eines Tages würdest du viel geben für eine volle Tasche im Flur.</b>", CTA]]),
("29_eltern_sprechen", "DXZphH6AnOg", "erfolgsart", "hell", "2026-10-09 12:00", "Szene", [
 ["Ein Junge sitzt auf der Treppe und hört, wie seine Eltern in der Küche über ihn reden.", "<b>Was er dort hört, kann ihn ein Leben lang begleiten:</b>"],
 ["Kinder hören mehr, als wir denken.", "Am genauesten hören sie zu, wenn sie glauben, dass es niemand merkt."],
 ["Was du deinem Kind direkt sagst, kann es anzweifeln.", "Was es zufällig mithört, hält es oft für die Wahrheit."],
 ["Hört es: Sie ist so anstrengend.", "Dann kann daraus werden: Ich bin zu viel."],
 ["Hört es: Hast du gesehen, wie lange er heute geübt hat?", "Dann kann daraus werden: Ich schaffe Dinge."],
 ["Aus solchen Sätzen wächst mit den Jahren eine innere Stimme.", "Sie spricht oft noch, wenn das Kind längst erwachsen ist."],
 ["Rede deshalb gut über dein Kind.", "Am Telefon. Beim Abendessen. Vor den Großeltern. So, dass es dich hören kann."],
 ["Zeig einem Kind, dass du es liebst.", "<b>Und lass es hören, wie du klingst, wenn du stolz bist.</b>", CTA]]),
("30_neuanfang", "DcL9_cCAkBX", "erfolgsart", "schwarz", "2026-10-09 16:00", "Gegenüberstellung", [
 ["Du hast neu angefangen und nennst es Scheitern.", "<b>Sieh dir an, was davor war:</b>"],
 ["<b>Davor</b> hast du dreimal überlegt, bevor du etwas gesagt hast.", "<b>Jetzt</b> sagst du es einfach."],
 ["<b>Davor</b> hast du leiser gelacht, damit es niemanden stört.", "<b>Jetzt</b> hörst du dich wieder lachen."],
 ["<b>Davor</b> hast du dich für jeden Wunsch entschuldigt.", "<b>Jetzt</b> bestellst du, worauf du Lust hast."],
 ["<b>Davor</b> wusstest du genau, was alle anderen brauchen.", "<b>Jetzt</b> lernst du wieder, was du selbst brauchst."],
 ["Wer sich jahrelang anpasst, merkt den Verlust selten an einem bestimmten Tag.", "Es geschieht in kleinen Schritten. Ein bisschen stiller. Ein bisschen blasser."],
 ["Irgendwann weißt du kaum noch, wie es sich anfühlt, ganz du selbst zu sein."],
 ["Dann ist ein Ende eine gute Nachricht.", "<b>Mit dem Loslassen beginnt das Wiederfinden.</b>", CTA]]),
("31_millennials", "DWPAdMrAhJ3", "erfolgsart", "beige", "2026-10-10 12:00", "Liste", [
 ["Wer zwischen 1981 und 1996 geboren wurde, ist in zwei Welten groß geworden.", "<b>Was viele von ihnen noch kennen:</b>"],
 ["Draußen spielen, bis die Straßenlaternen angehen.", "Telefonnummern auswendig wissen."],
 ["Ein Lied aus dem Radio aufnehmen und hoffen, dass der Moderator nicht reinredet."],
 ["Das Modem pfeifen hören und warten, bis ein einziges Bild geladen ist.", "Die erste SMS mit 160 Zeichen."],
 ["Sich verabreden und einfach da sein, ohne vorher zu schreiben.", "Fotos erst sehen, wenn der Film entwickelt ist."],
 ["Den eigenen Eltern das Smartphone erklären und den eigenen Kindern die Kassette."],
 ["Diese Generation weiß noch, wie still es ohne Internet war.", "Und sie war unter den ersten, die online arbeiten, lieben und leben lernten."],
 ["Sie musste sich öfter umstellen, als ihr lieb war.", "<b>Dafür findet sie sich heute in beiden Welten zurecht.</b>", CTA]]),
("32_stolz", "DdJ0S4-gumi", "erfolgsart", "hell", "2026-10-07 16:00", "Geschichte", [
 ["Zwei Brüder sprechen seit elf Jahren nicht miteinander.", "<b>Keiner weiß mehr genau, warum:</b>"],
 ["Es ging um das Haus der Eltern. Vielleicht auch um einen Satz bei der Beerdigung.", "Jeder wartete darauf, dass der andere den ersten Schritt macht."],
 ["Beide haben die Nummer noch im Handy.", "Beide haben sie in all den Jahren mehr als einmal angesehen."],
 ["Der Ältere schrieb an Weihnachten eine Nachricht.", "Dann löschte er sie wieder. Nächstes Jahr, dachte er."],
 ["So hält Stolz einen Streit am Leben.", "Er verspricht dir, dass später noch genug Zeit ist."],
 ["Aber niemand weiß, welches Gespräch das letzte war.", "Man merkt es erst, wenn kein weiteres mehr kommt."],
 ["Fällt dir gerade jemand ein?", "Dann schreib ihm heute. Drei Wörter reichen: Du fehlst mir."],
 ["Recht behalten kannst du auch allein.", "<b>Für den ersten Schritt ist es selten zu früh und manchmal zu spät.</b>", CTA]]),
("33_liebe_aussprechen", "DcymgsoAtCK", "erfolgsart", "schwarz", "2026-10-11 12:00", "Sätze zum Nachsprechen", [
 ["Die Liebe ist noch da.", "Du hast nur irgendwann aufgehört, sie auszusprechen.", "<b>Sätze, die schon zu lange fehlen:</b>"],
 ["Ich bin froh, dass es dich gibt.", "Für den Menschen, der jeden Tag da ist und es deshalb nie hört."],
 ["Danke, dass du das immer machst.", "Für alles, was längst selbstverständlich geworden ist."],
 ["Ich bin stolz auf dich.", "Auch Erwachsene warten manchmal ein halbes Leben auf diesen Satz."],
 ["Das habe ich von dir gelernt.", "Für deine Mutter. Für deinen Vater. Solange du es ihnen noch sagen kannst."],
 ["Ich liebe dich.", "Ohne Anlass. An einem ganz normalen Abend."],
 ["Wir denken: Das wissen sie doch längst.", "Aber etwas zu wissen ist anders, als es zu hören."],
 ["Gefühle halten Schweigen lange aus. Menschen weniger.", "<b>Sag es denen zuerst, bei denen du es für selbstverständlich hältst.</b>", CTA]]),
("34_mutter_spart", "DdorvwgggN3", "erfolgsart", "beige", "2026-10-11 16:00", "Geschichte", [
 ["Andere Mütter sparen für die Hochzeit ihrer Tochter.", "Diese Mutter hat für etwas anderes gespart.", "<b>Und lange kein Wort darüber verloren:</b>"],
 ["Jeden Monat legte sie einen kleinen Betrag zur Seite.", "Auf ein Konto, das nur auf den Namen ihrer Tochter lief."],
 ["Es war kein Geld für ein Kleid oder ein Fest."],
 ["Zum 18. Geburtstag gab sie ihr die Unterlagen und sagte:", "Das ist dafür, dass du nie bleiben musst, wo es dir nicht gut geht."],
 ["Sie selbst hatte diese Wahl lange nicht.", "Sie wollte gehen und wusste jahrelang nicht, wovon sie leben sollte."],
 ["Also sorgte sie dafür, dass ihre Tochter einen Satz nie sagen muss:", "Ich möchte gehen, aber ich kann nicht."],
 ["Zum Wertvollsten, was Eltern mitgeben können, gehört Selbstständigkeit.", "Ein eigenes Einkommen. Ein eigenes Konto. Das Wissen, dass man es auch allein schafft."],
 ["Sie hat ihrer Tochter keinen Mann gewünscht, der sie versorgt.", "Sie hat ihr gewünscht, dass sie nie einen braucht."],
 ["So verändert eine Generation die nächste.", "<b>Eine Frau findet die Tür und hält sie der Tochter auf.</b>", CTA]]),
("35_glimmers", "DVTu0urgouw", "erfolgsart", "hell", "2026-10-12 12:00", "Erklärstück", [
 ["Jeder kennt Trigger.", "Kaum jemand kennt ihr Gegenteil.", "<b>Es heißt Glimmer:</b>"],
 ["Ein Trigger ist ein Reiz, der deinen Körper in Alarm versetzt.", "Ein Glimmer ist ein Reiz, der ihm zeigt: Gerade ist alles gut."],
 ["Glimmer sind winzig.", "Die Sonne auf dem Küchentisch. Der Geruch von frischem Kaffee. Ein Lied, das du seit Jahren kennst."],
 ["Oder ein Mensch.", "Jemand lächelt dich im Vorbeigehen an. Dein Kind schläft neben dir ein."],
 ["In solchen Momenten kann dein Nervensystem kurz herunterfahren.", "Die Schultern sinken. Der Atem wird tiefer."],
 ["Dein Kopf ist darauf eingestellt, Gefahren zu finden.", "Das Gute rauscht deshalb oft unbemerkt vorbei."],
 ["Du kannst das üben.", "Halte bei jedem Glimmer ein paar Sekunden inne und sag dir still: Das ist gerade schön."],
 ["Je öfter du das tust, desto leichter fallen dir solche Momente auf."],
 ["Schau dich jetzt einmal um.", "<b>Irgendwo in deiner Nähe ist gerade einer.</b>", CTA]]),
("36_verbindung_schuetzen", "DZFvuw3gmSQ", "erfolgsart", "schwarz", "2026-10-12 16:00", "Geschichte", [
 ["Sie haben sich nie laut gestritten.", "Niemand hat betrogen. Niemand ist gegangen.", "<b>Trotzdem waren sie sich nach zwölf Jahren fremd:</b>"],
 ["Es fing harmlos an.", "Der gemeinsame Abend fiel aus, weil beide müde waren. Dann noch einmal. Dann immer."],
 ["Sie erzählte von ihrem Tag, und er sah dabei aufs Handy.", "Irgendwann rief sie lieber ihre Schwester an."],
 ["Er schlug einen Ausflug vor, und sie hatte zu viel zu tun.", "Irgendwann schlug er nichts mehr vor."],
 ["Gespräche gab es weiter.", "Über Termine, Einkäufe und die Frage, wer die Kinder abholt."],
 ["Aufgehört zu lieben hat keiner von beiden.", "Es hat sich bloß lange niemand mehr um die Verbindung gekümmert."],
 ["So geht Nähe meistens verloren.", "Langsam und ohne dass es an einem bestimmten Tag passiert wäre."],
 ["Was sie schützt, ist unspektakulär.", "Zeit zu zweit. Echte Aufmerksamkeit. Etwas, das man nur miteinander erlebt."],
 ["Viele Paare fangen erst an, wenn es fast zu spät ist.", "<b>Fang an, solange es noch leichtfällt.</b>", CTA]]),
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
    OUT = sys.argv[1] if len(sys.argv) > 1 else "w_2026-10-05"
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
