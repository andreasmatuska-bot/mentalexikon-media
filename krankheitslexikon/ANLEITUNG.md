# Krankheitslexikon: Tagesbetrieb in der Cloud

Stand 09.10.2026. Auftrag von Andreas vom 04.10.2026, umgestellt am 06.10.2026 (nur alter Stil, drei Reels am Tag) und am 09.10.2026 (ganz in der Cloud, Upload über dieses Repository, kein Mac und kein Chrome mehr nötig). Diese Datei ist die verbindliche Regel für den Lauf „Krankheitslexikon täglich planen“. Sie ersetzt für den Lauf die Notizen 05 und 06 auf dem Mac.

Instagram Seite: @krankheitslexikon. In Publer: Konto „Übersetzung deiner Krankheit“ (Account ID 6ac2850a0134954651865392) im Workspace „Instagram Pages“.

## Was gepostet wird
* Es gibt NUR NOCH den alten Stil, so wie Julia ihre Beiträge früher selbst gemacht hat (Reels vor dem 04.10.2026). Nicht aufgehübscht, nicht „hochwertiger“. Der neue Look (erzeugte Illustration, neue Farbwelt, nummerierte Punkte auf einem Körperbild, Motion Design) wird nicht mehr gebaut und nicht mehr gepostet, weil der alte Stil beim Publikum viel besser ankommt.
* Drei normale Reels pro Tag (mit Teilen im Feed, kein Test Reel, keine Story), Zeit in Zypern (Asia/Nicosia): 12:00 Uhr (das ist 11:00 Uhr deutscher Zeit), 15:30 Uhr und 19:00 Uhr.
* Jedes Reel mit Titelbild (die Grafik selbst, steht am Anfang der `_IG.mp4`) und mit Beschreibung. Die Beschreibung muss in Publer wirklich beim Post stehen.
* Bereits geplante Beiträge nie löschen oder überschreiben. Nie sofort veröffentlichen, nur für morgen einplanen.

## Themen
* Nur aus der Welt des Kanals: Körperteil, Organ, Zone oder Beschwerde plus seelische Bedeutung als Liste, am besten etwas, das man an sich selbst prüfen kann.
* Die drei Themen eines Tages unterscheiden sich deutlich. Rund einmal pro Woche ist eines eine Brücke zum Coaching Thema (Grenzen setzen, Nein sagen, Empathen), ebenfalls im alten Stil.
* Kein Thema doppelt: vor dem Bau THEMEN.md prüfen.

## Inhaltliche Regeln
* Nur seelische Bedeutung, Stress und Anspannung. Keine Zuordnung von Zeichen zu schweren Krankheiten, kein Heilversprechen, keine Diagnose, keine Krebs Hashtags. Immer ein Hinweis auf ärztliche Abklärung in der Beschreibung.
* Wird eine Lehre oder Quelle genannt (zum Beispiel Jin Shin Jyutsu, Dahlke, Tepperwein), muss die Zuordnung dort wirklich so stehen. Per Websuche gegenprüfen und die Fundstelle für den Qualitätsmanager notieren. Am einfachsten: keine Lehre und keinen Autor nennen.
* Alles auf Deutsch, du, nie Gedankenstriche, nur die Anführungszeichen „ und “.

## Stil der Originale (Maßstab)
Angesehen am 06.10.2026 im Reels Raster von @krankheitslexikon (unter anderem „Was dir deine Krankheit sagen will:“, „Was dir kein Arzt über Krankheit und Schmerzen sagt!“, „Jede Sucht beginnt mit…“, „Was bedeutet dein Schmerz?“).

Allen gemeinsam:
* Ein einziges stehendes Bild mit Musik, 4 bis 6 Sekunden. Kein Motion Design, kein Zoom. Sehr viel Text in kleiner Schrift, den man in der Zeit nicht lesen kann (deshalb läuft das Video in Schleife).
* Sieht nach Canva aus: einfache Flächen, Standardschriften, nicht alles pixelgenau ausgerichtet.
* Wasserzeichen @krankheitslexikon klein, grau oder schwarz, irgendwo mitten im Bild (oft am rechten Rand zwischen zwei Punkten oder mitten im Text), nicht in einer Fußzeile.
* Unten eine Zeile „Folge mir, um die Sprache deines Körpers zu verstehen.“ (auch „Folge mir jetzt, …“ oder „Folge mir, um zu verstehen, was deine Krankheit bedeutet.“).
* Überschrift oben, oft mit farbigem Marker oder Kasten dahinter.

