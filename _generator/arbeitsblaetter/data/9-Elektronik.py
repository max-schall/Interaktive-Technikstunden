from render import *

TR = ('<svg viewBox="0 0 120 80" style="width:46mm;height:31mm" font-family="Barlow Semi Condensed,sans-serif" font-size="7">'
      '<g stroke="#111" stroke-width="1" fill="none"><circle cx="64" cy="40" r="22"/><path d="M54 26v28M20 40h34M54 33l20 -12V4M54 47l20 12v18"/></g>'
      '<path d="M74 59l-8 -1 4 -6z" fill="#111"/><text x="24" y="36">?</text><text x="80" y="12">?</text><text x="80" y="74">?</text></svg>')

WS = {
'01_Schalter_Relais': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne die Wechselschaltung und ein Relais mit Steuer- und Laststromkreis.',
    sections=[
    ('arten', [
        TAB('Ordne zu.', ['Bauteil', 'Schalter oder Taster?', 'Schließer oder Öffner?'], [['Klingelknopf', '[[Taster]]', '[[Schließer]]'], ['Lichtschalter', '[[Schalter]]', '[[Schließer]]'], ['Kühlschrank-Türkontakt', '[[Taster]]', '[[Öffner]]']], h=6),
    ]),
    ('wechsel', [
        BOX('Zeichne den Schaltplan einer Wechselschaltung mit Batterie, zwei Wechselschaltern und einer Lampe.', 38, loes='Batterie → Wechselschalter A (Mittelkontakt) → zwei parallele Leitungen → Wechselschalter B (Mittelkontakt) → Lampe → zurück zur Batterie.'),
    ]),
    ('relais', [
        L('Fließt Strom durch die [[Spule]], wird sie zum [[Elektromagneten]] und zieht den [[Anker]] an. Dieser schließt den [[Laststromkreis]]. Ohne Strom zieht eine [[Feder]] den Anker zurück.'),
    ]),
    ('m1', [
        A('**M1:** Begründe, warum man eine 230-V-Lampe über ein Relais von einem Mikrocontroller schalten lässt.', 2, 'Der Mikrocontroller liefert nur kleine Ströme bei 3–5 V. Das Relais trennt den ungefährlichen Steuerstromkreis vom gefährlichen Netzstromkreis.'),
    ]),
]),

'02_Dioden_LED': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne eine LED mit Vorwiderstand an einer 9-V-Batterie und beschrifte Anode und Kathode.',
    sections=[
    ('diode', [
        BOXES('Zeichne die Diode im Stromkreis.', ['Durchlassrichtung (Lampe leuchtet)', 'Sperrrichtung (Lampe aus)'], 30, loes=['Dreieck zeigt in Stromrichtung, Anode an +', 'Strich (Kathode) zum Pluspol']),
    ]),
    ('led', [
        L('Die [[Anode]] ist das längere Bein und kommt an Plus. Die [[Kathode]] ist das kürzere Bein; dort ist das Gehäuse [[abgeflacht]].'),
    ]),
    ('vorwiderstand', [
        GL('Berechne den Vorwiderstand mit R_V = (U_B − U_LED) : I.', ['U_B = 9 V, rote LED 2 V, 20 mA: R_V = [[350]] Ω', 'U_B = 5 V, blaue LED 3 V, 20 mA: R_V = [[100]] Ω', 'U_B = 12 V, grüne LED 2,2 V, 20 mA: R_V = [[490]] Ω']),
    ]),
    ('rechnen', [
        A('Erkläre, was passiert, wenn man eine LED ohne Vorwiderstand an 9 V anschließt.', 1, 'Es fließt ein sehr großer Strom, die LED wird zerstört.'),
    ]),
]),

'03_Sensoren': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und zeichne die Kennlinien von LDR und NTC als Skizze.',
    sections=[
    ('ldr', [
        TAB('Wie ändert sich der Widerstand?', ['Sensor', 'Einfluss', 'Widerstand'], [['LDR', 'mehr Licht', '[[sinkt]]'], ['NTC', 'wärmer', '[[sinkt]]'], ['PTC', 'wärmer', '[[steigt]]']], h=6),
    ]),
    ('teiler', [
        A('Ein LDR ist R₂. Erkläre, was mit U₂ passiert, wenn es dunkel wird.', 2, 'Der Widerstand des LDR steigt. Am größeren Widerstand liegt die größere Spannung, also steigt U₂.'),
    ]),
    ('alltag', [
        ZU('Ordne zu.', ['Lichtsensor', 'Temperatursensor', 'Ultraschallsensor', 'Bewegungsmelder'], ['Einparkhilfe', 'automatische Tür', 'Straßenlaterne', 'Thermostat'], loes=[3, 4, 1, 2]),
    ]),
    ('rechnen', [
        GL('Berechne U₂ = U · R₂ : (R₁ + R₂).', ['U = 9 V, R₁ = 10 kΩ, R₂ = 20 kΩ → U₂ = [[6]] V', 'U = 12 V, R₁ = R₂ → U₂ = [[6]] V', 'U = 9 V, R₁ = 2 kΩ, R₂ = 1 kΩ → U₂ = [[3]] V', 'U = 6 V, R₁ = 1 kΩ, R₂ = 5 kΩ → U₂ = [[5]] V']),
    ]),
]),

