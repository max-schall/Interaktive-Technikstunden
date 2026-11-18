from render import *

WS = {
'01_Elektromagnet': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne einen Elektromagneten mit Spule, Eisenkern und Batterie.',
    sections=[
    ('leiter', [
        A('Beschreibe, was mit der Kompassnadel passiert, wenn Strom durch den Draht fließt. Was folgt daraus?', 2, 'Die Nadel wird abgelenkt und stellt sich quer zum Draht. Um einen stromdurchflossenen Leiter entsteht ein Magnetfeld.'),
    ]),
    ('spule', [
        TAB('Wie verändert sich die Stärke des Elektromagneten?', ['Änderung', 'stärker oder schwächer?'], [['mehr Windungen', '[[stärker]]'], ['kleinere Stromstärke', '[[schwächer]]'], ['Eisenkern herausnehmen', '[[viel schwächer]]'], ['Strom ausschalten', '[[keine Wirkung]]']], h=7, widths=[55, 45]),
    ]),
    ('anwend', [
        ZU('Ordne die Anwendungen zu.', ['Schrottkran', 'Türöffner', 'Relais', 'Lautsprecher'],
           ['kleiner Strom schaltet großen Strom', 'Membran bewegt sich im Takt', 'hebt Eisen und lässt es fallen', 'zieht den Riegel zurück'], loes=[3, 4, 1, 2]),
    ]),
    ('vergleich', [
        TAB('Vergleiche.', ['Eigenschaft', 'Dauermagnet', 'Elektromagnet'], [['ein- und ausschaltbar', '[[nein]]', '[[ja]]'], ['Stärke veränderbar', '[[nein]]', '[[ja]]'], ['braucht Strom', '[[nein]]', '[[ja]]']], h=7, widths=[44, 28, 28]),
    ]),
]),

'02_Klingel_Relais': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne den Schaltplan einer Relaisschaltung mit Steuer- und Arbeitsstromkreis.',
    sections=[
    ('klingel', [
        A('Erkläre in vier Schritten, warum die Klingel immer wieder schlägt.', 4, 'Strom fließt, der Elektromagnet zieht den Anker an · der Klöppel schlägt an die Glocke · der Unterbrecherkontakt öffnet, der Strom ist weg · die Feder zieht den Anker zurück, der Kontakt schließt – von vorn.'),
    ]),
    ('relais', [
        L('Ein Relais ist ein [[Schalter]], der von einem [[Elektromagneten]] betätigt wird. Die Spule liegt im [[Steuerstromkreis]], der Kontakt im [[Arbeitsstromkreis]]. Ein [[Schließer]] schließt, ein [[Öffner]] öffnet, wenn Strom durch die Spule fließt.'),
        TAB('Ergänze: Wie steht der Kontakt?', ['Spule', 'Schließer', 'Öffner'], [['ohne Strom', '[[offen]]', '[[geschlossen]]'], ['mit Strom', '[[geschlossen]]', '[[offen]]']], h=7, widths=[34, 33, 33]),
    ]),
    ('vorteile', [
        A('Nenne zwei Vorteile eines Relais.', 2, 'Ein kleiner Steuerstrom kann einen großen Arbeitsstrom schalten. · Steuer- und Arbeitsstromkreis sind elektrisch getrennt (z. B. 4,5 V und 12 V).'),
        A('Ein Lüfter mit 12 V soll über einen Taster an einem 4,5-V-Stromkreis eingeschaltet werden. Beschreibe die Lösung.', 2, 'Der Taster schaltet die Relaisspule im 4,5-V-Steuerstromkreis. Der Schließer des Relais schaltet den 12-V-Arbeitsstromkreis mit dem Lüfter.'),
    ]),
]),

'03_Hausschaltungen': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne den Schaltplan der Wechselschaltung mit Batterie, zwei Wechselschaltern und Lampe.',
    sections=[
    ('serie', [
        A('Erkläre den Unterschied zwischen Ausschaltung und Serienschaltung an einem Beispiel.', 2, 'Ausschaltung: ein Schalter schaltet eine Leuchte (Abstellraum). Serienschaltung: zwei Wippen schalten zwei Lampengruppen getrennt (Kronleuchter, Bad).'),
    ]),
    ('wechsel', [
        TAB('Ergänze die Tabelle zur Wechselschaltung.', ['S1', 'S2', 'Lampe'], [['unten', 'unten', '[[an]]'], ['unten', 'oben', '[[aus]]'], ['oben', 'unten', '[[aus]]'], ['oben', 'oben', '[[an]]']], h=6, widths=[33, 33, 34]),
    ]),
    ('raum', [
        ZU('Welche Schaltung passt?', ['Ausschaltung', 'Serienschaltung', 'Wechselschaltung', 'Kreuzschaltung'],
           ['Flur mit zwei Türen', 'Treppenhaus über drei Etagen', 'Abstellraum', 'Kronleuchter mit zwei Gruppen'], loes=[3, 4, 1, 2]),
    ]),
    ('modell', [
        BOX('**M1:** Skizziere den Grundriss eures Modellhauses und trage Schalter und Leuchten ein.', 40, loes='z. B. Flur mit Wechselschaltung, Wohnzimmer mit Serienschaltung, Abstellraum mit Ausschaltung'),
    ]),
]),

