from render import *

WS = {
'01_Baum_Holz': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne einen Stammquerschnitt und beschrifte Rinde, Bast, Kambium, Splintholz, Kernholz und Mark.',
    sections=[
    ('stamm', [
        ZU('Ordne die Schichten des Stammes ihren Aufgaben zu.', ['Rinde', 'Bast', 'Kambium', 'Splintholz', 'Kernholz'],
           ['leitet Wasser nach oben', 'Wachstumsschicht', 'Schutz nach außen', 'stützt den Baum', 'leitet Nährstoffe nach unten'], loes=[4, 3, 1, 5, 2]),
    ]),
    ('ringe', [
        A('Erkläre, wie ein Jahresring entsteht.', 2, 'Im Frühjahr wächst helles, weiches Frühholz, im Sommer dunkles, festes Spätholz. Beide zusammen bilden einen Jahresring.'),
    ]),
    ('arten', [
        SORT('Sortiere die Holzarten.', ['Buche', 'Fichte', 'Eiche', 'Kiefer', 'Ahorn', 'Tanne', 'Lärche', 'Birke'], ['Laubholz', 'Nadelholz'], h=16,
             loes=[['Buche', 'Eiche', 'Ahorn', 'Birke'], ['Fichte', 'Kiefer', 'Tanne', 'Lärche']]),
    ]),
    ('arbeiten', [
        L('Holz nimmt Feuchtigkeit auf und [[quillt]]. Beim Trocknen [[schwindet]] es. Das geschieht vor allem [[quer]] zur Faser.', intro='**M1:** Ergänze die Lücken.'),
    ]),
]),

'02_Handelsformen': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Klebe kleine Proben der Holzwerkstoffe ein oder zeichne ihre Kanten.',
    sections=[
    ('vollholz', [
        TAB('Ordne den Querschnitten die Namen zu.', ['Querschnitt', 'Name'], [['dünn und breit, bis 40 mm dick', '[[Brett]]'], ['dick und breit, über 40 mm', '[[Bohle]]'], ['fast quadratisch, groß', '[[Kantholz]]'], ['sehr klein, für Rahmen', '[[Leiste]]'], ['rund', '[[Rundstab]]']], h=6, widths=[60, 40]),
    ]),
    ('werkstoffe', [
        TAB('Ergänze den Aufbau der Holzwerkstoffe.', ['Holzwerkstoff', 'Aufbau'], [['Sperrholz', '[[kreuzweise verleimte Furniere]]'], ['Tischlerplatte', '[[Mittellage aus Holzstäben, außen Furnier]]'], ['Spanplatte', '[[verpresste Holzspäne]]'], ['MDF', '[[feine Holzfasern]]']], h=7, widths=[30, 70]),
    ]),
    ('vergleich', [
        A('Nenne je einen Vorteil von Vollholz und von Holzwerkstoffen.', 2, 'Vollholz: natürliche, schöne Maserung, fest. · Holzwerkstoffe: große Platten, günstig, verziehen sich kaum, nutzen Holzreste.'),
    ]),
    ('m1', [
        A('**M1:** Du baust ein Regal mit 80 cm langen Böden. Begründe, welchen Werkstoff du wählst.', 2, 'Tischlerplatte (oder Vollholz/Leimholz): biegt sich kaum durch und trägt Bücher; Spanplatte würde durchhängen.'),
    ]),
]),

'03_Saegen_Feilen': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne die Zahnung von Feinsäge und Laubsäge mit Pfeil für die Schnittrichtung.',
    sections=[
    ('keil', [
        L('Jede Schneide hat die Form eines [[Keils]]. Ein kleiner Keilwinkel schneidet [[leicht]], bricht aber schneller aus. Für Metall braucht man einen [[großen]] Keilwinkel.'),
    ]),
    ('saegen', [
        TAB('Ergänze die Tabelle.', ['Säge', 'schneidet auf …', 'Einsatz'], [['Feinsäge', '[[Stoß]]', '[[gerade Schnitte in Leisten]]'], ['Laubsäge', '[[Zug]]', '[[Kurven, Innenausschnitte]]']], h=7, widths=[22, 26, 52]),
    ]),
    ('laubsaege', [
        A('Beschreibe, wie man einen Innenausschnitt mit der Laubsäge sägt.', 3, 'Zuerst im Ausschnitt ein Loch bohren. Sägeblatt oben ausspannen, durch das Loch führen, mit den Zähnen nach unten (zum Griff) wieder einspannen. Dann senkrecht neben der Linie sägen.'),
    ]),
    ('feilen', [
        GL('Ordne von grob nach fein.', ['Raspel → [[Feile]] → [[Schleifpapier]]', 'K 240, K 80, K 120 → [[K 80]] → [[K 120]] → [[K 240]]']),
    ]),
]),

