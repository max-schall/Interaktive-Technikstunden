from render import *

A_ = [[x, y, z] for x in range(4) for y in range(2) for z in range(2)]

WS = {
'01_CAD_CAM': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Skizziere, wie du deinen Schlüsselanhänger aus Grundkörpern zusammensetzt.',
    sections=[
    ('boolesch', [
        TAB('Welche Operation ist gemeint?', ['Ziel', 'Operation'], [['Loch in eine Platte', '[[abziehen]]'], ['Griff auf einen Deckel setzen', '[[vereinigen]]'], ['nur die Überlappung zweier Körper', '[[schneiden]]']], h=6, widths=[60, 40]),
        VOX('Dieser Quader ist der Grundkörper. Skizziere, wie er nach dem Abziehen eines 2 × 2 × 1 großen Quaders oben rechts aussieht.', A_, h=34, proj='iso', loes='Quader 4 × 2 × 2, rechts oben fehlt eine Stufe von 2 Würfeln Breite und 1 Würfel Höhe (L-Form von vorn).'),
    ]),
    ('ablauf', [
        GL('Ergänze den Ablauf.', ['Skizze → [[CAD-Modell]] → Export als [[STL]] oder SVG → [[CAM]]-Software / Slicer → Maschine']),
    ]),
    ('vorteile', [
        A('Nenne zwei Vorteile und eine Grenze des Konstruierens mit CAD.', 2, 'Vorteile: schnelle Änderungen, genaue Maße, 3D-Ansicht, Zeichnungen automatisch, Daten direkt an Maschinen · Grenze: Computer und Software nötig, Einarbeitung, Eingabefehler werden genau gefertigt.'),
    ]),
    ('m1', [
        BOX('**M1:** Skizziere deinen Schlüsselanhänger mit allen Maßen.', 36, loes='Platte max. 50 × 30 × 4 mm, Loch Ø 5 mm mit mind. 3 mm Randabstand, Initialen, Ecken R3.'),
    ]),
]),

'02_Laser_3D': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Notiere die Sicherheitsregeln am Lasercutter als Checkliste.',
    sections=[
    ('laser', [
        SORT('Sortiere die Werkstoffe.', ['Sperrholz', 'PVC', 'MDF', 'Acrylglas', 'Aluminium', 'Pappe', 'Polycarbonat'], ['für den Laser geeignet', 'verboten / ungeeignet'], h=16,
             loes=[['Sperrholz', 'MDF', 'Acrylglas', 'Pappe'], ['PVC', 'Aluminium', 'Polycarbonat']]),
        A('Erkläre den Unterschied zwischen Schneiden und Gravieren.', 2, 'Schneiden: Der Laser fährt Linien (Vektoren) mit hoher Leistung ab und trennt das Material. Gravieren: Der Laser fährt Zeile für Zeile (Raster) mit geringer Leistung und trägt nur die Oberfläche ab.'),
    ]),
    ('druck', [
        TAB('Wie wirken sich die Einstellungen aus?', ['Einstellung', 'Qualität', 'Druckzeit'], [['kleinere Schichthöhe', '[[feiner]]', '[[länger]]'], ['mehr Infill', '[[stabiler]]', '[[länger]]'], ['Stützstrukturen', '[[Überhänge möglich]]', '[[länger]]']], h=6),
    ]),
    ('ablauf', [
        A('Beschreibe die Schritte von der STL-Datei bis zum fertigen 3D-Druck.', 2, 'STL im Slicer öffnen · Teil flach platzieren · Schichthöhe, Infill, Stützen einstellen · G-Code erzeugen · Druck starten und erste Schicht beobachten · Teil abnehmen und Stützen entfernen'),
    ]),
    ('vergleich', [
        SORT('**M1:** Lasercutter oder 3D-Drucker?', ['Namensschild gravieren', 'Ersatz-Zahnrad', 'Box aus MDF', 'Handyhülle', '30 Pappschablonen'], ['Lasercutter', '3D-Drucker'], h=12,
             loes=[['Namensschild', 'Box aus MDF', 'Pappschablonen'], ['Ersatz-Zahnrad', 'Handyhülle']]),
    ]),
]),

'03_Serienfertigung': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und zeichne das Kostendiagramm für Einzel- und Serienfertigung.',
    sections=[
    ('arten', [
        SORT('Sortiere.', ['Brücke', 'Schrauben', 'Fahrrad-Modell', 'Maßanzug', 'Getränkedosen', 'Küchenschrank'], ['Einzelfertigung', 'Serienfertigung', 'Massenfertigung'], h=12,
             loes=[['Brücke', 'Maßanzug'], ['Fahrrad-Modell', 'Küchenschrank'], ['Schrauben', 'Getränkedosen']]),
    ]),
    ('kosten', [
        TAB('Kosten: Einzelfertigung 6 € je Stück; Serie 60 € Vorrichtung + 2 € je Stück.', ['Stückzahl', '5', '15', '30'], [['Einzel gesamt', '[[30 €]]', '[[90 €]]', '[[180 €]]'], ['Serie gesamt', '[[70 €]]', '[[90 €]]', '[[120 €]]']], h=7),
        A('Ab welcher Stückzahl lohnt sich die Serienfertigung? Begründe.', 1, 'Ab 15 Stück sind beide gleich teuer, darüber ist die Serie günstiger, weil sich die 60 € Vorrichtung auf viele Stücke verteilen.'),
    ]),
    ('vorrichtung', [
        ZU('Ordne zu.', ['Vorrichtung', 'Schablone', 'Lehre'], ['prüft ein Maß', 'hält das Werkstück in gleicher Lage', 'gibt eine Form zum Anzeichnen vor'], loes=[2, 3, 1]),
    ]),
    ('fliessband', [
        A('**M1:** Nenne einen Vorteil und einen Nachteil der Arbeitsteilung am Fließband.', 1, 'Vorteil: schneller, jede Person wird geübt · Nachteil: eintönig, Stau an langsamen Stationen'),
    ]),
]),

