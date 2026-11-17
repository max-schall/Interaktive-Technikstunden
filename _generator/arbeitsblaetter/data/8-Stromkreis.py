from render import *

SYMS = ('<svg viewBox="0 0 190 30" style="width:150mm;height:24mm" font-family="Barlow Semi Condensed,sans-serif" font-size="5">'
        '<g stroke="#111" stroke-width=".8" fill="none">'
        '<path d="M2 12h10M18 12h10M12 6v12"/><path d="M18 9v6" stroke-width="2"/>'
        '<path d="M34 12h8M54 12h8"/><circle cx="48" cy="12" r="6"/><path d="M44 8l8 8M52 8l-8 8"/>'
        '<path d="M68 12h6M90 12h6"/><rect x="74" y="9" width="16" height="6"/>'
        '<path d="M102 12h8M124 12h8M110 12l12-6"/><circle cx="110" cy="12" r="1"/><circle cx="124" cy="12" r="1"/>'
        '<path d="M138 12h8M158 12h8"/><circle cx="152" cy="12" r="6"/>'
        '<path d="M172 12h16M180 12v8"/><circle cx="180" cy="12" r="1.4" fill="#111"/></g>'
        '<g fill="#111" text-anchor="middle"><text x="15" y="27">A</text><text x="48" y="27">B</text><text x="82" y="27">C</text><text x="117" y="27">D</text><text x="152" y="15">A</text><text x="152" y="27">E</text><text x="180" y="27">F</text></g></svg>')

WS = {
'01_Stromkreis': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne den Schaltplan eines Stromkreises mit Batterie, Schalter und Lampe.',
    sections=[
    ('kreis', [
        L('Ein Stromkreis besteht aus [[Spannungsquelle]], [[Leitungen]] und [[Verbraucher]]. Strom fließt nur, wenn der Stromkreis [[geschlossen]] ist.'),
    ]),
    ('zeichen', [
        BILD('Benenne die Schaltzeichen A bis F.', SYMS, n=2, loes='A Batterie · B Lampe · C Widerstand · D Schalter (offen) · E Amperemeter · F Leitungsverzweigung'),
    ]),
    ('leiter', [
        SORT('Sortiere die Stoffe.', ['Kupfer', 'Glas', 'Graphit', 'Kunststoff', 'Aluminium', 'trockenes Holz', 'Salzwasser', 'Gummi'], ['Leiter', 'Nichtleiter'], h=16,
             loes=[['Kupfer', 'Graphit', 'Aluminium', 'Salzwasser'], ['Glas', 'Kunststoff', 'Holz', 'Gummi']]),
    ]),
    ('kurzschluss', [
        A('**M1:** Erkläre, was bei einem Kurzschluss passiert und warum er gefährlich ist.', 2, 'Der Strom fließt am Verbraucher vorbei direkt von Pol zu Pol. Die Stromstärke wird sehr groß, die Leitungen werden heiß – Brandgefahr.'),
    ]),
]),

'02_Spannung_Strom': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne den Schaltplan mit Amperemeter in Reihe und Voltmeter parallel zur Lampe.',
    sections=[
    ('modell', [
        TAB('Wassermodell: Ergänze.', ['Wasserkreislauf', 'Stromkreis'], [['Pumpe', '[[Spannungsquelle]]'], ['Rohr', '[[Leitung]]'], ['Turbine', '[[Verbraucher]]'], ['Wassermenge pro Sekunde', '[[Stromstärke]]']], h=6, widths=[50, 50]),
    ]),
    ('groessen', [
        TAB('Größen und Einheiten', ['Größe', 'Formelzeichen', 'Einheit', 'Messgerät'], [['Spannung', '[[U]]', '[[Volt (V)]]', '[[Voltmeter]]'], ['Stromstärke', '[[I]]', '[[Ampere (A)]]', '[[Amperemeter]]']], h=7),
    ]),
    ('multimeter', [
        A('Beschreibe, wie du mit dem Multimeter die Spannung einer Batterie misst.', 2, 'Drehschalter auf V⎓ (Gleichspannung), passenden Bereich wählen; schwarzes Kabel in COM, rotes in V; Messspitzen an Plus- und Minuspol halten.'),
    ]),
    ('messen', [
        BOX('Zeichne einen Stromkreis mit Lampe, in dem Stromstärke und Spannung an der Lampe gemessen werden.', 36, loes='Amperemeter in Reihe zur Lampe, Voltmeter parallel zur Lampe.'),
    ]),
]),

'03_Widerstand': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und zeichne das Formeldreieck.',
    sections=[
    ('messreihe', [
        TAB('Messreihe mit R = 100 Ω – berechne I.', ['U in V', '2', '4', '6', '8'], [['I in mA', '[[20]]', '[[40]]', '[[60]]', '[[80]]']], h=7),
        BOX('Zeichne die U-I-Kennlinie (U nach rechts, I nach oben).', 34, loes='Gerade durch den Ursprung bis (8 V | 80 mA).'),
    ]),
    ('gesetz', [
        GL('Stelle das ohmsche Gesetz um.', ['U = [[R · I]]', 'R = [[U : I]]', 'I = [[U : R]]']),
    ]),
    ('rechnen', [
        GL('Berechne.', ['R = 220 Ω, I = 50 mA → U = [[11]] V', 'U = 12 V, I = 0,04 A → R = [[300]] Ω', 'U = 9 V, R = 450 Ω → I = [[20]] mA']),
    ]),
    ('draht', [
        A('**M1:** Nenne drei Größen, von denen der Widerstand eines Drahtes abhängt.', 1, 'Länge, Querschnitt (Dicke), Material'),
    ]),
]),

