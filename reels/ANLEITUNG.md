# Reels für Mindsetologie und Mentalexikon (8 pro Tag und Seite)

Stand 09.10.2026. Von Andreas so festgelegt, ersetzt alle früheren Pläne für beide Seiten (Karussells über Publer, Test Reels, Listen Videos um 10:30, 17:30, 20:30).

## Was gepostet wird
* Nur noch die kurzen Listen Reels im Stil der Listen Videos von Mindsetologie (cremefarbener Hintergrund, goldener Kasten, Liste, Standbild, 6 Sekunden). Das kommt nach Andreas extrem gut an. Am Aussehen nichts ändern.
* Musik: ruhig und entspannt (karussells/_engine/musik/ruhig_*.wav, erzeugt von musik_ruhig_bauen.py: langsames, weiches E Piano mit warmer Fläche, kein Schlagzeug, kein Klatschen, keine Glocken). Die alte fröhliche Musik (froehlich_*.wav) fand Andreas sehr nervig. Sie wird nie mehr verwendet.
* 8 Reels pro Tag auf jeder der beiden Seiten, um 08:00, 10:00, 12:00, 14:00, 16:00, 18:00, 20:00 und 22:00 Uhr Zeit in Zypern (Asia/Nicosia). Andreas hat 8 pro Tag und die Zeiten 10 bis 18 Uhr im Zweistundentakt genannt, 08:00, 20:00 und 22:00 ergänzen das auf 8.
* Normale Reels, keine Test Reels. Karussells werden NICHT über Publer gepostet (die postet das Team von Hand mit Musik).
* Prinzip: die erfolgreichsten Listen immer wieder posten und jedes Mal nur ein paar Wörter ändern. Jede Liste läuft pro Woche zweimal je Seite, jeweils mit anderer Überschrift, Frage, Caption, Reihenfolge der Punkte und Musik.

## Dateien
* pool.json: alle Listen. Felder: id, slug, feld (Themenfeld), herkunft, quelle (Shortcode der Vorlage), aufrufe_vorlage, typ (nummern, liste, story, tabelle, gruppen), fest (true = Reihenfolge der Punkte nie ändern), kopf (3 Überschriften), punkte, schluss (optional), frage (2), caption (2, ohne Frage und ohne Folg Zeile), pause (optional true = nicht mehr einplanen).
* woche_planen.py <Starttag> [Tage] [--ab HH:MM]: verteilt die Listen auf die Termine beider Seiten und schreibt plan/<Starttag>.json. Regeln stecken im Skript (gleiche Liste frühestens nach 2 Tagen wieder, pro Tag kein Themenfeld doppelt, beide Seiten nie gleichzeitig dieselbe Liste).
* reel_bauen.js <plan.json>: baut je Eintrag <seite>/<Tag>/<HHMM>_<slug>.mp4 und .jpg. Meldet UEBERLAUF, wenn ein Text nicht passt (dann den Text in pool.json kürzen). Alle sollen "schrift 21" melden.
* auswertung/: Scrapes beider Seiten und AUSWERTUNG.md (was am besten lief).
* Vor dem Bauen: in karussells/_engine `npm install`, Schrift Liberation Sans muss vorhanden sein (fc-list).

## Textregeln
Deutsch, du, nie Gedankenstriche, nur die Anführungszeichen „ und “. Zahl in der Überschrift = Anzahl der Punkte. Jeder Punkt beginnt mit einem fetten Teil. Keine Überschrift oder Caption darf auf eine bestimmte Position verweisen (Punkte werden gemischt), außer bei fest = true. Nichts mit falschen oder nicht prüfbaren Aussagen über Gesundheit, Medizin, Recht, Geld und Gehälter, keine Klischees, kein Sex, keine Drogen, keine erfundenen Zitate echter Personen. Gesundheit und Sicherheit nur vorsichtig (kann, oft, meist). Nirgends AMATUSKA. Kein Aufruf, ein bestimmtes Wort zu kommentieren. Caption: zwei bis vier Sätze, keine Hashtags, keine Emojis. Die Zeile "<Frage> Folg @seite für mehr davon." hängt das Skript selbst an.

## Einplanen in Publer
Workspace "Instagram Pages". Mindsetologie Account ID 6ac4a50abf25b54bdef0ea2d, Mentalexikon Account ID 6abf689a4c27d7dbc3ad0f5a.
Erst pushen (Branch main), dann je Eintrag: platform instagram, post_type reel, media_url https://raw.githubusercontent.com/andreasmatuska-bot/mentalexikon-media/main/reels/<datei>.mp4, caption exakt aus dem Plan, when schedule, scheduled_for = termin mit dem dann gültigen Versatz von Asia/Nicosia (Sommerzeit +03:00, ab der Zeitumstellung Ende Oktober +02:00). Mehrere Posts eines Kontos pro Aufruf sind möglich (confirm_multiple true), ein Aufruf nur für ein Konto. Nach Fehlern erst den Bestand auflisten, nie doppelt senden. Jeder Post braucht seine Caption, danach in Publer kontrollieren.

## Jede Woche
Der Wochenlauf plant immer die nächsten 7 Tage ab dem Tag nach dem letzten schon geplanten Tag. Dabei: neue Auswertung (welche Listen liefen auf den Seiten am besten), die schwächsten Listen auf pause setzen, 4 bis 8 neue Listen aus den erfolgreichsten Vorlagen in den Pool schreiben (mit 3 Überschriften, 2 Fragen, 2 Captions), bei den bleibenden Listen ein paar Wörter ändern, Lektor lesen lassen, bauen, pushen, einplanen. Reels, deren Termin vorbei ist, können aus dem Repository gelöscht werden (älter als 14 Tage), damit es nicht zu groß wird.