'04_Messen_Anreissen': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne einen Messschieber, der 23,4 mm anzeigt, und beschrifte Hauptskala und Nonius.',
    sections=[
    ('werkzeuge', [
        ZU('Ordne die Werkzeuge zu.', ['Stahlmaßstab', 'Anschlagwinkel', 'Streichmaß', 'Messschieber'],
           ['Maße auf 0,1 mm genau', 'Längen messen', 'Parallelen zur Kante', 'rechte Winkel anreißen'], loes=[4, 1, 3, 2]),
    ]),
    ('messschieber', [
        A('Beschreibe, wie man den Messschieber abliest.', 2, 'Ganze Millimeter auf der Hauptskala links von der Nonius-Null ablesen. Dann den Nonius-Strich suchen, der sich mit einem Strich der Hauptskala deckt – er gibt die Zehntelmillimeter an.'),
    ]),
    ('training', [
        TAB('Lies die Werte ab.', ['Hauptskala vor der Null', 'deckender Nonius-Strich', 'Messwert'], [['17 mm', '6', '[[17,6 mm]]'], ['42 mm', '3', '[[42,3 mm]]'], ['8 mm', '9', '[[8,9 mm]]']], h=7),
    ]),
    ('anreissen', [
        A('Erkläre, warum man beim Anreißen von einer Bezugskante aus misst.', 2, 'Alle Maße beziehen sich auf dieselbe gerade Kante. So addieren sich Messfehler nicht und die Linien werden rechtwinklig und parallel.'),
    ]),
]),

'05_Bohren': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne die Tischbohrmaschine und beschrifte mindestens acht Bauteile.',
    sections=[
    ('aufbau', [
        ZU('Ordne die Bauteile ihren Aufgaben zu.', ['Bohrfutter', 'Vorschubhebel', 'Tiefenanschlag', 'NOT-AUS', 'Maschinenschraubstock'],
           ['stoppt sofort', 'spannt das Werkstück', 'hält den Bohrer', 'begrenzt die Bohrtiefe', 'bewegt den Bohrer nach unten'], loes=[4, 5, 3, 1, 2]),
    ]),
    ('bohrer', [
        TAB('Welcher Bohrer passt?', ['Aufgabe', 'Bohrer'], [['Loch in ein Brett bohren', '[[Holzspiralbohrer]]'], ['großes, flaches Loch', '[[Forstnerbohrer]]'], ['Loch in Aluminium', '[[Metallbohrer]]'], ['Bohrloch entgraten', '[[Kegelsenker]]']], h=6, widths=[55, 45]),
    ]),
    ('drehzahl', [
        L('Ein großer Bohrer braucht eine [[kleine]] Drehzahl, ein kleiner Bohrer eine [[große]] Drehzahl. Harte Werkstoffe wie Stahl bohrt man [[langsamer]] als Holz.'),
    ]),
    ('sicher', [
        A('Nenne vier Sicherheitsregeln an der Tischbohrmaschine.', 3, 'Schutzbrille tragen · Haare zusammenbinden · keine Handschuhe · Werkstück spannen · Bohrfutterschlüssel abziehen · Späne erst nach Stillstand mit dem Pinsel entfernen.'),
    ]),
]),

'06_Fuegen_Beschichten': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne eine Schraub- und eine Dübelverbindung im Schnitt.',
    sections=[
    ('arten', [
        SORT('Sortiere die Verbindungen.', ['Schraube', 'Leim', 'Nagel', 'Dübel mit Leim', 'Steckverbindung', 'Heißkleber'], ['lösbar', 'unlösbar'], h=14,
             loes=[['Schraube', 'Steckverbindung'], ['Leim', 'Nagel', 'Dübel mit Leim', 'Heißkleber']]),
    ]),
    ('leimen', [
        A('Beschreibe in vier Schritten, wie man zwei Leisten verleimt.', 3, 'Flächen prüfen · Leim dünn auf beide Flächen · zusammenfügen und mit Zwingen (Zulagen) pressen · ausgetretenen Leim entfernen und trocknen lassen.'),
    ]),
    ('schrauben', [
        A('Begründe, warum man vor dem Schrauben vorbohrt und senkt.', 2, 'Vorbohren verhindert, dass das Holz reißt. Senken sorgt dafür, dass der Schraubenkopf bündig mit der Oberfläche abschließt.'),
    ]),
    ('beschichten', [
        TAB('Ergänze die Tabelle.', ['Beschichtung', 'Eigenschaft'], [['Öl', '[[zieht ein, Maserung betont]]'], ['Lasur', '[[farbig, Maserung sichtbar]]'], ['Lack', '[[harte, geschlossene Schicht]]']], h=6, widths=[30, 70]),
    ]),
]),

'07_Wiederholung': dict(ichkann=True, skip=['quiz-st'], heft_label='Notizen', heft_title='Das muss ich noch üben', heft_sub='Fragen, Merkpunkte, Begriffe',
    sections=[
    ('begriffe', [
        ZU('Ordne die Fachbegriffe zu.', ['Kambium', 'Sperrholz', 'Laubsäge', 'Nonius', 'Zentrierspitze'],
           ['schneidet auf Zug', 'führt den Holzbohrer', 'Wachstumsschicht', 'Zehntelmillimeter ablesen', 'kreuzweise verleimte Furniere'], loes=[3, 5, 1, 4, 2]),
    ]),
    ('t1', [
        SORT('Sortiere.', ['Buche', 'Fichte', 'MDF', 'Eiche', 'Sperrholz', 'Kiefer'], ['Laubholz', 'Nadelholz', 'Holzwerkstoff'], h=14,
             loes=[['Buche', 'Eiche'], ['Fichte', 'Kiefer'], ['MDF', 'Sperrholz']]),
    ]),
    ('t2', [
        GL('Rechne um.', ['35 cm = [[350]] mm', '1,5 m = [[1500]] mm', '84 mm = [[8,4]] cm']),
    ]),
    ('t3', [
        RF(['f|Große Bohrer laufen schnell.|Große Bohrer laufen langsam.', 'r|Schrauben werden vorgebohrt.', 'f|Leim wird dick aufgetragen.|Leim wird dünn aufgetragen.'], fix=False),
    ]),
]),
}
