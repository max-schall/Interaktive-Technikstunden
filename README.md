# Interaktive Technikstunden

Interaktive HTML-Präsentationen mit Arbeitsblättern für den Technikunterricht der Klassen 7–10 – gleicher methodischer Aufbau wie die Chemie- und IT-Präsentationen, eigenes Design.

- `index.html` – Startseite: Klassenstufe → Reihe → Stunde
- `<Klasse>-<Reihe>/00_Uebersicht.html` – Übersicht der Reihe mit Hinweisen für Lehrkräfte
- `<Klasse>-<Reihe>/01_….html` – Präsentation (eigenständig, offline lauffähig)
- `<Klasse>-<Reihe>/01_….pdf` / `01_…_Lösung.pdf` – Arbeitsblatt (mit QR-Code zur Präsentation) und Lösung
- `fonts/` – Schriften (müssen neben den Reihen liegen)
- `_generator/` – Quellen und Skripte

## Reihen

| Klasse | Kapitel 1 | Kapitel 2 | Kapitel 3 |
|---|---|---|---|
| 7 | Arbeiten im Technikraum (5) | Der Werkstoff Holz (7) | Skizzen und technische Zeichnungen (5) |
| 8 | Der Werkstoff Metall (6) | Kunststoffe und Fertigungsverfahren (6) | Der elektrische Stromkreis (6) |
| 9 | Schalter, Sensoren und Schaltungen (7) | Von der Idee zum Serienprodukt (6) | Maschinen und Mobilität (7) |
| 10 | Bauen und Wohnen (6) | Energieversorgung (6) | Steuerung und Regelung (6) |

Die Abfolge ist spiralförmig angelegt: Holz → Metall/Kunststoff → Serienfertigung; Stromkreis → Elektronik → Steuerung und Regelung; Zeichnen (Kl. 7) → CAD/CAM (Kl. 9).
Jede Reihe endet mit einer Stunde „Wiederholung und Selbsttest“ (Karteikarten, Trainer, Quiz, „Ich kann …“-Liste).

## Gestaltungsprinzip „Werkstattzeichnung“

Chemie arbeitet mit weichen Karten und Klassenfarben, IT mit einer Konsolen-Optik. Technik übernimmt die Bildsprache der **technischen Zeichnung**:

- **Papier und Blaupause:** Hell ist ein ruhiger, warmer Papierton, dunkel eine Blaupause (Preußischblau mit hellen Linien) – bewusst ohne Raster im Hintergrund.
- **Schriftfeld:** Die Kopfleiste ist wie ein Schriftfeld nach DIN EN ISO 7200 aufgebaut – Zellen mit Kleinbeschriftung („Benennung“, „Stunde“, „Klasse“).
- **Positionsnummern:** Stationen erscheinen als Kreise mit Ziffer, verbunden durch eine Bezugslinie; die Nummern kehren im Hefteintrag und auf dem Arbeitsblatt wieder.
- **Maßlinien:** Unter jeder Stationsüberschrift steht eine Maßlinie mit Pfeilen und Begrenzungsstrichen.
- **Normschrift:** Beschriftungen in Barlow Semi Condensed (an DIN 1451 angelehnt), Fließtext in Atkinson Hyperlegible, Code in IBM Plex Mono.
- **Linie statt Schatten:** keine Rundungen und Schatten; dünne Konturen, gefüllte Flächen (Knöpfe, Tags) mit 45°-Fase, Karten mit Eckmarke.
- **Signalfarben:** Jede Reihe hat eine an RAL-Signalfarben angelehnte Kapitelfarbe (z. B. RAL 3020 Verkehrsrot für den Stromkreis).
- **Arbeitsblätter** tragen einen Zeichnungsrahmen und ein Schriftfeld mit Benennung, Name, Datum, Blatt und QR-Code zur Präsentation.

## Bauen

    cd _generator
    python3 build.py                              # Präsentationen, Übersichten, Startseite
    python3 build.py 8-Stromkreis                 # nur eine Reihe
    python3 test.py 8-Stromkreis                  # alle Stationen headless durchklicken, JS-Fehler melden
    cd arbeitsblaetter && python3 render.py --alle    # Arbeitsblätter und Lösungen (PDF)
    python3 scorm.py                              # SCORM-Paket mit allen Reihen → ../_scorm/

Die Inhalte einer Stunde stehen in `_generator/src/<Reihe>/NN_Name.html` (Kopfkommentar mit Metadaten, Stationen als
`<section class="station">`, Skript am Ende). Design: `_generator/base.css` (Bausteine aus IT) + `_generator/style.css`
(Technik-Gestaltung), Bausteine: `_generator/lib.js` (aus IT) + `_generator/tech.js` (Technik), Reihen: `_generator/series.py`.

### Technik-Bausteine (`tech.js`)

| Baustein | Einsatz |
|---|---|
| `circuit()` | Stromkreis-Simulator (Reihe/parallel, Schalter, Kurzschluss, durchbrennende Lampen, Messwerte) |
| `plot()` | Liniendiagramme (Kennlinien, Messreihen, Verläufe) |
| `gears()` | Zahnrad-, Riemen- und Kettengetriebe mit Animation, Zwischenrad, Übersetzung |
| `voxel()`, `voxQuiz()` | Würfelkörper in Kabinettprojektion/Isometrie mit Dreitafelbild; Ansichten-Quiz |
| `caliper()` | Messschieber mit Nonius (frei oder als Trainer) |
| `signs()`, `signSVG()` | Sicherheitszeichen (Form und Farbe nach DIN EN ISO 7010, vereinfacht) |
| `logic()` | UND/ODER/NICHT mit Schaltzeichen, Schalterschaltung und Wahrheitstabelle |
| `regel()` | Raumheizung als Steuerung und Zweipunktregelung mit Störgröße |
| `sankey()` | Energieflussbilder |
| `beam()`, `truss()` | Biegesteifigkeit von Profilen; Rahmen gegen Dreieck mit Zug/Druck |
| `transistorSim()` | Dunkel-, Hell- und Wärmeschaltung mit LDR/NTC und Poti |
| `rcSim()` | Kondensator laden/entladen, Ausschaltverzögerung |
| `costSim()`, `gridSim()`, `engine4()` | Stückkosten, Stromnetz an einem Tag, Viertaktmotor |

## Online

Die Arbeitsblätter enthalten einen QR-Code zur jeweiligen Präsentation. Die Adresse steht in
`_generator/arbeitsblaetter/render.py` (`PAGES`) und lautet derzeit
`https://max-schall.github.io/Interaktive-Technikstunden/` – passend zu den Chemie- und IT-Repositorien.
Wird ein anderer Ort gewählt, `PAGES` ändern und `render.py --alle` erneut ausführen.
