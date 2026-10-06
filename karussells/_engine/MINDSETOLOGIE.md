# Mindsetologie (Spiegelseite von Mentalexikon)

Stand 06.10.2026. Vorgabe von Andreas: Die Seite Mindsetologie bekommt genau dieselben Beiträge wie Mentalexikon, nur leicht umgeschrieben. Stil, Design, Art des Postens und Ablauf sind gleich, alle Uhrzeiten liegen eine halbe Stunde später.

## Plan
* Karussells: vier pro Tag um 9:30, 12:30, 16:30 und 19:30 Uhr Zypern (Asia/Nicosia). Ohne Musik, kein Kommentar Aufruf.
* Videos: dieselben fertigen Mindset Videos wie bei Mentalexikon, nur als Test Reels, um 14:30 und 21:30 Uhr (Mindset_47 bis Mindset_66 vom 06.10. bis 15.10.2026). Caption wie bei Mentalexikon, aber mit @mindsetologie. Es werden keine neuen Videos gebaut.
* Publer: Workspace "Instagram Pages", Konto Mindsetologie, Account ID 6ac4a50abf25b54bdef0ea2d.

## Woher die Karussells kommen
Jedes Karussell von Mentalexikon (Texte in woche_beispiel.py und den Dateien woche_JJJJ-MM-TT.py, Liste K; Buchführung in verwendet.json) wird genau einmal für Mindsetologie übernommen. Es werden keine eigenen Vorlagen gewählt. Welche schon übernommen sind, steht in `mindsetologie_verwendet.json` (gleicher Ordnername wie bei Mentalexikon).

Reihenfolge: nach dem Termin bei Mentalexikon, das älteste zuerst. Wenn möglich am selben Tag wie bei Mentalexikon und eine halbe Stunde später, sonst auf dem nächsten freien Termin.

## Umschreiben
* Gleiche Aussage, gleicher Aufbau, gleiche Anzahl Slides und Absätze, gleiche Zahl der Punkte. Jeden Absatz spürbar anders formulieren, aber nicht länger als das Original (höchstens plus 10 Zeichen).
* Hook auf Slide 1 genauso stark, Fettungen an den gleichen Stellen.
* Alle Textregeln aus ANLEITUNG.md gelten (nie Gedankenstriche, du, kurze Sätze, nichts erfinden, vorsichtige Aussagen über Körper und Psyche).
* Letzter Absatz: `Mehr davon:<br><b>Folge @mindsetologie.</b>`. Nirgends @mentalexikon, nirgends AMATUSKA.
* Farbe: reihum hell, schwarz, beige in zeitlicher Reihenfolge der Mindsetologie Termine, nie zweimal dieselbe hintereinander, möglichst nicht dieselbe Farbe wie der Zwilling bei Mentalexikon.
* Die Abwechslung pro Tag (Themenfeld, Art, Bau des ersten Satzes) gilt wie in ANLEITUNG.md.

## Bauen
Plan Datei als JSON anlegen (Liste von {nr, slug, farbe, termin, art, mentalexikon_termin, slides}, Muster: mindsetologie_start.json), dann `python3 mindsetologie_bauen.py <plan.json> [slug ...]`. Das setzt den Handle @mindsetologie, schreibt Bilder, slides.json und caption.txt nach `mindsetologie/<slug>/` im Repository und meldet UEBERLAUF.

## Prüfen
Wie in ANLEITUNG.md: kein UEBERLAUF, keine Gedankenstriche, Kontaktbögen ansehen, unabhängiger Lektor liest die neuen Texte gegen das Original (Rechtschreibung, natürliches Deutsch, Bezüge, Sinn, Zahlen, Caption). Korrekturen einarbeiten, neu rendern.

## Einplanen
Bilder pushen (Branch main), Adresse `https://raw.githubusercontent.com/andreasmatuska-bot/mentalexikon-media/main/mindsetologie/<slug>/01.jpg ...`. Publer: platform instagram, post_type photo, media_urls in Reihenfolge, when schedule, account 6ac4a50abf25b54bdef0ea2d. Höchstens 3 Posts pro Aufruf, dazwischen 20 Sekunden warten. Nach Fehlern erst den Bestand auflisten, nie doppelt senden. Danach mindsetologie_verwendet.json ergänzen und pushen.

Test Reels: post_type reel, media_url der Videodatei aus `videos/`, network_options {"details": {"type": "reel", "trial_reel": "MANUAL", "feed": false}}.
