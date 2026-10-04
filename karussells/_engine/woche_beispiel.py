import json, os, re, subprocess, sys
CTA = "Mehr davon:<br><b>Folge @mentalexikon.</b>"
B = lambda n: f"<b>{n}.</b> "
K = [
("02_streit_abkuehlen", "DcrMvz-DF2K", [
 ["12 Sätze, die einen Streit abkühlen.", "Bevor jemand etwas sagt, das er nie wieder zurücknehmen kann.", "<b>Merk sie dir:</b>"],
 [B(1)+"Ich will das mit dir klären. Ich will nicht gewinnen.", B(2)+"Sag mir bitte noch einmal, was bei dir angekommen ist."],
 [B(3)+"Ich bin gerade zu wütend, um fair zu bleiben. Gib mir 20 Minuten.", B(4)+"Was davon ist dir am wichtigsten?"],
 [B(5)+"Da hast du recht.", B(6)+"Das wusste ich nicht."],
 [B(7)+"Ich merke, dass ich dir wehgetan habe. Das wollte ich nicht.", B(8)+"Lass uns dort anfangen, wo es gekippt ist."],
 [B(9)+"Es tut mir leid.", "Der schwerste von allen. Er funktioniert nur ohne Aber. Das Aber löscht den ganzen Satz."],
 [B(10)+"Ich brauche dich hier nicht als Gegner.", B(11)+"Was brauchst du von mir, damit das aufhört?"],
 [B(12)+"Wir sind noch nicht fertig. Aber für heute ist es genug."],
 ["Keiner dieser Sätze gewinnt einen Streit.", "<b>Sie beenden nur den Teil, in dem beide verlieren.</b>", CTA]]),
("03_hochsensibel", "DcyvP6eAPF0", [
 ["Hochsensibel heißt nicht empfindlich.", "Es heißt, dass bei dir mehr ankommt, als andere senden.", "<b>9 Dinge, die dich deshalb Kraft kosten:</b>"],
 [B(1)+"Eine offene Tür im Rücken.", B(2)+"Der Satz: Stell dich nicht so an."],
 [B(3)+"Besuch, der sich nicht ankündigt.", B(4)+"Großraumbüros."],
 [B(5)+"Small Talk, der kein Ende findet.", B(6)+"Schlechte Laune von jemandem im Raum."],
 [B(7)+"Grelles Licht von der Decke.", B(8)+"Entscheidungen unter Zeitdruck."],
 [B(9)+"Der Satz: Du bist zu empfindlich."],
 ["Der letzte Satz kostet am meisten.", "Er macht aus einer Eigenschaft einen Fehler. Wer ihn oft genug hört, hält sich irgendwann selbst für falsch gebaut."],
 ["Nichts davon ist Schwäche.", "<b>Die Welt kommt bei dir nur in einer anderen Lautstärke an.</b>", CTA]]),
("04_allein_leben", "DdMnc_yAL2t", [
 ["Immer mehr Menschen entscheiden sich bewusst dafür, allein zu leben.", "Ehe und Partnerschaft sind für sie kein Ziel mehr.", "<b>Warum das so ist:</b>"],
 ["Filme und Werbung haben uns beigebracht, dass man irgendwann ankommen muss.", "Dass man dann ausgewählt wurde und endlich zufrieden sein darf."],
 ["Aber Beziehungen sind Arbeit.", "Manchen Menschen bringen sie keine Ruhe, sondern Anspannung und weniger Freiheit."],
 ["Bewusst allein zu leben heißt, dass anderes Vorrang hat.", "Freundschaften. Arbeit. Reisen. Ein eigener Raum."],
 ["Es heißt, entscheiden zu können, ohne sich vor jemandem zu rechtfertigen."],
 ["Und es heißt, die Hoffnung losgelassen zu haben, dass irgendwann jemand kommt und einen rettet."],
 ["Was viele Paare nie aussprechen:", "Sie sind seit Jahrzehnten zusammen und leben nur noch nebeneinander her."],
 ["Sie fragen sich, wie es anders wäre, und erfahren es nie.", "Wer bewusst allein lebt, findet es heraus."],
 ["Es ist keine Notlösung.", "<b>Für manche Menschen ist es die bessere Entscheidung.</b>", CTA]]),
("05_gehen", "Ddby-5RgJIk", [
 ["Gehen ist eines der stärksten Werkzeuge für deinen Kopf.", "Und kaum jemand nutzt es bewusst.", "<b>Das passiert dabei:</b>"],
 ["Beim Gehen ist dein ganzer Körper im Wechsel aktiv.", "Links, rechts, links, rechts. Viele kommen dabei auch im Kopf in Bewegung."],
 ["Gedanken, die im Sitzen kreisen, kommen im Gehen voran.", "Vielen fällt es so leichter, Belastendes und starke Gefühle zu sortieren."],
 ["Gleichzeitig kann Gehen dein Nervensystem beruhigen.", "Schon 10 bis 20 Minuten können deinen Körper in den Ruhemodus bringen."],
 ["Entscheidend ist nicht die Strecke.", "Entscheidend ist, dass du es regelmäßig tust."],
 ["<b>Geh, bevor</b> du eine wichtige Entscheidung triffst.", "<b>Geh, bevor</b> du auf eine Nachricht antwortest, die dich aufwühlt."],
 ["<b>Geh mit dem anderen,</b> wenn ihr streitet.", "<b>Geh nach</b> einem schweren Gespräch."],
 ["<b>Geh,</b> wenn du Trauer, einen Verlust oder eine Trennung verarbeiten musst."],
 ["Du brauchst keine Ausrüstung und keinen Plan.", "<b>Du brauchst nur die Tür und zwanzig Minuten.</b>", CTA]]),
("06_alleinsein", "DdZkkevgIDc", [
 ["Dein Nervensystem braucht Zeit mit Menschen.", "Und es braucht Zeit ohne sie."],
 ["Im Alleinsein findet dein Körper zurück ins Gleichgewicht.", "Wie viel jemand davon braucht, ist bei jedem anders."],
 ["Trotzdem hat Alleinsein einen schlechten Ruf.", "Es gilt als traurig. Als etwas für Menschen, die sonst niemanden haben.", "<b>5 Zeichen, dass du es gerade brauchst:</b>"],
 [B(1)+"Du bist gereizt. Schon das Atmen der anderen geht dir auf die Nerven."],
 [B(2)+"Dein Körper meldet sich. Kopfschmerzen, Verspannungen, alte Beschwerden sind wieder da, ohne dass du weißt, warum."],
 [B(3)+"Du lässt Nachrichten liegen und zuckst zusammen, wenn das Telefon klingelt."],
 [B(4)+"Du kommst nicht zur Ruhe. Du rennst, machst und arbeitest immer weiter."],
 [B(5)+"Du bist wütend und weißt nicht, worauf. Meist kommen dann deine eigenen Bedürfnisse zu kurz."],
 ["Alleinsein ist kein Rückzug von den Menschen.", "<b>Es ist die Voraussetzung dafür, dass du für sie da sein kannst.</b>", CTA]]),
("07_sympathie", "Dcx4ljkAFJu", [
 ["Sympathie entscheidet sich selten an großen Dingen.", "Sie entscheidet sich an Kleinigkeiten, die jeder bemerkt.", "<b>10 Dinge, die dich unsympathisch machen:</b>"],
 [B(1)+"Den Namen des anderen nie benutzen.", B(2)+"Über Menschen reden, die nicht dabei sind."],
 [B(3)+"Jede Geschichte übertrumpfen.", B(4)+"Aufs Handy schauen, während jemand mit dir spricht."],
 [B(5)+"Den Kellner anders behandeln als die Gäste am Tisch."],
 [B(6)+"Nie eine Frage stellen.", B(7)+"Komplimente machen, an denen ein Aber hängt."],
 [B(8)+"Immer recht behalten wollen.", B(9)+"Zu spät kommen und es lustig finden."],
 [B(10)+"Sich nie entschuldigen."],
 ["Punkt 5 ist der zuverlässigste von allen.", "Wie jemand mit dem Kellner umgeht, verrät mehr als alles, was er am Tisch über sich erzählt."],
 ["Die meisten wollen Sympathie gewinnen.", "<b>Meistens reicht es, sie nicht zu verspielen.</b>", CTA]]),
("08_respektlos_stoppen", "DdoCQfbAOMO", [
 ["So stoppst du jemanden sofort, der respektlos mit dir umgeht.", "<b>Ohne laut zu werden:</b>"],
 ["Wird jemand unhöflich, wollen wir uns verteidigen.", "Wir sagen: So redest du nicht mit mir. Warum bist du so?"],
 ["Genau das bringt uns aus der Ruhe.", "Und es zeigt dem anderen, wie viel Gewicht seine Worte haben."],
 ["Selbstsichere Menschen wissen: Unhöflichkeit ist selten persönlich gemeint.", "Meistens ist der andere unsicher, überreizt oder beides."],
 ["Stell stattdessen eine ruhige, direkte Frage.", "Dann muss er sich selbst erklären."],
 ["Hilf mir zu verstehen, was du damit meinst.", "Glaubst du, dieser Kommentar bringt uns weiter?"],
 ["Das klingt ziemlich hart. Was steckt dahinter?"],
 ["Damit rechnet fast niemand.", "Die leise Reaktion nimmt ihn in die Verantwortung und setzt eine klare Grenze."],
 ["Eine ruhige Frage gibt die Verantwortung dorthin zurück, wo sie hingehört.", "<b>Du musst dich nicht erklären, um dich zu behaupten.</b>", CTA]]),
("09_tochter_und_sohn", "DdhK3w6AGyM", [
 ["Sie hat als Kind alle versorgt.", "Er hat als Kind gelernt, immer zu funktionieren.", "<b>Warum genau diese beiden sich finden:</b>"],
 ["Sie fühlte sich früh für alle und alles verantwortlich.", "Niemand fragte, wie es ihr ging. Sie regelte die Stimmung der ganzen Familie."],
 ["Er stand als Kind unter Druck und Kontrolle.", "Also tat er so, als hätte er alles im Griff. Der brave Junge, auf den man sich verlassen kann."],
 ["Sie fühlt sich zu ihm hingezogen, weil er sich wirklich für ihr Inneres interessiert.", "Seine ruhige Art lässt ihre Wachsamkeit sinken."],
 ["Er fühlt sich zu ihr hingezogen, weil sie sich kümmert.", "Endlich eine Pause von dem Druck, den er kennt."],
 ["Doch je enger es wird, desto mehr weicht er aus.", "Spricht sie ein Problem an, hört er Kritik und geht in Abwehr."],
 ["Sie fühlt sich allein gelassen. Genau wie früher.", "Sie drängt, er zieht sich zurück."],
 ["Das ist ihr Kreislauf.", "Und er dreht sich so lange, bis einer von beiden ihn erkennt."],
 ["Zwei Menschen wiederholen hier nicht ihre Liebe.", "<b>Sie wiederholen ihre Kindheit.</b>", CTA]]),
("10_beziehungen_wandel", "DduGYCkgFaP", [
 ["In Beziehungen verändert sich gerade etwas Grundlegendes.", "Menschen opfern ihre innere Ruhe nicht mehr für Freundschaft oder Liebe.", "<b>Was dahintersteckt:</b>"],
 ["Lange ging es bei Gesundheit nur um Ernährung und Bewegung.", "Dabei prägt uns kaum etwas so stark wie die Menschen, mit denen wir unsere Zeit verbringen."],
 ["Wir sind für Verbindung gemacht.", "Und diese Verbindung wirkt bis in den Körper."],
 ["Manche Menschen übernehmen nie Verantwortung.", "Sie erwarten, dass du es immer wieder für sie richtest."],
 ["Dein Körper bezahlt dafür.", "Er bleibt im Stress, wenn du zu lange Verständnis hast und nie zur Ruhe kommst."],
 ["Anders als die Generationen vor uns sind wir nicht mehr bereit, diesen Preis zu zahlen."],
 ["Wir glauben nicht mehr, dass Selbstlosigkeit heißt, sich alles gefallen zu lassen."],
 ["Wir wählen Beständigkeit.", "Statt der Unruhe, die wir lange Schmetterlinge genannt haben."],
 ["Ein Mensch kann dich lieben und dir trotzdem nicht guttun.", "<b>Dein Körper entscheidet mit, wer bleiben darf.</b>", CTA]]),
("11_liebe_wahrheiten", "Dc5uLKWgAJY", [
 ["Liebe ist nicht das Gefühl am Anfang.", "Sie ist das, was danach jeden Tag entschieden wird.", "<b>10 Wahrheiten, die kaum jemand hören will:</b>"],
 [B(1)+"Liebe allein reicht nicht.", B(2)+"Verliebtheit geht vorbei."],
 [B(3)+"Niemand ändert sich, nur weil du es dir wünschst.", B(4)+"Du kannst jemanden lieben und trotzdem nicht mit ihm leben."],
 [B(5)+"Aufmerksamkeit ist die eigentliche Währung.", B(6)+"Wer dich warten lässt, hat sich entschieden."],
 [B(7)+"Streit ist kein schlechtes Zeichen.", B(8)+"Am Ende verzeiht man nicht die Tat. Man verzeiht dem Menschen."],
 [B(9)+"Verschiedene Lebenspläne kosten mehr als jeder Streit.", B(10)+"Manchmal ist niemand schuld."],
 ["Die siebte überrascht die meisten.", "Nicht der Streit sollte dir Sorgen machen. Das Schweigen sollte es."],
 ["Keine dieser Wahrheiten macht die Liebe kleiner.", "<b>Sie machen nur deine Erwartung ehrlicher.</b>", CTA]]),
("12_mental_load", "DdbRozTAEj6", [
 ["Deinem Partner Entscheidungen abzunehmen, ist eine Form von Liebe.", "<b>Warum Mental Load so viele Beziehungen belastet:</b>"],
 ["Mental Load ist die unsichtbare Arbeit im Hintergrund.", "Das ständige Mitdenken, das den Alltag am Laufen hält."],
 ["Es geht nicht nur ums Erledigen.", "Es geht ums Erinnern, Vorausdenken, Planen und Abstimmen."],
 ["Wer fast alles davon trägt, macht nicht nur mehr.", "Er denkt an alles. So wächst der Groll."],
 ["Was er dann nicht hören will:", "Sag mir einfach, was ich tun soll. Schreib mir eine Liste."],
 ["Das macht die Last größer, nicht kleiner.", "Jetzt muss er auch noch dich organisieren."],
 ["Entlasten sieht anders aus.", "Etwas erledigen, ohne darum gebeten zu werden. Eine Entscheidung treffen, damit der andere es nicht muss."],
 ["Eine Sache ganz übernehmen.", "Selbst sehen, was ansteht. Termine und Erinnerungen selbst im Blick haben."],
 ["Niemand braucht einen Partner, der auf Ansage hilft.", "<b>Gebraucht wird jemand, der von allein sieht, was zu tun ist.</b>", CTA]]),
("13_konter", "Dc1KexVDMmn", [
 ["Der beste Konter ist nicht der lauteste.", "Es ist der, auf den es keine Antwort gibt.", "<b>9 Reaktionen, die jeden Spruch entwaffnen:</b>"],
 ["Wer zurückschießt, liefert dem anderen genau den Widerstand, den er gesucht hat."],
 [B(1)+"Das war jetzt unnötig.", B(2)+"Meinst du das ernst?"],
 [B(3)+"Sag das bitte noch mal. Langsamer.", B(4)+"Und weiter?"],
 [B(5)+"Was willst du damit erreichen?", B(6)+"Kann sein."],
 [B(7)+"Interessant, dass dir das so wichtig ist.", B(8)+"Darüber diskutiere ich nicht."],
 [B(9)+"Nichts sagen. Ihn einfach nur ansehen."],
 ["Alle neun tun dasselbe.", "Sie nehmen dem Spruch die Bühne, statt ihn zu beantworten. Kaum ein Spruch überlebt eine ruhige Rückfrage."],
 ["Es gewinnt nicht, wer den besseren Satz hat.", "<b>Es gewinnt, wer am Ende noch über sein eigenes Thema spricht.</b>", CTA]]),
("14_kinder_in_erwachsenen", "DdgAY73APCy", [
 ["Viele Menschen sind Kinder in erwachsenen Körpern.", "<b>Woran du echte Reife erkennst:</b>"],
 ["Bekommt ein Kind nicht, was es braucht, kann es Entwicklungsschritte überspringen.", "Als Erwachsener fällt dieser Mensch unter Druck in alte Muster zurück."],
 ["Dann wird gespottet und geschrien.", "Türen knallen. Oder es wird zur Strafe geschwiegen."],
 ["In Beziehungen fehlt diesen Menschen, was es dafür braucht.", "Gefühle regulieren. Streit lösen. Vernünftig miteinander reden."],
 ["Sie erleben Nähe als anstrengend.", "Und geben dem Partner die Schuld an jedem Problem."],
 ["Ein reifer Mensch kommt mit Stress zurecht.", "Er verschwindet nicht, wenn es schwierig wird."],
 ["Er sucht den Fehler nicht immer bei den anderen.", "Er hält ein Gefühl aus, bis es vorbeigeht."],
 ["Und er kann zuhören, auch wenn er anderer Meinung ist.", "Widerspruch bedroht ihn nicht."],
 ["Reife hat nichts mit dem Alter zu tun.", "<b>Sie zeigt sich daran, ob jemand sich selbst aushält.</b>", CTA]]),
("15_fragen_fuer_naehe", "Ddg1MbtgPAv", [
 ["Willst du jemandem wirklich nahe sein, musst du dich für ihn interessieren.", "<b>4 Arten von Fragen, die echte Nähe schaffen:</b>"],
 ["Nähe entsteht, wenn wir neugierig sind und ganz zuhören.", "Mit einer Frage fängt es an."],
 ["<b>Gefühlsfragen</b>", "Wann warst du zuletzt richtig begeistert? Wann hast du dich zuletzt verstanden gefühlt?"],
 ["<b>Interessenfragen</b>", "Was beschäftigt dich gerade wirklich? Was hast du zuletzt über dich gelernt?"],
 ["<b>Zukunftsfragen</b>", "Worauf arbeitest du gerade hin? Wovon willst du mehr, wovon weniger?"],
 ["<b>Leichte Fragen</b>", "Wann hast du zuletzt Tränen gelacht? Mit welchem Hobby würdest du gern anfangen?"],
 ["Manche Menschen reden nur über sich.", "Eine Frage zurück kommt nie. So kann keine Nähe entstehen."],
 ["Nähe entsteht nicht, weil jemand viel von sich erzählt.", "<b>Sie entsteht, weil jemand dich wirklich fragt.</b>", CTA]]),
("16_schwarzes_schaf", "DdmdJS3gC4k", [
 ["7 Dinge, die das schwarze Schaf der Familie ausmachen.", "Also den Menschen, der den Kreislauf durchbricht."],
 [B(1)+"Es hinterfragt alles.", "Es folgt der eigenen Intuition und gilt deshalb schnell als schwierig."],
 [B(2)+"Es ist sehr feinfühlig.", "Es sieht, was andere nicht sehen wollen, und spürt, was unausgesprochen bleibt."],
 [B(3)+"Es sucht tiefe Verbindungen.", "Es will nicht nur dazugehören. Es will wirklich gekannt werden."],
 [B(4)+"Es wurde zutiefst missverstanden.", "Aus dem Gefühl, nie gesehen zu werden, ist großes Mitgefühl gewachsen."],
 [B(5)+"Es versteht Erfolg anders.", "Nach den eigenen Maßstäben leben, nicht nach den Erwartungen der anderen."],
 [B(6)+"Es trägt eine Weisheit in sich, die nur entsteht, wenn man einmal ganz unten war."],
 [B(7)+"Es hält die Wahrheit hoch.", "Es stellt die Fragen, denen alle anderen ausweichen."],
 ["Wer aus der Reihe fällt, ist nicht der Fehler im System.", "<b>Oft ist er der Einzige, der hinsieht.</b>", CTA]]),
("17_reife_saetze", "DctjwBQgAUu", [
 ["Reife erkennst du nicht daran, wie jemand redet, wenn alles gut läuft.", "<b>11 Sätze, die nur reife Menschen sagen:</b>"],
 [B(1)+"Ich habe nicht richtig zugehört. Sag es bitte noch mal.", B(2)+"Ich weiß es nicht."],
 [B(3)+"Das war mein Fehler.", B(4)+"Das muss ich erst einmal sacken lassen."],
 [B(5)+"Wie genau meinst du das?", B(6)+"Ich bin schlecht gelaunt. Das hat nichts mit dir zu tun."],
 [B(7)+"Nein.", B(8)+"Ich habe meine Meinung geändert."],
 [B(9)+"Das schaffe ich nicht.", B(10)+"Ich verstehe dich und sehe es trotzdem anders."],
 [B(11)+"Wie geht es dir damit?"],
 ["Jeder dieser Sätze kostet in dem Moment etwas.", "Stolz. Bequemlichkeit. Das letzte Wort."],
 ["Reife ist kein Alter.", "<b>Sie ist eine Wortwahl.</b>", CTA]]),
("18_trauer_saetze", "Dc3ByIqDOIq", [
 ["Wenn jemand einen Menschen verloren hat, sagen die meisten lieber gar nichts.", "<b>11 Sätze, die mehr helfen als Schweigen:</b>"],
 [B(1)+"Ich weiß nicht, was ich sagen soll.", B(2)+"Erzähl mir von ihm."],
 [B(3)+"Ich denke an dich.", B(4)+"Ich komme am Donnerstag um sechs und bringe Essen mit."],
 [B(5)+"Du musst nicht reden.", B(6)+"Das ist so unfair."],
 [B(7)+"Ich vermisse ihn auch.", B(8)+"Wie geht es dir heute?"],
 [B(9)+"Mir ist etwas eingefallen, das er einmal gesagt hat."],
 [B(10)+"Du kannst hier nichts falsch machen.", B(11)+"Ich bin auch in einem halben Jahr noch da."],
 ["Der falsche Satz ist fast nie das Problem.", "<b>Das Schweigen ist es.</b>", CTA]]),
("19_unreife_mutter", "DdQ0vlQgHQv", [
 ["Eine emotional unreife Mutter ist innerlich nie erwachsen geworden.", "<b>Was das mit ihren Kindern macht:</b>"],
 ["Es geht vor allem um ihre Bedürfnisse.", "Und darum, wie sie nach außen wirkt. Das Bild ist alles."],
 ["Ihr fehlt, was eine Mutter bräuchte.", "Gefühle regulieren. Streit lösen. Spüren, wie es dem anderen gerade geht."],
 ["In ihr sitzt viel Scham.", "Und die gibt sie oft an ihre Kinder weiter."],
 ["Du hast Sätze gehört wie:", "Du bist zu empfindlich. So war das nie. Ich habe alles für dich aufgegeben."],
 ["Und diese Sätze hast du nie gehört:", "Ich höre dir zu. Wie geht es dir damit? Das hätte ich nicht tun sollen."],
 ["Du lernst früh, dass für deine Gefühle kein Platz ist.", "Die Stimmung im ganzen Haus bestimmt sie."],
 ["Was bleibt, sieht man von außen nicht.", "Wenig Selbstwert. Der Drang, es allen recht zu machen. Der Glaube, sich Liebe verdienen zu müssen."],
 ["Es war nie deine Aufgabe, sie glücklich zu machen.", "<b>Du hast es nur so gelernt.</b>", CTA]]),
("20_dein_mensch", "DdmCqdjAPTF", [
 ["Dein Körper sagt dir, wann du deinem Menschen begegnet bist.", "Es fühlt sich nicht wie ein Feuerwerk an.", "<b>Sondern so:</b>"],
 ["Echte Liebe ist beständig und verlässlich.", "Er betritt den Raum, und dein ganzer Körper fühlt sich sicher."],
 ["Er tut, was er sagt.", "Dein Herz schlägt ruhiger. Seine Stimme macht deinen Atem langsamer."],
 ["In deinen dunklen Momenten will er dich nicht verändern.", "Er redet dir deine Gefühle nicht aus."],
 ["Er hört zu. Er hält die Stille aus.", "Und er sagt, so oft es nötig ist: Ich bleibe."],
 ["Er droht nicht damit, zu gehen, wenn es schwer wird."],
 ["Jedes Mal, wenn ihr nach einem Streit wieder zueinanderfindet, wächst die Sicherheit."],
 ["Liebe ist keine Achterbahn.", "Und kein Kampf, der sich als Leidenschaft verkleidet."],
 ["Wenn Liebe sich ruhig anfühlt, fehlt ihr nichts.", "<b>Dein Körper hört nur auf, sich zu wehren.</b>", CTA]]),
("21_nichtstun", "DdPMrt0AHrc", [
 ["Gar nichts zu tun gehört zum Besten, was du für dein Nervensystem tun kannst.", "<b>Was dabei in dir passiert:</b>"],
 ["Dass du es brauchst, merkst du zuerst an deiner Gereiztheit."],
 ["Nichtstun ist die Zeit, in der keine Reize ankommen.", "Kein Bildschirm. Keine Aufgabe. Niemand, der etwas von dir will."],
 ["Dein Kopf kann in den Ruhemodus schalten.", "Er sortiert Erinnerungen und ordnet, was am Tag passiert ist."],
 ["Oft reichen schon 15 bis 20 Minuten.", "Draußen fällt es vielen noch leichter."],
 ["Du merkst es am Körper.", "Der Atem rutscht in den Bauch. Ein tiefer Seufzer kommt von allein."],
 ["Hände und Füße werden warm.", "Du gähnst oder willst dich strecken."],
 ["Kommt dabei Traurigkeit oder Wut hoch, darf das sein.", "Je schwerer dir das Stillsitzen fällt, desto mehr brauchst du es."],
 ["Ausruhen ist keine verlorene Zeit.", "<b>Es ist der Teil, an dem alles andere hängt.</b>", CTA]]),
("22_abwehr", "DdOyf3eAMq9", [
 ["Eine Gewohnheit macht Beziehungen schneller kaputt als alles andere.", "<b>Es ist Abwehr.</b>"],
 ["Abwehr heißt, sofort zu reagieren.", "Statt offen zu bleiben für das, was der andere gerade sagt."],
 ["Wer abwehrt, unterbricht und widerspricht.", "Er wischt weg, was der andere denkt und fühlt."],
 ["Es klingt so:", "Immer hast du etwas auszusetzen. Das habe ich nie gesagt. Tut mir leid, wenn du das so siehst."],
 ["Wer abwehrt, glaubt, sich zu schützen.", "In Wahrheit schafft er Abstand."],
 ["Neben jemandem, der ständig abwehrt, fühlt sich niemand sicher."],
 ["<b>So änderst du es:</b>", "Nicht unterbrechen. Langsamer atmen. Nachfragen, bis du seine Sicht verstehst."],
 ["Anerkennen, was er fühlt, auch wenn du es anders siehst.", "Und Stille aushalten. Nicht alles muss sofort gelöst werden."],
 ["Abwehr ist kein Charakterzug.", "<b>Sie ist eine Gewohnheit. Und Gewohnheiten kann man ändern.</b>", CTA]]),
]
THEMES = ["hell", "schwarz", "beige"]
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
os.makedirs("w1", exist_ok=True)
meta = []
for i, (slug, src, slides) in enumerate(K):
    assert len(slides) <= 10
    th = THEMES[i % 3]
    d = f"w1/{slug}"; os.makedirs(d, exist_ok=True)
    json.dump(slides, open(f"{d}/slides.json", "w"), ensure_ascii=False, indent=1)
    cap = caption(slides); open(f"{d}/caption.txt", "w").write(cap)
    full = json.dumps(slides, ensure_ascii=False) + cap
    for bad in ["–", "—", " - "]:
        assert bad not in full, (slug, bad)
    r = subprocess.run(["node", "build.js", f"{d}/img", f"{d}/slides.json", th], capture_output=True, text=True)
    print(slug, th, len(slides), len(cap), r.stdout.strip().replace("\n", " | "), r.stderr[:200])
    meta.append({"slug": slug, "quelle": src, "farbe": th, "slides": len(slides)})
json.dump(meta, open("w1/meta.json", "w"), ensure_ascii=False, indent=1)
