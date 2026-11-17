from render import *

WS = {
'01_Metalle': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne die Querschnitte von sechs Handelsformen und beschrifte sie.',
    sections=[
    ('pruefstand', [
        TAB('Trage die Ergebnisse des Prüfstands ein.', ['Probe', 'Magnet', 'Masse (1 cm³)', 'Farbe'], [['Stahl', '[[ja]]', '[[7,9 g]]', '[[silbergrau]]'], ['Aluminium', '[[nein]]', '[[2,7 g]]', '[[hell silbern]]'], ['Kupfer', '[[nein]]', '[[8,9 g]]', '[[rotbraun]]'], ['Messing', '[[nein]]', '[[8,5 g]]', '[[goldgelb]]']], h=6),
    ]),
    ('gruppen', [
        SORT('Sortiere.', ['Baustahl', 'Aluminium', 'Gusseisen', 'Kupfer', 'Messing', 'Zink', 'Bronze'], ['Eisenmetall', 'Nichteisenmetall', 'Legierung'], h=14,
             loes=[['Baustahl', 'Gusseisen'], ['Aluminium', 'Kupfer', 'Zink'], ['Messing', 'Bronze']]),
    ]),
    ('formen', [
        BOXES('Zeichne die Querschnitte.', ['Rohr', 'Winkelprofil', 'U-Profil', 'Flachstahl'], 22, loes=['Kreisring', 'L-Form', 'U-Form', 'flaches Rechteck']),
    ]),
    ('alltag', [
        A('**M1:** Begründe, warum Stromkabel aus Kupfer und Fahrradrahmen oft aus Aluminium sind.', 2, 'Kupfer leitet Strom sehr gut. Aluminium ist leicht und rostet nicht.'),
    ]),
]),

'02_Stahl': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne einen Hochofen und beschrifte Gicht, Möller, Heißwind, Schlacke und Roheisen.',
    sections=[
    ('hochofen', [
        L('In den Hochofen werden [[Eisenerz]], Koks und [[Kalk]] gefüllt. Unten wird heiße Luft (Heißwind) eingeblasen. Es entstehen flüssiges [[Roheisen]] und [[Schlacke]].'),
        ZU('Ordne die Teile des Hochofens zu.', ['Gicht', 'Möller', 'Heißwind', 'Schlacke', 'Gichtgas'], ['heißes Abgas oben', 'Einfüllöffnung oben', 'Gemisch aus Erz, Koks und Kalk', 'Gesteinsreste, schwimmen oben', 'eingeblasene heiße Luft'], loes=[5, 1, 2, 3, 4]),
        BOX('Zeichne einen Hochofen im Schnitt und beschrifte ihn.', 50, loes='Turm, oben Gicht mit Einfüllung, Möller-Schichten, unten Heißwind-Düsen, darunter Schlacke und Roheisen mit Abstich.'),
    ]),
    ('weg', [
        GL('Ergänze den Weg zum Stahl.', ['Eisenerz → [[Hochofen]] → Roheisen (ca. [[4]] % C) → Konverter → Stahl (unter [[2]] % C) → [[Walzen]] → Bleche, Profile']),
    ]),
    ('gruen', [
        A('**M1:** Erkläre, warum Stahl mit Wasserstoff klimafreundlicher ist als Stahl aus dem Hochofen.', 2, 'Im Hochofen nimmt Kohlenstoff den Sauerstoff auf, es entsteht CO₂. Bei der Direktreduktion entsteht mit Wasserstoff nur Wasserdampf – wenn der Wasserstoff mit Ökostrom erzeugt wird, entsteht kaum CO₂.'),
    ]),
]),

'03_Trennen': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und notiere die Formel für die Drehzahl mit einem Rechenbeispiel.',
    sections=[
    ('werkzeuge', [
        ZU('Ordne die Werkzeuge zu.', ['Reißnadel', 'Körner', 'Bügelsäge', 'Kegelsenker'], ['Bohrstelle markieren', 'entgraten', 'auf Metall anreißen', 'Rohre trennen'], loes=[3, 4, 1, 2]),
    ]),
    ('saegen', [
        A('Erkläre, warum man dünnes Blech mit einem feinen Sägeblatt sägt.', 2, 'Es müssen mindestens drei Zähne im Eingriff sein. Bei grober Zahnung haken die Zähne im dünnen Blech ein und brechen aus.'),
    ]),
    ('bohren', [
        GL('Berechne die Drehzahl mit n = v · 1000 : (π · d).', ['Stahl, v = 25 m/min, d = 8 mm: n ≈ [[995]] 1/min', 'Aluminium, v = 60 m/min, d = 10 mm: n ≈ [[1910]] 1/min']),
    ]),
    ('ablauf', [
        A('Beschreibe die Arbeitsschritte für einen Schlüsselanhänger aus Aluminiumblech.', 3, 'Anreißen · ankörnen · Loch bohren (gespannt) · aussägen oder schneiden · feilen · entgraten und glätten.'),
    ]),
]),

