# Karussell Engine (Mentalexikon)

Stand 05.10.2026 (abends). Vorgaben von Andreas: Die erfolgreichsten Karussells der Instagram Seiten Mentalogie und erfolgsart für Mentalexikon nachbauen. Die Karussells sind der einzige Inhalt im Feed der Seite: VIER Karussells pro Tag um 9:00, 12:00, 16:00 und 19:00 Uhr Zypern (Asia/Nicosia). Mindset Videos erscheinen nicht mehr als normale Beiträge (Umstellung von Andreas am 05.10.2026 abends, vorher zwei Karussells und ein Reel um 12:00). Die fertigen Videos laufen nur noch als Test Reels und gehören nicht zu dieser Engine. Noch keine Beiträge mit Kommentar Aufruf (Engagement oder Pitch), nur normale Karussells. Ohne Musik. Vollautomatisch, ohne Rückfragen.

## Abwechslung (Pflicht, von Andreas am 05.10.2026 verlangt)
Die vier Beiträge eines Tages dürfen nicht gleich aussehen und nicht gleich klingen.
* Farbe: reihum hell, schwarz, beige über alle Termine in zeitlicher Reihenfolge. Zwei aufeinanderfolgende Termine haben nie dieselbe Farbe, auch nicht über Nacht.
* Art des Beitrags: an einem Tag höchstens ein Karussell derselben Art. Arten: Liste mit Zahl (9 Dinge, 10 Wahrheiten), Sätze zum Nachsprechen, Erklärstück (warum etwas so ist), Geschichte oder Szene (eine Person, ein Moment), Gegenüberstellung (so klingt es, so wäre es richtig).
* Erster Satz: nicht zwei Hooks am selben Tag mit demselben Bau. Nicht immer "X ist nicht Y. Es ist Z." und nicht immer eine Zahl. Auch die fette Pointe am Ende soll nicht jedes Mal nach dem Muster "Es ist kein A. Es ist B." gebaut sein. Höchstens ein Karussell pro Tag mit dieser Verneinungsfigur.
* Thema: an einem Tag vier verschiedene Themenfelder (zum Beispiel Partnerschaft, Familie und Kindheit, Umgang mit schwierigen Menschen, Ruhe und Nervensystem, Selbstwert, Freundschaft, Kommunikation). Ähnliche Themen mindestens zwei Tage auseinander.
* Länge und Satzbild: kurze Listen und längere Erklärstücke mischen, nicht viermal 9 Slides mit demselben Rhythmus.
* Der Lektor prüft das ausdrücklich: Er bekommt alle Texte der Woche in zeitlicher Reihenfolge und meldet Tage, an denen zwei Beiträge gleich klingen. Solche Texte werden umgeschrieben oder auf einen anderen Tag getauscht.

## Vorlagen (Stand 05.10.2026, von Andreas so festgelegt)
Es gibt zwei Vorbildseiten: Mentalogie (instagram.com/mentalogie) und erfolgsart (instagram.com/erfolgsart). Andreas will, dass immer nur die wirklich erfolgreichsten Beiträge nachgebaut werden, egal von welcher Seite.

`vorlagen_pool.json` ist die gemeinsame Bestenliste beider Seiten (erfolgsart: letzte 2000 Beiträge, Mentalogie: letzte 600). Je Vorlage: quelle (Instagram Kurzcode), seite, url, datum, likes, kommentare, faktor (Likes im Verhältnis zum üblichen Wert der Seite in dieser Zeit), stufe, hinweise, verwendet, caption.
* Stufe A: Ausreißer (ab 10.000 Likes oder mindestens das Dreifache des Üblichen). Stufe B: klar überdurchschnittlich. Stufe C: Durchschnitt.
* Auswahl: immer zuerst freie Vorlagen der Stufe A nach Likes absteigend, erst wenn die aufgebraucht sind Stufe B. Stufe C nie verwenden, dann lieber eigene Themen nach AUSWERTUNG.md.
* Nicht verwenden: verwendet true, Hinweis "werbung". Hinweis "krankheit_pruefen": Caption lesen, bei Krankheiten und Diagnosen überspringen. Hinweis "tiere" (Hunde, Katzen): passt nicht zur Seite, überspringen.
* "likes_geschaetzt" true heißt verborgene Likes, nur über Kommentare geschätzt. Solche Vorlagen kommen nie in Stufe A.
* Bei Mentalogie enthält die Caption den vollständigen Text der Slides. Bei erfolgsart ist die Caption nur die Zusammenfassung des Themas, oft eine kleine Geschichte mit Fotos. Dann Thema, Kernaussage und Hook übernehmen und daraus ein eigenes Text Karussell in unserem Design schreiben.
* Auffrischen: `python3 pool_bauen.py erfolgsart=<datei.json> mentalogie=<datei.json>` mit frisch gescrapten Daten (Felder shortCode, type, likesCount, commentsCount, timestamp, url, paidPartnership, caption). Der Pool wächst nur, verwendet wird aus verwendet.json gesetzt. Das Skript gibt aus, wie viele Vorlagen je Stufe noch frei sind.
* Nach dem Einplanen verwendet.json ergänzen und pool_bauen.py ohne Argumente laufen lassen, damit verwendet im Pool stimmt.

