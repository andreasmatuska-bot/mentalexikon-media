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

# Listen Videos (eigene Reels von Mindsetologie)

Stand 06.10.2026. Vorgabe von Andreas: zusätzlich zu Karussells und Test Reels drei kurze Listen Videos pro Tag, so wie die bisherigen Reels der Seite. Vorlage sind die erfolgreichsten eigenen Videos von Mindsetologie (letzte 200 Beiträge), in etwa umgeschrieben. Sie erscheinen immer eine Stunde nach einem Karussell: 10:30, 17:30 und 20:30 Uhr Zypern. Normale Reels, keine Test Reels.

## Format (Stand 06.10.2026 abends, von Andreas so verlangt)
Die Videos müssen exakt so aussehen wie die bisherigen Reels der Seite (Stand Mai und Juni 2026) und das Titelbild auch. Nachgemessen an den Originalen:
* Standbild, 6 Sekunden (Andreas am 07.10.2026: 6 statt gut 4 Sekunden), keine Bewegung, kein eigener Hook am Anfang. Das Titelbild ist dasselbe Bild.
* Hintergrund creme #F4F1EA, Schrift Liberation Sans, Text fast schwarz #1E2021.
* Oben ein goldener Kasten #C8B163 über die ganze Textbreite mit der Überschrift in fetten Großbuchstaben (32 px bei 720 px Breite, Zeilenabstand 1,1).
* Darunter eine dünne Linie, dann die Liste: goldene Punkte oder goldene Nummern, der Anfang jedes Punkts fett, der Rest normal (21 px, Zeilenabstand 1,5). Darunter wieder eine dünne Linie.
* Unten mittig fett die Frage mit dem Zeigefinger Emoji, kein "Folg uns" im Bild.
* Unten rechts hell das Wasserzeichen MINDSETOLOGIE.
* Der ganze Block steht senkrecht in der Mitte. Seitenrand 74 px.
Das alles steckt in `listen_video.js`. Am Aussehen nichts ändern. Passt ein Text nicht, wird der Text gekürzt (die Schrift wird nur im Notfall kleiner).

## Musik
Jedes Video bekommt eine eigene kurze, fröhliche Musik fest eingebaut (Ukulele, Glockenspiel, Klatschen), weil Publer keine Instagram Musik setzen kann. Die Stücke liegen in `karussells/_engine/musik/` und werden von `musik_bauen.py` selbst erzeugt, es ist keine fremde Musik. `listen_video.js` wechselt die Stücke reihum.

## Vorlagen
`mindsetologie_videos/_vorlagen/scrape_JJJJ-MM-TT.json`: die letzten 200 Beiträge, sortiert nach Aufrufen, mit Caption. Der Text im Video steht NICHT in der Caption, die Caption beschreibt aber das Thema. Den Text im Bild kann man nur über den Browser auf dem Mac ansehen (Video Adresse öffnen, Standbild bei 2,5 Sekunden). Ist das nicht möglich, wird das Thema aus der Caption genommen und die Liste im gleichen Stil neu geschrieben.
`mindsetologie_videos/verwendet.json`: schon gebaute Vorlagen (verwendet) und bewusst ausgelassene (uebersprungen, mit Grund). Immer die Vorlage mit den meisten Aufrufen zuerst, die in keiner der beiden Listen steht.

## Was nicht gebaut wird
Falsche oder nicht prüfbare Aussagen über Gesundheit, Medizin, Recht, Geld und Gehälter, Ranglisten mit unsicheren Fakten, Klischees über Frauen oder Männer, Inhalte mit Sex oder Drogen, erfundene Zitate echter Personen, Doppelungen. Solche Vorlagen kommen mit Grund in uebersprungen. Gesundheitstipps nur vorsichtig (kann, oft).

## Text
Wie die Vorlage, aber in etwa umgeschrieben: gleiche Idee, gleicher Aufbau, eigene Formulierungen. Nie Gedankenstriche, du, kurze Zeilen, nur die Anführungszeichen „ und “. Angekündigte Zahl stimmt mit der Anzahl der Punkte. Höchstens 13 kurze oder 10 längere Punkte. Jeder Punkt beginnt mit einem fetten Teil (<b>). Kein Aufruf, ein Wort zu kommentieren. Caption: zwei bis vier Sätze zum Thema, Leerzeile, die Frage, dann "Folg @mindsetologie für mehr davon." Keine Hashtags, keine Emojis.

## Bauen
Plan Datei `mindsetologie_videos/plan_JJJJ-MM-TT.json` nach dem Muster plan_2026-10-06.json (Felder nr, slug, quelle, aufrufe_vorlage, termin, typ, kopf, punkte, schluss, frage, cta, caption; typ ist nummern, liste, story, tabelle oder gruppen). In karussells/_engine: `npm install`, dann `node listen_video.js ../../mindsetologie_videos/<plan>.json ../../mindsetologie_videos/v3 [slug ...]`. Meldet UEBERLAUF, wenn der Text nicht passt (dann kürzen). Standbilder `v3/<slug>.jpg` ansehen, unabhängigen Lektor lesen lassen.

## Einplanen
Pushen, dann Publer: platform instagram, post_type reel, media_url `https://raw.githubusercontent.com/andreasmatuska-bot/mentalexikon-media/main/mindsetologie_videos/v3/<slug>.mp4`, when schedule, account 6ac4a50abf25b54bdef0ea2d. Ein Post pro Aufruf, 20 Sekunden Pause. Danach verwendet.json ergänzen und pushen.
