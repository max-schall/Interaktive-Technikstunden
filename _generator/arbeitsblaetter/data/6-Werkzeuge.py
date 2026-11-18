from render import *

WS = {
'01_Werkzeuge_ordnen': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Notiere zu jeder Gruppe zwei Werkzeuge aus eurem Technikraum.',
    sections=[
    ('gruppen', [
        SORT('Sortiere die Werkzeuge nach ihrer Aufgabe.', ['Stahlmaßstab', 'Feile', 'Schraubendreher', 'Rundzange', 'Schraubstock', 'Bohrer', 'Hammer und Nagel', 'Reißnadel', 'Schraubzwinge', 'Seitenschneider'],
             ['Messen/Anreißen', 'Spannen', 'Trennen', 'Fügen', 'Umformen'], h=22,
             loes=[['Stahlmaßstab', 'Reißnadel'], ['Schraubstock', 'Schraubzwinge'], ['Feile', 'Bohrer', 'Seitenschneider'], ['Schraubendreher', 'Hammer und Nagel'], ['Rundzange']]),
    ]),
    ('trennen', [
        ZU('Ordne den Trennwerkzeugen ihren Einsatz zu.', ['Feinsäge', 'Laubsäge', 'Bügelsäge', 'Feile', 'Blechschere'],
           ['dünnes Blech schneiden', 'Kurven in dünnem Holz', 'Kanten glätten', 'gerade Schnitte in Holzleisten', 'Metallrohre ablängen'], loes=[5, 2, 4, 1, 3]),
        A('Erkläre, was beim Zerspanen passiert.', 1, 'Eine Schneide hebt kleine Teilchen (Späne) vom Werkstück ab; so wird Material abgetrennt.'),
    ]),
    ('auswahl', [
        TAB('Welches Werkzeug wählst du?', ['Aufgabe', 'Werkzeug'], [['Rundholz auf 120 mm kürzen', '[[Feinsäge]]'], ['Draht zu einer Öse biegen', '[[Rundzange]]'], ['Linie auf Aluminium anreißen', '[[Reißnadel]]'], ['Leimfuge zusammenpressen', '[[Schraubzwinge]]']], h=7, widths=[60, 40]),
    ]),
    ('m1', [
        A('**M1:** Die Kombizange passt in zwei Gruppen. Begründe.', 2, 'Mit den Backen kann man Draht biegen (Umformen), mit der Schneide Draht abkneifen (Trennen).'),
    ]),
]),

'02_Fuegen_Umformen': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne den Hammer und beschrifte Bahn, Finne, Kopf, Keil und Stiel.',
    sections=[
    ('schraube', [
        BOXES('Zeichne die Schraubenköpfe.', ['Schlitz', 'Kreuzschlitz PH', 'Innensechskant', 'Torx'], 24, loes=['ein gerader Schlitz', 'Kreuz', 'Sechseck', 'Stern mit sechs Spitzen']),
        A('Begründe, warum die Klinge genau passen muss.', 1, 'Sonst rutscht sie ab: Der Schraubenkopf wird beschädigt und man kann sich verletzen.'),
    ]),
    ('hammer', [
        L('Die flache Schlagfläche heißt [[Bahn]], das keilförmige Ende [[Finne]]. Der [[Keil]] hält den Kopf auf dem Stiel. Man greift den Hammer am [[Stielende]].'),
    ]),
    ('zangen', [
        ZU('Ordne die Zangen zu.', ['Rundzange', 'Seitenschneider', 'Beißzange', 'Flachzange'],
           ['Nägel herausziehen', 'kleine Teile halten', 'Drahtösen biegen', 'Kabel abschneiden'], loes=[3, 4, 1, 2]),
    ]),
    ('biegen', [
        A('Beschreibe in drei Schritten, wie du einen Blechwinkel im Schraubstock biegst.', 3, 'Biegelinie anreißen · Blech mit Schutzbacken so spannen, dass die Linie an der Backenkante liegt · mit Holzklotz und Kunststoffhammer auf 90° biegen und prüfen.'),
    ]),
]),