## Regeln für Text
* Inhalt sinngemäß wie die Vorlage, aber neu formuliert in natürlichem Deutsch. Nichts wörtlich abschreiben.
* Nie Gedankenstriche. Ansprache du. Kurze Sätze.
* Keine erfundenen Studien, Zahlen oder Heilversprechen. Aussagen über Körper und Psyche vorsichtig formulieren (kann, oft, viele).
* Keine Werbung, keine Themen wie KI Geld verdienen (das sind bei den Vorbildseiten Werbebeiträge, überspringen). Keine Beiträge über Krankheiten und Diagnosen.
* Slide 1: Hook, letzte Zeile fett mit Doppelpunkt. Dann ein Gedanke pro Slide. Letzte Slide: Pointe fett, dann "Mehr davon:<br><b>Folge @mentalexikon.</b>". Höchstens 10 Slides.
* Angekündigte Zahl muss zur Anzahl der Punkte passen.
* Auf den Slides steht nur @mentalexikon. Nie "AMATUSKA LLC".
* Caption wie bei Mentalogie: der Slide Text als Fließtext in Absätzen, Listen nummeriert, letzte Zeile "Mehr davon: folge @mentalexikon." Keine Hashtags, keine Emojis. Die Funktion caption() in woche_beispiel.py baut das automatisch.

## Design
1080 x 1440 JPG, Schrift Sofia Sans Condensed (500, fett 800), 82 px, linksbündig, vertikal mittig. Fußzeile: Seitenzahl, @mentalexikon, Pfeil. Farben wechseln reihum: hell, schwarz, beige (siehe Abwechslung).

## Bauen
`npm install` in diesem Ordner, dann `node build.js <Ausgabeordner> <slides.json> <beige|hell|schwarz>`. Chromium liegt unter /opt/pw-browsers/chromium. Meldet "UEBERLAUF Slide N", wenn Text nicht passt (dann kürzen). `woche_beispiel.py` ist die komplette erste Woche als Vorlage: Liste K mit (Ordnername, Quelle, Slides), erzeugt pro Karussell slides.json, caption.txt und die Bilder.

## Prüfen (Pflicht)
1. Kein UEBERLAUF, keine Gedankenstriche.
2. Kontaktbogen aller Slides ansehen.
3. Ein unabhängiger Agent liest alle Texte gegen (Rechtschreibung, natürliches Deutsch, Bezüge, Zahlen, unbelegte Behauptungen, Caption). Pflichtkorrekturen einarbeiten und neu rendern.

## Einplanen
Bilder nach `karussells/NN_thema/01.jpg ...` in dieses Repository (Branch main) pushen. Publer Workspace "Mindset Seite", Konto Mentalexikon (Account ID 6abf689a4c27d7dbc3ad0f5a), platform instagram, post_type photo, media_urls in Reihenfolge (raw.githubusercontent.com/andreasmatuska-bot/mentalexikon-media/main/karussells/...), when schedule, Zeit als ISO mit dem gültigen Versatz von Asia/Nicosia. Höchstens 3 Posts pro Aufruf (confirm_multiple true) und zwischen den Aufrufen kurz warten, sonst meldet Publer "Rate limit". Nach einem Fehler oder Abbruch zuerst die eingeplanten Posts auflisten und nur fehlende Termine nachtragen, nie doppelt senden.

## Buchführung
`verwendet.json`: jede genutzte Vorlage (Instagram Kurzcode) mit Nummer, Ordner, Farbe, Termin. Keine Vorlage und kein Thema zweimal.
`AUSWERTUNG.md`: was bisher gut und schlecht lief, wird bei jedem Lauf fortgeschrieben und bestimmt die Themenwahl.