'04_Reihe_Parallel': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne beide Schaltungen mit zwei Lampen als Schaltplan.',
    sections=[
    ('reihe', [
        A('Zwei gleiche Lampen sind in Reihe an 6 V geschaltet. Gib die Spannung an jeder Lampe an und erkläre, was passiert, wenn eine Lampe durchbrennt.', 2, 'Jede Lampe bekommt 3 V. Brennt eine durch, ist der Stromkreis unterbrochen – auch die andere geht aus.'),
    ]),
    ('parallel', [
        A('Zwei gleiche Lampen sind parallel an 6 V. Durch jede fließen 0,3 A. Wie groß ist der Gesamtstrom?', 1, 'I = 0,3 A + 0,3 A = 0,6 A'),
    ]),
    ('regeln', [
        TAB('Ergänze die Regeln.', ['', 'Reihenschaltung', 'Parallelschaltung'], [['Stromstärke', '[[überall gleich]]', '[[I = I₁ + I₂]]'], ['Spannung', '[[U = U₁ + U₂]]', '[[überall gleich]]'], ['Gesamtwiderstand', '[[R₁ + R₂]]', '[[kleiner als R₁ und R₂]]']], h=7),
    ]),
    ('rechnen', [
        GL('Berechne.', ['R₁ = 30 Ω, R₂ = 60 Ω in Reihe: R_ges = [[90]] Ω', 'an 9 V: I = [[100]] mA', 'zwei Widerstände je 200 Ω parallel: R_ges = [[100]] Ω']),
    ]),
]),

'05_Leistung_Sicherheit': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Berechne die Jahres-Stromkosten eines Geräts aus deinem Haushalt.',
    sections=[
    ('leistung', [
        GL('Berechne die Leistung bzw. Stromstärke.', ['U = 12 V, I = 2 A → P = [[24]] W', 'Wasserkocher 2300 W an 230 V → I = [[10]] A']),
        TAB('Ordne die Geräte nach ihrer Leistung und schätze, wie lange sie für 1 kWh laufen.', ['Gerät', 'Leistung', 'Zeit für 1 kWh'], [['LED-Lampe', '7 W', '[[ca. 143 h]]'], ['Laptop', '60 W', '[[ca. 17 h]]'], ['Fernseher', '100 W', '[[10 h]]'], ['Föhn', '2000 W', '[[30 min]]']], h=7),
    ]),
    ('kosten', [
        GL('Berechne Energie und Kosten (35 ct pro kWh).', ['Föhn 2000 W, 15 min: E = [[0,5]] kWh, Kosten: [[17,5]] ct', 'Fernseher 100 W, 3 h täglich, 1 Jahr: E = [[109,5]] kWh, Kosten: [[38,33]] €']),
    ]),
    ('gefahr', [
        ZU('Ordne die Schutzmaßnahmen zu.', ['Isolierung', 'Schutzleiter', 'Sicherung', 'FI-Schutzschalter'], ['schaltet bei Fehlerstrom ab', 'unterbricht bei zu großem Strom', 'verhindert Berührung der Leiter', 'leitet Strom vom Gehäuse zur Erde'], loes=[4, 3, 1, 2]),
    ]),
    ('verhalten', [
        A('**M1:** Nenne drei Regeln für den sicheren Umgang mit Elektrogeräten.', 2, 'Stecker nicht am Kabel ziehen · keine Geräte in der Nähe von Wasser · defekte Kabel nicht benutzen · Mehrfachsteckdosen nicht hintereinanderstecken · vor Arbeiten Sicherung ausschalten'),
    ]),
]),

'06_Wiederholung': dict(ichkann=True, skip=['quiz-st'], heft_label='Notizen', heft_title='Das muss ich noch üben', heft_sub='Fragen, Merkpunkte, Formeln',
    sections=[
    ('begriffe', [
        ZU('Ordne die Fachbegriffe zu.', ['Kurzschluss', 'Isolator', 'Amperemeter', 'Ohmsches Gesetz', 'FI-Schalter'],
           ['U = R · I', 'Strom fließt am Verbraucher vorbei', 'schaltet bei Fehlerstrom ab', 'Nichtleiter', 'misst die Stromstärke in Reihe'], loes=[4, 1, 5, 2, 3]),
    ]),
    ('t1', [
        TAB('Ergänze.', ['Größe', 'Zeichen', 'Einheit'], [['Spannung', '[[U]]', '[[V]]'], ['Stromstärke', '[[I]]', '[[A]]'], ['Widerstand', '[[R]]', '[[Ω]]'], ['Leistung', '[[P]]', '[[W]]']], h=6),
    ]),
    ('t2', [
        GL('Rechne.', ['R = 100 Ω, I = 0,05 A → U = [[5]] V', 'U = 6 V, I = 0,5 A → P = [[3]] W']),
    ]),
    ('t3', [
        RF(['r|In der Reihenschaltung ist die Stromstärke überall gleich.', 'f|Im Haus sind die Geräte in Reihe geschaltet.|Sie sind parallel geschaltet.', 'r|In der Parallelschaltung liegt an jedem Zweig die volle Spannung.'], fix=False),
    ]),
]),
}