Aufbauten, die gebaut werden (reine Textgrafiken):
* A „Papier“: beiges Papier mit feiner Körnung. Überschrift fett schwarz, linksbündig, auf neongrünem Marker, zwei Zeilen. Darunter sechs Punkte: Ziffer mit Punkt, direkt dahinter der Begriff fett, Doppelpunkt, darunter zwei bis drei Zeilen Text, dunkelgrau, sehr klein. Wasserzeichen rechts zwischen Punkt 3 und 4. Reihe „Was dir deine Krankheit sagen will:“. Im Skript: bau_papier (Standard).
* B „Zwei Spalten“: hellgrauer Verlauf, Überschrift rot auf rosa Kasten, mittig, darunter in Rot „(Und was die wenigsten wissen…)“. Zwei Spalten Fließtext: Begriff fett, Pfeil, Bedeutung normal, sehr dicht, 13 bis 14 Begriffe. Fußzeile rot. Im Skript: bau_spalten, im JSON „aufbau“: „spalten“. Beispiel 05 Schlaf kommt dem nahe und lief mit über 200.000 Aufrufen am besten. Noch nicht direkt gegen ein Original abgeglichen.
* C „Balken“: dunkles Foto (Kerze, Rauch) als Hintergrund, Überschrift weiß in Serifenschrift, darunter 8 bis 9 schwarze Balken mit weißem Text „Begriff, Bedeutung“, mittig, unterschiedlich breit, Fußzeile als roter Balken, Wasserzeichen unten links. Noch nicht im Skript. Erst bauen, wenn ein passendes, frei nutzbares Foto im Ordner vorlagen liegt. Keine erzeugten Bilder.
* Zwischen den Aufbauten abwechseln. Zwei Videos mit gleichem Aufbau nicht direkt hintereinander am selben Tag, wenn es sich vermeiden lässt.

Aufbauten mit Bildmaterial (Organe als Bildchen, Körperumrisse, Fußreflexzonen, dunkle Poster) werden vorerst nicht gebaut. Erzeugte Illustrationen sind tabu.

Vergleichsbilder liegen in vorlagen/ (Titelbilder 05 bis 09 im alten Stil). Julias Originale selbst sind aus der Cloud meist nicht abrufbar. Wo die Vorlagen sauberer oder aufwendiger wirken als diese Beschreibung der Originale, gilt die Beschreibung.

## Dateien in diesem Ordner
* engine/build_alt.py: baut Grafik, Titelbild, Video und `_IG.mp4`. Zeichnet mit Pillow und numpy, braucht ffmpeg, kein Chromium. Schriften in engine/fonts (League Spartan, Open Sans, Oswald). Musik: engine/musik_ruhig_warm.mp3.
  Aufruf im Ordner engine: `python3 build_alt.py inhalte/<datei>.json <ausgabeordner> musik_ruhig_warm.mp3`
* engine/inhalte/: Inhalt jedes gebauten Videos als JSON (name, titel, punkte, optional aufbau, unter, fuss, schrift, abstand). Name fortlaufend: Krankheitslexikon_15_Thema, Dateiname inhalt_15_Thema_papier.json oder _spalten.json.
* videos/JJJJ-MM-TT/ (Tag der Veröffentlichung): je Video `_IG.mp4`, `_Titelbild.jpg`, `_Beschreibung.txt`. Die große .png und die .mp4 ohne Titelbild werden nicht eingecheckt.
* vorrat/: fertig gebaute und vom Qualitätsmanager freigegebene Videos, die noch nie eingeplant wurden. Die werden zuerst verbraucht.
* vorlagen/: Vergleichsbilder und Beispiel Beschreibungen.
* THEMEN.md: Themenliste, fortlaufend ergänzen. PROTOKOLL.md: je Lauf ein kurzer Eintrag, höchstens die letzten 14 Läufe behalten.

## Technik
* Video 6 Sekunden, 1080x1920, 30 Bilder pro Sekunde, reines Standbild ohne Zoom, Musik ab Sekunde 2 der Musikdatei mit Ein und Ausblendung, etwa minus 16 LUFS, yuv420p, Profil High, Ton 128k (steht fest im Skript), unter 10 MB.
* `_IG.mp4`: Titelbild steht 0,10 s voll und blendet in 0,25 s ins Video über, Gesamtlänge bleibt 6 Sekunden. Publer nimmt kein eigenes Cover an, deshalb dieser Weg.
* Meldet das Skript „Inhalt zu lang“, Text kürzen oder im JSON schrift oder abstand kleiner setzen.