'04_Transistor': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne die Dunkelschaltung und markiere, wo der LDR sitzt.',
    sections=[
    ('aufbau', [
        BILD('Beschrifte die Anschlüsse des Transistors.', TR, n=1, loes='links: Basis (B) · oben: Kollektor (C) · unten mit Pfeil: Emitter (E)'),
    ]),
    ('dunkel', [
        L('Ein kleiner [[Basisstrom]] steuert einen großen [[Kollektorstrom]]. Ab etwa [[0,7]] V zwischen Basis und Emitter schaltet der Transistor durch.'),
        A('Erkläre, warum die LED in der Dunkelschaltung bei Dunkelheit angeht.', 3, 'Der LDR sitzt zwischen Basis und Emitter. Bei Dunkelheit wird sein Widerstand groß, an ihm liegt eine größere Spannung. Erreicht sie 0,7 V, fließt Basisstrom und der Transistor schaltet die LED ein.'),
    ]),
    ('schwelle', [
        A('Wozu dient das Poti in der Schaltung?', 1, 'Mit dem Poti stellt man die Schaltschwelle ein, also bei welcher Helligkeit die LED angeht.'),
    ]),
    ('anwendung', [
        SORT('Sortiere die Anwendungen.', ['Nachtlicht', 'Lüfter bei Hitze', 'Rollladen bei Sonne', 'Straßenlaterne', 'Feuermelder'], ['Dunkelschaltung', 'Hellschaltung', 'Wärmeschaltung'], h=14,
             loes=[['Nachtlicht', 'Straßenlaterne'], ['Rollladen bei Sonne'], ['Lüfter bei Hitze', 'Feuermelder']]),
    ]),
]),

'05_Kondensator': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und skizziere die Entladekurve eines Kondensators.',
    sections=[
    ('aufbau', [
        L('Ein Kondensator besteht aus zwei leitenden [[Platten]], getrennt durch einen [[Isolator]]. Er speichert elektrische [[Ladung]]. Die Kapazität wird in [[Farad]] angegeben.'),
    ]),
    ('laden', [
        BOX('Skizziere, wie die Spannung am Kondensator nach dem Loslassen des Tasters abnimmt (Zeit nach rechts, Spannung nach oben).', 32, loes='Kurve fällt zuerst steil, dann immer flacher ab (Entladekurve).'),
    ]),
    ('tau', [
        GL('Berechne τ = R · C (kΩ · µF = ms).', ['R = 100 kΩ, C = 100 µF → τ = [[10]] s', 'R = 47 kΩ, C = 470 µF → τ = [[22,09]] s', 'R = 10 kΩ, C = 1000 µF → τ = [[10]] s']),
    ]),
    ('m1', [
        A('**M1:** Nenne zwei Anwendungen für Kondensatoren.', 1, 'Innenlicht im Auto (Verzögerung), Blitzgerät, Netzteil (Glättung), Defibrillator'),
    ]),
]),

'06_Schaltungen_bauen': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne eine gute und eine schlechte Lötstelle im Schnitt.',
    sections=[
    ('farbcode', [
        TAB('Bestimme die Widerstandswerte.', ['Ring 1', 'Ring 2', 'Ring 3', 'Wert'], [['braun', 'schwarz', 'rot', '[[1 kΩ]]'], ['gelb', 'violett', 'braun', '[[470 Ω]]'], ['rot', 'rot', 'orange', '[[22 kΩ]]'], ['[[orange]]', '[[orange]]', '[[braun]]', '330 Ω']], h=6),
    ]),
    ('steckbrett', [
        A('Erkläre, welche Löcher eines Steckbretts leitend miteinander verbunden sind.', 2, 'Je fünf Löcher einer kurzen Reihe sind verbunden (nicht über den Mittelsteg). Die langen Randschienen sind über die ganze Länge verbunden (Plus und Minus).'),
    ]),
    ('loeten', [
        GL('Ergänze die Schritte beim Löten.', ['Spitze reinigen → Lötstelle [[erhitzen]] → [[Lot]] an die Lötstelle führen → erst Lot, dann [[Kolben]] wegnehmen → Beinchen kürzen']),
    ]),
    ('fehler', [
        ZU('**M1:** Ordne Fehler und Ursache zu.', ['LED dunkel, Spannung da', 'LED kurz hell, dann tot', 'geht nur beim Drücken'], ['kalte Lötstelle', 'LED falsch gepolt', 'Vorwiderstand fehlt'], loes=[3, 1, 2]),
    ]),
]),

'07_Wiederholung': dict(ichkann=True, skip=['quiz-st'], heft_label='Notizen', heft_title='Das muss ich noch üben', heft_sub='Fragen, Merkpunkte, Formeln',
    sections=[
    ('begriffe', [
        ZU('Ordne die Fachbegriffe zu.', ['Relais', 'Diode', 'LDR', 'Transistor', 'Kondensator'],
           ['speichert Ladung', 'elektromagnetischer Schalter', 'lässt Strom nur in eine Richtung', 'kleiner Strom steuert großen', 'Widerstand sinkt bei Licht'], loes=[5, 1, 3, 4, 2]),
    ]),
    ('t1', [
        GL('Rechne.', ['R_V für 9 V, LED 3 V, 20 mA: [[300]] Ω', 'U₂ bei 9 V, R₁ = 1 kΩ, R₂ = 2 kΩ: [[6]] V', 'τ bei 47 kΩ und 100 µF: [[4,7]] s']),
    ]),
    ('t2', [
        A('Erkläre die Hellschaltung in zwei Sätzen.', 2, 'Der LDR sitzt zwischen Plus und Basis. Bei Helligkeit sinkt sein Widerstand, die Basisspannung steigt über 0,7 V und der Transistor schaltet die LED ein.'),
    ]),
    ('t3', [
        TAB('Farbcode', ['Farben', 'Wert'], [['braun-schwarz-orange', '[[10 kΩ]]'], ['rot-violett-braun', '[[270 Ω]]']], h=6, widths=[60, 40]),
    ]),
]),
}
