from render import *

WS = {
'01_Technik_Alltag': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Notiere zu jedem Bereich der Technik ein eigenes Beispiel.',
    sections=[
    ('natur', [
        SORT('Sortiere: Natur oder Technik?', ['Baum', 'Stuhl', 'Vogel', 'Flugzeug', 'Schafwolle', 'Pullover', 'Fluss', 'Brücke', 'Kieselstein', 'Ziegelstein'], ['Natur', 'Technik'], h=18,
             loes=[['Baum', 'Vogel', 'Schafwolle', 'Fluss', 'Kieselstein'], ['Stuhl', 'Flugzeug', 'Pullover', 'Brücke', 'Ziegelstein']]),
    ]),
    ('begriff', [
        L('Technik bedeutet: Menschen [[erfinden]] Gegenstände, [[stellen]] sie [[her]] und [[nutzen]] sie. Erfindungen werden ständig [[verbessert]].'),
        TAB('Welches Bedürfnis erfüllt die Technik?', ['Technik', 'Bedürfnis'], [['Heizung, Fenster', '[[Wohnen]]'], ['Fahrrad, Bus', '[[Mobilität]]'], ['Smartphone', '[[Kommunikation]]'], ['Rauchmelder', '[[Sicherheit]]']], h=6, widths=[50, 50]),
    ]),
    ('bereiche', [
        ZU('Ordne die Beispiele den Bereichen der Technik zu.', ['Bautechnik', 'Maschinenbau', 'Elektrotechnik', 'Medizintechnik'],
           ['Herzschrittmacher', 'Brücke', 'Stromnetz', 'Getriebe'], loes=[4, 1, 3, 2]),
    ]),
    ('m1', [
        A('**M1:** Nenne drei Verbesserungen, die das Boot vom Einbaum bis zur Motoryacht erfahren hat.', 2, 'z. B. größer und stabiler durch Planken, schneller durch Segel und Motor, unabhängig vom Wind durch Dampf- und Motorantrieb, leichter durch Kunststoff.'),
    ]),
]),

'02_Sicherheit': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne zu jeder Art von Sicherheitszeichen ein Beispiel in der richtigen Form und Farbe.',
    sections=[
    ('regeln', [
        RF(['r|Die Jacke bleibt an der Garderobe.', 'f|Späne werden vom Tisch gepustet.|Späne werden abgesaugt.', 'f|Maschinen darf man ausprobieren, wenn die Lehrkraft beschäftigt ist.|Maschinen nur nach Einweisung und mit Erlaubnis benutzen.', 'r|Lange Haare werden zusammengebunden.']),
        A('Begründe, warum man im Technikraum nicht rennen darf.', 1, 'Man kann stolpern und andere anstoßen, die gerade mit spitzen oder scharfen Werkzeugen arbeiten.'),
    ]),
    ('zeichen', [
        TAB('Ergänze die Tabelle der Sicherheitszeichen.', ['Art', 'Form', 'Farbe', 'Bedeutung'], [['Verbot', '[[Kreis mit Balken]]', '[[rot/weiß]]', '[[Das darfst du nicht.]]'], ['Gebot', '[[Kreis]]', '[[blau/weiß]]', '[[Das musst du tun.]]'], ['Warnung', '[[Dreieck]]', '[[gelb/schwarz]]', '[[Achtung, Gefahr!]]'], ['Rettung', '[[Rechteck]]', '[[grün/weiß]]', '[[Hier gibt es Hilfe.]]']], h=7, widths=[18, 24, 20, 38]),
    ]),
    ('sortieren', [
        A('Erkläre, warum an der Bohrmaschine Handschuhe verboten sind.', 1, 'Handschuhe können vom drehenden Bohrer erfasst werden; die Hand wird mitgerissen.'),
    ]),
    ('notfall', [
        A('**M1:** Nenne die Schritte, wenn sich jemand im Technikraum verletzt hat.', 2, 'Ruhe bewahren, Arbeit beenden (ggf. NOT-AUS) · Lehrkraft informieren · Erste Hilfe leisten · bei schweren Verletzungen Notruf 112 · Unfall ins Verbandbuch eintragen.'),
    ]),
]),

