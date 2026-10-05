# Karussell Engine (Mentalexikon)

Stand 05.10.2026. Vorgaben von Andreas: Die erfolgreichsten Karussells der Instagram Seite Mentalogie für Mentalexikon nachbauen. Zwei Karussells pro Tag, 12:30 und 19:00 Uhr Zypern (Asia/Nicosia), zusätzlich zu einem Reel pro Tag um 9:00 (Umstellung von Andreas am 05.10.2026, vorher drei Karussells und drei Reels). Ohne Musik. Vollautomatisch, ohne Rückfragen.

## Regeln für Text
* Inhalt sinngemäß wie die Vorlage, aber neu formuliert in natürlichem Deutsch. Nichts wörtlich abschreiben.
* Nie Gedankenstriche. Ansprache du. Kurze Sätze.
* Keine erfundenen Studien, Zahlen oder Heilversprechen. Aussagen über Körper und Psyche vorsichtig formulieren (kann, oft, viele).
* Keine Werbung, keine Themen wie KI Geld verdienen (das sind bei Mentalogie Werbebeiträge, überspringen). Keine Beiträge über Krankheiten und Diagnosen.
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