'04_Nachhaltigkeit': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und zeichne den Produktlebenszyklus als Kreislauf.',
    sections=[
    ('zyklus', [
        GL('Ergänze den Lebenszyklus.', ['[[Rohstoffgewinnung]] → Herstellung → [[Transport]] → [[Nutzung]] → Entsorgung oder [[Recycling]]']),
    ]),
    ('rohstoffe', [
        ZU('Ordne Rohstoff und Verwendung im Handy zu.', ['Kupfer', 'Gold', 'Kobalt', 'Silizium'], ['Prozessor-Chip', 'Akku', 'Leiterbahnen', 'Kontakte'], loes=[3, 4, 2, 1]),
        A('Begründe, warum Rohstoffe wie Kobalt problematisch sein können.', 2, 'Sie werden teils unter gefährlichen Bedingungen, auch mit Kinderarbeit, abgebaut; der Abbau schadet Umwelt und Wasser; die Vorräte sind begrenzt.'),
    ]),
    ('handy', [
        A('Nenne drei Möglichkeiten für ein altes Handy, geordnet von gut nach schlecht.', 2, 'Weiter nutzen/reparieren · verkaufen oder verschenken · zum Recycling bringen (nicht Hausmüll, nicht Schublade)'),
    ]),
    ('bewertung', [
        TAB('**M1:** Gewichtete Bewertung (Gewicht · Punkte).', ['Kriterium', 'Gewicht', 'Handy A', 'Handy B'], [['Preis', '2', '5', '3'], ['Lebensdauer', '3', '2', '4'], ['Reparierbarkeit', '2', '1', '5'], ['**Summe**', '', '[[18]]', '[[28]]']], h=6),
    ]),
]),

'05_Arbeitswelt': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Notiere einen technischen Beruf mit Tätigkeiten und Ausbildungsdauer.',
    sections=[
    ('revolution', [
        TAB('Ordne die industriellen Revolutionen.', ['Stufe', 'Kennzeichen'], [['1.0', '[[Dampfmaschine]]'], ['2.0', '[[Elektrizität, Fließband]]'], ['3.0', '[[Computer, Roboter]]'], ['4.0', '[[Vernetzung, Smart Factory]]']], h=6, widths=[20, 80]),
    ]),
    ('smart', [
        ZU('Ordne zu.', ['Digitaler Zwilling', 'Cobot', 'Vorausschauende Wartung'], ['Roboter neben Menschen', 'Teile tauschen, bevor sie kaputtgehen', 'virtuelles Abbild einer Maschine'], loes=[3, 1, 2]),
    ]),
    ('chancen', [
        A('Nenne je zwei Chancen und Risiken von Industrie 4.0.', 3, 'Chancen: weniger schwere Arbeit, individuelle Produkte, weniger Ausfälle, neue Berufe · Risiken: Wegfall einfacher Tätigkeiten, Hackerangriffe, Überwachung'),
    ]),
    ('berufe', [
        A('**M1:** Welcher technische Beruf interessiert dich? Begründe.', 2, 'Individuelle Antwort, z. B. Mechatroniker/-in, weil Mechanik, Elektronik und Programmieren zusammenkommen.'),
    ]),
]),

'06_Wiederholung': dict(ichkann=True, skip=['quiz-st'], heft_label='Notizen', heft_title='Das muss ich noch üben', heft_sub='Fragen, Merkpunkte, Begriffe',
    sections=[
    ('begriffe', [
        ZU('Ordne die Fachbegriffe zu.', ['CAD', 'Slicer', 'Lehre', 'Fixkosten', 'Smart Factory'],
           ['vernetzte Fabrik', 'zerlegt das Modell in Schichten', 'Konstruieren am Computer', 'prüft ein Maß', 'einmalige Kosten'], loes=[3, 2, 5, 4, 1]),
    ]),
    ('t1', [
        RF(['f|PVC darf gelasert werden.|PVC ist am Laser verboten (Chlorgas).', 'r|Der 3D-Druck gehört zum Urformen.', 'r|Eine kleinere Schichthöhe dauert länger.'], fix=False),
    ]),
    ('t2', [
        GL('Schablone 40 €, ohne Schablone 5 €/Stück, mit Schablone 3 €/Stück.', ['gleich teuer bei [[20]] Stück', 'Kosten für 30 Stück mit Schablone: [[130]] €']),
    ]),
    ('t3', [
        A('Erkläre, warum lange Nutzung eines Smartphones besonders nachhaltig ist.', 1, 'Der größte Teil der Umweltbelastung entsteht bei Rohstoffgewinnung und Herstellung – je länger man es nutzt, desto weniger neue Geräte werden gebraucht.'),
    ]),
]),
}