'03_Arbeitsplatz': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne die Werkbank und beschrifte Schraubstock, Schutzbacken, Bankzange und Werkzeugablage.',
    sections=[
    ('werkbank', [
        ZU('Ordne die Teile der Werkbank ihren Aufgaben zu.', ['Schraubstock', 'Schutzbacken', 'Bankzange', 'Werkzeugablage'],
           ['schützen das Werkstück vor Abdrücken', 'Platz für die benötigten Werkzeuge', 'spannt Holz, Metall und Kunststoff', 'spannt nur Holz'], loes=[2, 4, 1, 3]),
    ]),
    ('spannen', [
        A('Beschreibe, wie du ein Holzstück zum Sägen richtig einspannst.', 2, 'Im Schraubstock mit Schutzbacken oder in der Bankzange, fest und möglichst kurz über den Backen, die Sägelinie dicht neben den Backen.'),
    ]),
    ('dienste', [
        A('Erkläre, warum es sinnvoll ist, einen Werkzeugdienst einzurichten. Nenne zwei Gründe.', 2, 'Es gibt kein Gedränge am Werkzeugschrank. · Es wird kontrolliert, ob alle Werkzeuge vollständig und unbeschädigt zurückkommen.'),
    ]),
    ('ende', [
        L('Am Stundenende werden die [[Maschinen]] ausgeschaltet, die Werkzeuge [[gereinigt]] und zurückgebracht, das Werkstück [[beschriftet]] und der Arbeitsplatz [[abgesaugt]].', intro='**M1:** Ergänze die Lücken.'),
    ]),
]),

'04_Bionik': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Skizziere deine eigene bionische Erfindung mit Vorbild und Prinzip.',
    sections=[
    ('beispiele', [
        TAB('Ergänze die Tabelle.', ['Vorbild in der Natur', 'Prinzip', 'technische Erfindung'], [['Klette', 'winzige Widerhaken', '[[Klettverschluss]]'], ['Lotusblatt', '[[Wasser perlt ab, nimmt Schmutz mit]]', 'selbstreinigende Farbe'], ['Bienenwabe', '[[stabile Sechsecke]]', '[[Wabenplatte]]']], h=7, widths=[28, 38, 34]),
    ]),
    ('methode', [
        L('Bionik setzt sich aus [[Biologie]] und [[Technik]] zusammen. Zuerst wird ein Vorbild [[beobachtet]], dann das Prinzip verstanden, auf die Technik [[übertragen]] und getestet.'),
    ]),
    ('wabe', [
        A('Erkläre, warum Wabenplatten im Flugzeugbau verwendet werden.', 2, 'Sie sind sehr leicht und trotzdem stabil. Ein leichteres Flugzeug braucht weniger Treibstoff.'),
    ]),
    ('m1', [
        BOX('**M1:** Wähle ein Vorbild und skizziere eine Erfindung. Schreibe das Prinzip dazu.', 40, loes='z. B. Gecko → Haftband ohne Klebstoff; Pinguin → stromlinienförmiges U-Boot; Specht → stoßdämpfender Helm'),
    ]),
]),

'05_Wiederholung': dict(ichkann=True, skip=['quiz-st'], heft_label='Notizen', heft_title='Das muss ich noch üben', heft_sub='Fragen, Merkpunkte, Begriffe',
    sections=[
    ('begriffe', [
        ZU('Ordne die Fachbegriffe zu.', ['Technik', 'NOT-AUS', 'Schutzbacken', 'Bionik', 'Bankzange'],
           ['spannt nur Holz', 'Lösungen der Natur übertragen', 'erfinden, herstellen, nutzen', 'schützen das Werkstück', 'schaltet alle Maschinen ab'], loes=[5, 4, 1, 3, 2]),
    ]),
    ('t1', [
        SORT('Sortiere.', ['Holzbrett', 'Eiche', 'Fahrradhelm', 'Lotusblatt', 'Wabenplatte', 'Ahornsamen'], ['Natur', 'Technik'], h=14,
             loes=[['Eiche', 'Lotusblatt', 'Ahornsamen'], ['Holzbrett', 'Fahrradhelm', 'Wabenplatte']]),
    ]),
    ('t2', [
        BOXES('Zeichne je ein Sicherheitszeichen und beschrifte es.', ['Verbot', 'Gebot', 'Warnung', 'Rettung'], 26, loes=['roter Kreis mit Balken, z. B. Essen verboten', 'blauer Kreis, z. B. Augenschutz', 'gelbes Dreieck, z. B. Spannung', 'grünes Rechteck, z. B. Erste Hilfe']),
    ]),
    ('t3', [
        RF(['f|An der Bohrmaschine trägt man Handschuhe.|Handschuhe sind dort verboten.', 'r|Beschädigtes Werkzeug wird gemeldet.', 'f|Metall wird in der Bankzange gespannt.|Metall gehört in den Schraubstock.'], fix=False),
    ]),
]),
}