'03_Maschinen': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Skizziere den Schleifteller und markiere mit einem Pfeil die Seite, an der geschliffen wird.',
    sections=[
    ('deku', [
        TAB('Ergänze die Tabelle zur Dekupiersäge.', ['Teil', 'Aufgabe'], [['Niederhalter', '[[hält das Werkstück auf dem Tisch]]'], ['Sägeblatt', '[[Zähne zeigen nach unten]]'], ['Drehzahlregler', '[[Hubzahl je nach Werkstoff]]'], ['Spannknopf', '[[spannt das Sägeblatt]]']], h=7, widths=[30, 70]),
    ]),
    ('stich', [
        SORT('Ordne zu.', ['Werkstück wird zum Blatt geführt', 'Pendelhub', 'Rundungen und Stirnseiten', 'Niederhalter einstellen', 'Fußplatte muss aufliegen', 'abwärts laufende Seite'],
             ['Dekupiersäge', 'Stichsäge', 'Tellerschleifmaschine'], h=16,
             loes=[['Werkstück wird zum Blatt geführt', 'Niederhalter einstellen'], ['Pendelhub', 'Fußplatte muss aufliegen'], ['Rundungen und Stirnseiten', 'abwärts laufende Seite']]),
    ]),
    ('teller', [
        A('Erkläre, warum man nur an der abwärts laufenden Seite des Schleiftellers schleift.', 2, 'Dort drückt der Teller das Werkstück auf den Auflagetisch. Auf der anderen Seite würde es nach oben gerissen und weggeschleudert.'),
    ]),
    ('regeln', [
        RF(['f|Zum Sägeblattwechsel reicht es, die Maschine auszuschalten.|Der Netzstecker muss gezogen werden.', 'r|Beim Schleifen wird die Absaugung eingeschaltet.', 'f|Kleine Teile schleift man an der Maschine.|Kleine Teile schleift man von Hand.']),
    ]),
]),

'04_Fuehrerschein': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Gestalte deinen eigenen Maschinenführerschein für die Tischbohrmaschine.',
    sections=[
    ('weg', [
        A('Nenne die Schritte auf dem Weg zum Maschinenführerschein.', 2, 'Einweisung · Regeln lernen · Theorieprüfung · praktische Prüfung unter Aufsicht · Eintrag und Unterschrift · Arbeiten mit Erlaubnis.'),
    ]),
    ('check', [
        TAB('Erstelle eine Checkliste für die Tischbohrmaschine.', ['vor dem Einschalten', 'während der Arbeit', 'nach der Arbeit'],
            [['[[Schutzbrille, Haare zusammen, Werkstück spannen, Schlüssel abziehen]]', '[[konzentriert, Hände weg vom Bohrer, niemand daneben]]', '[[ausschalten, Stillstand abwarten, Späne mit Handfeger, Mängel melden]]']], h=26, widths=[34, 33, 33]),
    ]),
    ('fehler', [
        A('Nenne vier Fehler, die an der Bohrmaschine gefährlich sind, und begründe jeweils.', 4, 'offene Haare – werden vom Bohrer erfasst · Handschuhe – werden mitgerissen · Werkstück nicht gespannt – wird herumgeschleudert · Schlüssel steckt – fliegt weg · keine Schutzbrille – Späne im Auge · Schmuck – verfängt sich.'),
    ]),
    ('m1', [
        BOX('**M1:** Merkblatt: Skizziere „deine“ Maschine und beschrifte die Bedienteile.', 42, loes='z. B. Dekupiersäge mit Sägeblatt, Niederhalter, Tisch, Schalter, Drehzahlregler, Absaugung'),
    ]),
]),

'05_Wiederholung': dict(ichkann=True, skip=['quiz-st'], heft_label='Notizen', heft_title='Das muss ich noch üben', heft_sub='Fragen, Merkpunkte, Begriffe',
    sections=[
    ('begriffe', [
        ZU('Ordne die Fachbegriffe zu.', ['Trennen', 'Fügen', 'Umformen', 'Niederhalter', 'Finne'],
           ['Teile werden verbunden', 'keilförmiges Ende am Hammer', 'Form ändert sich ohne Späne', 'hält das Werkstück auf dem Sägetisch', 'Material wird abgetrennt'], loes=[2, 5, 3, 4, 1]),
    ]),
    ('t1', [
        SORT('Sortiere.', ['Raspel', 'Anschlagwinkel', 'Schraubendreher', 'Rundzange', 'Blechschere', 'Hammer und Nagel'], ['Messen', 'Trennen', 'Fügen', 'Umformen'], h=14,
             loes=[['Anschlagwinkel'], ['Raspel', 'Blechschere'], ['Schraubendreher', 'Hammer und Nagel'], ['Rundzange']]),
    ]),
    ('t2', [
        ZU('Ordne zu.', ['Kombizange', 'Beißzange', 'Torx'], ['Nägel herausziehen', 'Stern-Antrieb', 'halten, biegen, abkneifen'], loes=[2, 3, 1]),
    ]),
    ('t3', [
        RF(['f|An der Bohrmaschine trägt man Handschuhe.|Handschuhe sind dort verboten.', 'r|Vor dem Einschalten wird der Bohrfutterschlüssel abgezogen.', 'f|Man schleift an der aufwärts laufenden Tellerseite.|Nur an der abwärts laufenden Seite.'], fix=False),
    ]),
]),
}
