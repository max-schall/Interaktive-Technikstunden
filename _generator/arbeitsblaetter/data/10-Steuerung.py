from render import *

KREIS = ('<svg viewBox="0 0 200 90" style="width:120mm;height:54mm" font-family="Barlow Semi Condensed,sans-serif" font-size="7">'
         '<g fill="none" stroke="#111" stroke-width=".8"><rect x="60" y="8" width="45" height="18"/><rect x="130" y="8" width="55" height="18"/><rect x="130" y="62" width="55" height="18"/><rect x="60" y="62" width="45" height="18"/><circle cx="35" cy="17" r="6"/>'
         '<path d="M2 17h27M41 17h19M105 17h25M157 26v36M130 71h-25M60 71H35V23"/></g>'
         '<g fill="#111"><path d="M29 17l-4 -2v4zM60 17l-4 -2v4zM130 17l-4 -2v4zM157 62l-2 -4h4zM105 71l4 -2v4zM35 23l-2 4h4z"/>'
         '<text x="82" y="20" text-anchor="middle">A</text><text x="157" y="20" text-anchor="middle">B</text><text x="157" y="74" text-anchor="middle">C</text><text x="82" y="74" text-anchor="middle">D</text>'
         '<text x="2" y="12">E</text><text x="38" y="45">F</text><text x="190" y="45">G ↓</text></g></svg>')

WS = {
'01_Steuern_Regeln': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne den Regelkreis einer Raumheizung und beschrifte alle Teile.',
    sections=[
    ('sim', [
        A('Beschreibe, wie Steuerung und Regelung auf ein geöffnetes Fenster reagieren.', 2, 'Steuerung: Die Heizung läuft unverändert weiter, die Temperatur sinkt. Regelung: Der Sensor misst die sinkende Temperatur, der Regler schaltet die Heizung ein und gleicht die Störung (soweit möglich) aus.'),
    ]),
    ('kreis', [
        BILD('Beschrifte den Regelkreis der Raumheizung (A bis G).', KREIS, n=2, loes='A Regler · B Stellglied (Heizkörperventil) · C Regelstrecke (Raum) · D Sensor (Thermometer) · E Sollwert · F Istwert · G Störgröße (offenes Fenster)'),
    ]),
    ('sortieren', [
        SORT('Steuerung oder Regelung?', ['Toaster', 'Thermostat', 'Ampel mit festen Phasen', 'Tempomat', 'Zeitschaltuhr', 'Spülkasten mit Schwimmer'], ['Steuerung', 'Regelung'], h=14,
             loes=[['Toaster', 'Ampel', 'Zeitschaltuhr'], ['Thermostat', 'Tempomat', 'Spülkasten']]),
    ]),
    ('m1', [
        A('**M1:** Erkläre, warum der Istwert bei einem Zweipunktregler um den Sollwert pendelt.', 2, 'Der Regler kennt nur an und aus. Er schaltet erst unterhalb des Sollwerts ein und erst oberhalb wieder aus (Schaltdifferenz); dazwischen steigt bzw. sinkt die Temperatur weiter.'),
    ]),
]),

'02_Signale': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne ein analoges Signal und darunter das digitale Signal mit 2 Bit.',
    sections=[
    ('eva', [
        SORT('Ordne nach dem EVA-Prinzip.', ['Bewegungsmelder', 'Sirene', 'Mikrocontroller', 'Fensterkontakt', 'Motor', 'Ampellampe'], ['Eingabe (Sensor)', 'Verarbeitung', 'Ausgabe (Aktor)'], h=12,
             loes=[['Bewegungsmelder', 'Fensterkontakt'], ['Mikrocontroller'], ['Sirene', 'Motor', 'Ampellampe']]),
    ]),
    ('ad', [
        BOX('Zeichne ein analoges Signal (Welle) und darunter, wie ein 2-Bit-A/D-Wandler es mit 8 Abtastungen darstellt.', 34, loes='Stufenkurve mit 4 Stufen (00, 01, 10, 11), die der Welle grob folgt.'),
        TAB('Wie viele Stufen?', ['Bit', '1', '2', '4', '8', '10'], [['Stufen', '[[2]]', '[[4]]', '[[16]]', '[[256]]', '[[1024]]']], h=7),
    ]),
    ('vergleich', [
        A('Erkläre den Unterschied zwischen analogen und digitalen Signalen an einem Beispiel.', 2, 'Analog: stufenlos, z. B. Zeiger einer Uhr. Digital: feste Stufen, z. B. Digitaluhr mit Ziffern; im Computer als 0 und 1.'),
    ]),
    ('binaer', [
        GL('**M1:** Rechne um.', ['13 = [[00001101]]', '00101010 = [[42]]', '255 = [[11111111]]']),
    ]),
]),

