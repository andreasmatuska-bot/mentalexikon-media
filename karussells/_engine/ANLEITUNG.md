# Karussell Engine (Mentalexikon)

Stand 05.10.2026. Vorgaben von Andreas: Die erfolgreichsten Karussells der Instagram Seiten Mentalogie und erfolgsart für Mentalexikon nachbauen. Tagesablauf: 9:00 Karussell, 12:00 Mindset Reel, 19:00 Karussell. Also zwei Karussells pro Tag, 9:00 und 19:00 Uhr Zypern (Asia/Nicosia), zusätzlich zu einem Reel pro Tag um 12:00 (Umstellung von Andreas am 05.10.2026, vorher drei Karussells und drei Reels). Ohne Musik. Vollautomatisch, ohne Rückfragen.

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
1080 x 1440 JPG, Schrift Sofia Sans Condensed (500, fett 800), 82 px, linksbündig, vertikal mittig. Fußzeile: Seitenzahl, @mentalexikon, Pfeil. Farben wechseln reihum: hell, schwarz, beige.

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