## Beschreibung (Caption)
Im Stil des Kanals, Muster siehe vorlagen/ und vorrat/:
1. „‼️ Lies hier weiter 👇🏼“
2. Ein bis zwei Sätze Einstieg
3. Die Punkte einzeln erklärt, gleicher Inhalt wie in der Grafik
4. Eine Frage an die Leser
5. Hinweis auf ärztliche Abklärung
6. Aufruf im genauen Wortlaut: „✍️ Schreibe „ja“ in die Kommentare, wenn du Zugang zu unserer kostenlosen Gesundheitsgruppe zum Austauschen haben möchtest.“ (bei einer Brücke stattdessen ein passendes Wort wie „Grenze“)
7. Genau fünf passende Hashtags

## Qualitätsmanager (Andreas ganz wichtig)
Bei jedem Lauf prüft ein unabhängiger Prüfer (eigener Agent, der den Bau nicht gesehen hat). Er bekommt nur die fertigen Dateien, THEMEN.md, die Fundstellen, die Vergleichsbilder aus vorlagen/ und diese Prüfliste. Er sieht jedes Bild selbst an und meldet zu jedem Punkt „bestanden“ oder „nicht bestanden“ mit Begründung. Ohne seine Freigabe wird nichts eingeplant.

Prüfung 1, vor dem Einplanen, je Video:
* a) Rechtschreibung, Grammatik, Umlaute und ß in Grafik, Titelbild und Beschreibung, keine Gedankenstriche
* b) Nichts abgeschnitten oder überlappend, alles lesbar, Wichtiges zwischen y 250 und 1640, Wasserzeichen @krankheitslexikon vorhanden
* c) Stil: sieht aus wie ein Beitrag von Julia aus der Zeit vor dem 04.10.2026, NICHT im neuen Look und nicht aufwendiger als die Originale, stehendes Bild
* d) Textmenge, Aufbau und Ton der Grafik entsprechen den Originalen
* e) Inhalt stimmt: in sich schlüssig, entspricht der genannten Lehre oder Quelle (selbst per Websuche nachprüfen), Grafik und Beschreibung sagen dasselbe
* f) Keine Zuordnung zu schweren Krankheiten, kein Heilversprechen, keine Diagnose, Hinweis auf ärztliche Abklärung, keine Krebs Hashtags
* g) Thema passt zur Zielgruppe, ist nicht doppelt (THEMEN.md) und die drei Themen des Tages unterscheiden sich
* h) Beschreibung vollständig: Einstieg, Punkte, Frage, Aufruf im genauen Wortlaut, genau fünf Hashtags
* i) Technik: 6 Sekunden, 1080x1920, 30 Bilder, Ton vorhanden, etwa minus 16 LUFS, unter 10 MB, erstes Bild der `_IG.mp4` ist das vollständige Titelbild

Bei Fehlern: beheben, neu bauen, denselben Prüfer noch einmal prüfen lassen, höchstens drei Runden. Was danach nicht in allen Punkten besteht, wird NICHT eingeplant, Andreas bekommt Bescheid.

Prüfung 2, nach dem Einplanen: richtiges Konto, genau drei Beiträge für morgen um 12:00, 15:30 und 19:00 Uhr Zypernzeit, jeweils die richtige Datei und die dazu passende Beschreibung, Wort für Wort gleich mit der `_Beschreibung.txt`, als Reel. Abweichungen sofort berichtigen und erneut prüfen.

## Hochladen und Einplanen
* Erst committen und in den Branch main pushen, dann prüfen, dass https://raw.githubusercontent.com/andreasmatuska-bot/mentalexikon-media/main/krankheitslexikon/videos/<Tag>/<Name>_IG.mp4 erreichbar ist (Status 200).
* Dann in Publer je Post: platform instagram, account = 6ac2850a0134954651865392, post_type reel, network_options {"details": {"type": "reel", "feed": true}}, media_url = die raw Adresse, caption exakt aus der `_Beschreibung.txt`, when "schedule", scheduled_for = morgen 12:00, 15:30 und 19:00 Uhr mit dem an diesem Tag gültigen Versatz von Asia/Nicosia (Sommerzeit +03:00, ab der Zeitumstellung am letzten Sonntag im Oktober +02:00, ab dem letzten Sonntag im März wieder +03:00).
* Bei Fehler, Zeitüberschreitung oder abgelaufener Verbindung zuerst den Bestand auflisten und nur fehlende Termine nachtragen, nie doppelt senden.
* Videos in videos/, deren Tag mehr als 14 Tage zurückliegt, löschen, damit das Repository klein bleibt.