'04_Fehlersuche': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Notiere das Vorgehen bei der Fehlersuche als nummerierte Liste.',
    sections=[
    ('fehler', [
        ZU('Ordne dem Fehlerbild die Ursache zu.', ['Lampe flackert beim Wackeln', 'Lampe leuchtet sehr schwach', 'neue LED bleibt dunkel', 'Kabel wird heiß'],
           ['Kurzschluss', 'falsche Polung', 'Wackelkontakt', 'Batterie fast leer'], loes=[4, 3, 2, 1]),
    ]),
    ('pruefer', [
        A('Erkläre, was ein Durchgangsprüfer anzeigt, und nenne eine Sicherheitsregel.', 2, 'Er zeigt an, ob ein Bauteil oder eine Leitung Strom leitet (Durchgang). Er darf nur an spannungsfreien Teilen benutzt werden.'),
    ]),
    ('suche', [
        TAB('Protokolliere deine Fehlersuche im Simulator.', ['Nr.', 'geprüftes Teil', 'Ergebnis'], [['1', '', ''], ['2', '', ''], ['3', '', ''], ['4', '', '']], h=7, widths=[10, 50, 40]),
    ]),
    ('vorgehen', [
        A('Nenne die Schritte einer systematischen Fehlersuche.', 3, 'Sichtprüfung · Spannungsquelle messen · abklemmen · Bauteile und Leitungen einzeln auf Durchgang prüfen · defektes Teil tauschen · Funktion testen.'),
    ]),
]),

'05_Alarmanlage': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne die Schaltpläne einer Alarmanlage nach dem Arbeits- und nach dem Ruhestromprinzip.',
    sections=[
    ('arbeit', [
        A('Erkläre, warum eine Alarmanlage nach dem Arbeitsstromprinzip leicht zu überlisten ist.', 2, 'Im Ruhezustand fließt kein Strom. Wird das Kabel durchtrennt, kann beim Öffnen kein Strom mehr fließen – der Alarm bleibt stumm, und niemand bemerkt es.'),
    ]),
    ('ruhe', [
        L('Beim Ruhestromprinzip fließt im Ruhezustand [[ständig]] Strom durch die [[Relaisspule]]. Wird der Kreis [[unterbrochen]], fällt das Relais ab. Sein [[Öffner]] schließt den Summerkreis.'),
    ]),
    ('selbst', [
        A('Erkläre die Aufgabe des Haltekontakts.', 2, 'Er liegt parallel zum Ein-Taster. Ist das Relais einmal angezogen, fließt der Strom über den Haltekontakt weiter; der Alarm bleibt an, bis der Aus-Taster den Kreis unterbricht.'),
    ]),
    ('m1', [
        BOX('**M1:** Zeichne den Schaltplan deiner geplanten Alarmanlage.', 42, loes='z. B. Ruhestromprinzip mit Reedkontakt an der Tür, Relais mit Öffner und Summer'),
    ]),
]),

'06_Wiederholung': dict(ichkann=True, skip=['quiz-st'], heft_label='Notizen', heft_title='Das muss ich noch üben', heft_sub='Fragen, Merkpunkte, Begriffe',
    sections=[
    ('begriffe', [
        ZU('Ordne die Fachbegriffe zu.', ['Elektromagnet', 'Relais', 'Wechselschaltung', 'Durchgangsprüfer', 'Ruhestromprinzip'],
           ['zeigt, ob ein Bauteil leitet', 'Spule mit Eisenkern', 'Unterbrechung löst Alarm aus', 'Schalter mit Elektromagnet', 'Lampe von zwei Stellen schalten'], loes=[4, 1, 5, 2, 3]),
    ]),
    ('t1', [
        RF(['r|Ein Elektromagnet wird mit mehr Windungen stärker.', 'f|Ohne Eisenkern ist er stärker.|Mit Eisenkern ist er stärker.', 'r|Ein Öffner ist ohne Strom in der Spule geschlossen.'], fix=False),
    ]),
    ('t2', [
        A('Welche Schaltung brauchst du für ein Treppenhaus über drei Etagen?', 1, 'Wechselschaltung mit einem Kreuzschalter (je weitere Schaltstelle ein Kreuzschalter).'),
    ]),
    ('t3', [
        A('Begründe, warum echte Alarmanlagen nach dem Ruhestromprinzip arbeiten.', 2, 'Ein durchtrenntes Kabel unterbricht den Ruhestrom und löst Alarm aus – Sabotage wird bemerkt.'),
    ]),
]),
}