'04_Gewinde': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne ein Gewinde und beschrifte d, d₁ und P.',
    sections=[
    ('gewinde', [
        L('Die Bezeichnung M10 bedeutet: [[metrisches]] Gewinde mit [[10]] mm Nenndurchmesser. Die Steigung ist der Abstand von einer [[Gewindespitze]] zur nächsten.'),
    ]),
    ('kernloch', [
        TAB('Berechne die Kernlöcher (Kernloch = d − P).', ['Gewinde', 'M4', 'M5', 'M6', 'M10'], [['Steigung P', '0,7 mm', '0,8 mm', '1 mm', '1,5 mm'], ['Kernloch', '[[3,3 mm]]', '[[4,2 mm]]', '[[5 mm]]', '[[8,5 mm]]']], h=7),
        BOX('Zeichne einen Gewindebolzen und beschrifte Nenndurchmesser d, Kerndurchmesser d₁ und Steigung P.', 32, loes='Bolzen mit Zickzack-Rand; d außen über die Spitzen, d₁ innen am Grund, P von Spitze zu Spitze.'),
    ]),
    ('werkzeug', [
        ZU('Ordne zu.', ['Gewindebohrer', 'Windeisen', 'Schneideisen', 'Schneidöl'], ['kühlt und schmiert', 'schneidet Außengewinde', 'schneidet Innengewinde', 'hält den Gewindebohrer'], loes=[4, 3, 1, 2]),
    ]),
    ('ablauf', [
        A('Erkläre, warum man den Gewindebohrer nach jeder Umdrehung etwas zurückdreht.', 1, 'Damit der Span bricht und der Gewindebohrer nicht klemmt oder abbricht.'),
    ]),
]),

'05_Fuegen_Umformen': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und zeichne einen Blindniet vor und nach dem Setzen.',
    sections=[
    ('verfahren', [
        SORT('Sortiere die Verfahren.', ['Schrauben', 'Biegen', 'Lackieren', 'Löten', 'Abkanten', 'Verzinken', 'Nieten'], ['Fügen', 'Umformen', 'Beschichten'], h=14,
             loes=[['Schrauben', 'Löten', 'Nieten'], ['Biegen', 'Abkanten'], ['Lackieren', 'Verzinken']]),
    ]),
    ('nieten', [
        A('Erkläre den Unterschied zwischen Löten und Schweißen.', 2, 'Beim Löten schmilzt nur das Lot, die Werkstücke bleiben fest. Beim Schweißen schmelzen die Werkstücke selbst an der Fügestelle.'),
    ]),
    ('rost', [
        TAB('**M1:** Rostversuch – rostet der Nagel?', ['Bedingung', 'Ergebnis', 'Begründung'], [['trockene Luft', '[[nein]]', '[[kein Wasser]]'], ['Leitungswasser', '[[ja]]', '[[Wasser und Sauerstoff]]'], ['Salzwasser', '[[ja, stark]]', '[[Salz beschleunigt]]'], ['verzinkt', '[[nein]]', '[[Zinkschicht schützt]]']], h=6, widths=[30, 20, 50]),
    ]),
    ('schutz', [
        A('Nenne drei Verfahren zum Korrosionsschutz mit je einem Beispiel.', 2, 'Lackieren (Gartenzaun) · Feuerverzinken (Leitplanke) · Pulverbeschichten (Fahrradrahmen) · Ölen (Werkzeug, Kette).'),
    ]),
]),

'06_Wiederholung': dict(ichkann=True, skip=['quiz-st'], heft_label='Notizen', heft_title='Das muss ich noch üben', heft_sub='Fragen, Merkpunkte, Begriffe',
    sections=[
    ('begriffe', [
        ZU('Ordne die Fachbegriffe zu.', ['Legierung', 'Roheisen', 'Körner', 'Kernloch', 'Korrosion'],
           ['Zerstörung durch Rost', 'Mischung aus Metallen', 'Bohrung für Innengewinde', 'Produkt des Hochofens', 'markiert die Bohrstelle'], loes=[5, 1, 4, 2, 3]),
    ]),
    ('t1', [
        SORT('Sortiere.', ['Stahl', 'Kupfer', 'Messing', 'Aluminium', 'Gusseisen', 'Bronze'], ['Eisenmetall', 'NE-Metall', 'Legierung'], h=12,
             loes=[['Stahl', 'Gusseisen'], ['Kupfer', 'Aluminium'], ['Messing', 'Bronze']]),
    ]),
    ('t2', [
        GL('Rechne.', ['Kernloch M8 (P = 1,25 mm): [[6,75 ≈ 6,8]] mm', 'Drehzahl Stahl, d = 5 mm, v = 25 m/min: n ≈ [[1590]] 1/min']),
    ]),
    ('t3', [
        RF(['f|Löten ist eine lösbare Verbindung.|Löten ist unlösbar.', 'r|Biegen ist Umformen.', 'r|Salz beschleunigt das Rosten.'], fix=False),
    ]),
]),
}