'03_Logik': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne die Schaltzeichen von UND, ODER und NICHT mit Wahrheitstabelle.',
    sections=[
    ('und', [
        TAB('Wahrheitstabelle UND', ['A', 'B', 'Y'], [['0', '0', '[[0]]'], ['0', '1', '[[0]]'], ['1', '0', '[[0]]'], ['1', '1', '[[1]]']], h=6),
    ]),
    ('oder', [
        TAB('Wahrheitstabelle ODER', ['A', 'B', 'Y'], [['0', '0', '[[0]]'], ['0', '1', '[[1]]'], ['1', '0', '[[1]]'], ['1', '1', '[[1]]']], h=6),
    ]),
    ('nicht', [
        BOXES('Zeichne die gleichwertige Schalterschaltung.', ['UND', 'ODER', 'NICHT'], 26, loes=['zwei Schalter in Reihe', 'zwei Schalter parallel', 'Öffner (Ruhekontakt)']),
    ]),
    ('anwendung', [
        ZU('**M1:** Welche Verknüpfung passt?', ['UND', 'ODER', 'NICHT'], ['Alarm bei Tür oder Fenster', 'Nachtlicht, wenn nicht hell', 'Presse nur mit beiden Händen'], loes=[2, 3, 1]),
    ]),
]),

'04_Mikrocontroller': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne das Struktogramm für das Treppenhauslicht.',
    sections=[
    ('treppe', [
        A('Begründe, ob das Treppenhauslicht eine Steuerung oder eine Regelung ist.', 2, 'Eine Steuerung: Nach dem Tastendruck leuchtet das Licht eine feste Zeit, ohne dass etwas gemessen und zurückgemeldet wird.'),
    ]),
    ('nacht', [
        L('Das Programm fragt in einer [[Endlosschleife]] den [[Lichtsensor]] ab. Ist der Wert kleiner als der [[Schwellwert]], wird die LED [[eingeschaltet]].'),
    ]),
    ('struktogramm', [
        BOX('Zeichne ein Struktogramm: Bei über 25 °C läuft der Lüfter, sonst ist er aus.', 40, loes='wiederhole fortlaufend: setze T auf Temperatur · wenn T > 25 → ja: Lüfter an / nein: Lüfter aus · warte 1 s'),
    ]),
    ('vorhersage', [
        GL('**M1:** Was passiert?', ['Helligkeit 18, Schwellwert 30 → LED [[an]]', 'wiederhole 4-mal: LED an, warte 500 ms, LED aus, warte 500 ms → Dauer [[4]] s']),
    ]),
]),

'05_Assistenzsysteme': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne den Regelkreis des Abstandsregeltempomaten.',
    sections=[
    ('systeme', [
        TAB('Ergänze Sensor und Aktor.', ['Assistenzsystem', 'Sensor', 'Aktor'], [['Einparkhilfe', '[[Ultraschall]]', '[[Lautsprecher]]'], ['Notbremsassistent', '[[Radar, Kamera]]', '[[Bremse]]'], ['Spurhalteassistent', '[[Kamera]]', '[[Lenkung]]']], h=6),
    ]),
    ('acc', [
        TAB('Abstandsregeltempomat als Regelkreis', ['Begriff', 'beim Abstandsregeltempomat'], [['Istwert', '[[gemessener Abstand]]'], ['Sollwert', '[[Sicherheitsabstand]]'], ['Stellglied', '[[Gas und Bremse]]'], ['Störgröße', '[[vorausfahrendes Auto]]']], h=6, widths=[30, 70]),
    ]),
    ('stufen', [
        A('Beschreibe den Unterschied zwischen Stufe 2 und Stufe 5 des automatisierten Fahrens.', 2, 'Stufe 2: Das Auto lenkt und bremst teilweise selbst, der Mensch muss ständig überwachen. Stufe 5: Das Auto fährt überall ohne Mensch, braucht kein Lenkrad.'),
    ]),
    ('ethik', [
        A('**M1:** Nenne je zwei Chancen und Risiken autonomer Fahrzeuge.', 3, 'Chancen: weniger Unfälle, mobil ohne Führerschein, weniger Staus · Risiken: Haftungsfragen, Datenschutz, Hackerangriffe, Sensorversagen bei schlechtem Wetter'),
    ]),
]),

'06_Wiederholung': dict(ichkann=True, skip=['quiz-st'], heft_label='Notizen', heft_title='Das muss ich noch üben', heft_sub='Fragen, Merkpunkte, Begriffe',
    sections=[
    ('begriffe', [
        ZU('Ordne die Fachbegriffe zu.', ['Regelung', 'Istwert', 'Aktor', 'A/D-Wandler', 'ODER'],
           ['mindestens ein Eingang 1', 'gemessener Wert', 'mit Rückmeldung', 'analog → Zahl', 'setzt Befehle um'], loes=[3, 2, 5, 4, 1]),
    ]),
    ('t1', [
        SORT('Sortiere.', ['Toaster', 'Thermostat', 'Tempomat', 'Zeitschaltuhr'], ['Steuerung', 'Regelung'], h=12, loes=[['Toaster', 'Zeitschaltuhr'], ['Thermostat', 'Tempomat']]),
    ]),
    ('t2', [
        GL('Logik.', ['UND: A = 1, B = 0 → Y = [[0]]', 'ODER: A = 0, B = 1 → Y = [[1]]', 'NICHT: A = 1 → Y = [[0]]']),
    ]),
    ('t3', [
        GL('Bits.', ['6 Bit → [[64]] Stufen', '00010001 = [[17]]']),
    ]),
]),
}
