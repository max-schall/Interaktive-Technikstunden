from render import *

WS = {
'01_Kunststoffe': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne die Molekülstruktur der drei Kunststoffgruppen als Modell.',
    sections=[
    ('herkunft', [
        L('Kunststoffe werden meist aus [[Erdöl]] hergestellt. Kleine Bausteine heißen [[Monomere]], die langen Ketten heißen [[Polymere]].'),
    ]),
    ('modell', [
        BOXES('Zeichne die Struktur der drei Gruppen.', ['Thermoplast', 'Duroplast', 'Elastomer'], 32, loes=['lange, unverbundene Ketten', 'eng vernetztes Netz', 'weitmaschig vernetzte Knäuel']),
        TAB('Wie verhalten sie sich?', ['Gruppe', 'beim Erwärmen', 'Beispiel'], [['Thermoplast', '[[wird weich, schmilzt]]', '[[PET-Flasche]]'], ['Duroplast', '[[bleibt hart, zersetzt sich]]', '[[Steckdose]]'], ['Elastomer', '[[bleibt elastisch]]', '[[Reifen]]']], h=6, widths=[24, 40, 36]),
    ]),
    ('produkte', [
        SORT('Sortiere.', ['Gießkanne', 'Pfannengriff', 'Gummiband', 'Acrylglas', 'Dichtung', 'Leiterplatte'], ['Thermoplast', 'Duroplast', 'Elastomer'], h=12,
             loes=[['Gießkanne', 'Acrylglas'], ['Pfannengriff', 'Leiterplatte'], ['Gummiband', 'Dichtung']]),
    ]),
    ('m1', [
        A('**M1:** Erkläre den Unterschied zwischen „biobasiert“ und „biologisch abbaubar“.', 2, 'Biobasiert: aus Pflanzen hergestellt (kann trotzdem dauerhaft sein). Biologisch abbaubar: zersetzt sich unter bestimmten Bedingungen – unabhängig vom Rohstoff.'),
    ]),
]),

'02_Bearbeiten': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und skizziere eine Spritzgießmaschine mit Trichter, Schnecke und Form.',
    sections=[
    ('werkstatt', [
        TAB('Wie bearbeitet man Acrylglas?', ['Arbeitsschritt', 'So geht es richtig'], [['Trennen', '[[ritzen und brechen oder fein sägen]]'], ['Bohren', '[[Metallbohrer, geringe Drehzahl, Unterlage]]'], ['Kanten', '[[feilen, nass schleifen, polieren]]']], h=7, widths=[25, 75]),
    ]),
    ('biegen', [
        A('Beschreibe, wie man einen Acrylglasstreifen um 90° biegt.', 3, 'Biegelinie anzeichnen, über dem Heizdraht auf ca. 160 °C erwärmen, mit Handschuhen um eine Schablone biegen und in Form abkühlen lassen.'),
    ]),
    ('industrie', [
        ZU('Ordne Verfahren und Produkt zu.', ['Spritzgießen', 'Extrudieren', 'Blasformen', 'Tiefziehen'], ['Rohr', 'Joghurtbecher', 'Legostein', 'Flasche'], loes=[2, 4, 1, 3]),
    ]),
    ('spritz', [
        GL('**M1:** Ergänze die Schritte beim Spritzgießen.', ['Granulat einfüllen → [[schmelzen (plastifizieren)]] → [[einspritzen]] → abkühlen → [[entformen]]']),
    ]),
]),

'03_Recycling': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne die Abfallhierarchie als Pyramide.',
    sections=[
    ('codes', [
        TAB('Ergänze die Recycling-Codes.', ['Code', 'Kurzzeichen', 'Beispiel'], [['1', '[[PET]]', '[[Getränkeflasche]]'], ['2', 'PE-HD', '[[Shampooflasche]]'], ['5', '[[PP]]', '[[Brotdose]]'], ['6', 'PS', '[[Styropor]]']], h=6),
    ]),
    ('wege', [
        ZU('Ordne die Verwertungswege zu.', ['werkstofflich', 'rohstofflich', 'energetisch'], ['Kunststoff wird zu Öl oder Gas', 'Kunststoff wird verbrannt, die Wärme genutzt', 'Kunststoff wird zu neuem Granulat'], loes=[2, 3, 1]),
    ]),
    ('mikro', [
        A('**M1:** Nenne zwei Quellen für Mikroplastik und eine Möglichkeit, es zu verringern.', 2, 'Reifenabrieb, Fasern aus Fleece-Kleidung, zerfallender Plastikmüll · Weniger Auto fahren, Waschbeutel nutzen, Müll richtig entsorgen.'),
    ]),
    ('vermeiden', [
        GL('Ordne von gut nach schlecht.', ['[[Vermeiden]] → [[Wiederverwenden]] → Recyceln → [[Verbrennen]] → Deponie']),
    ]),
]),

'04_Fertigungsverfahren': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und ergänze zu jeder Hauptgruppe zwei eigene Beispiele aus der Werkstatt.',
    sections=[
    ('gruppen', [
        GL('Ergänze die sechs Hauptgruppen nach DIN 8580.', ['1 [[Urformen]] · 2 [[Umformen]] · 3 [[Trennen]] · 4 [[Fügen]] · 5 [[Beschichten]] · 6 [[Stoffeigenschaft ändern]]']),
    ]),
    ('sortieren', [
        SORT('Sortiere die Verfahren.', ['Sägen', '3D-Druck', 'Biegen', 'Kleben', 'Lackieren', 'Härten', 'Bohren', 'Walzen', 'Gießen', 'Nieten'], ['Urformen', 'Umformen', 'Trennen', 'Fügen', 'Beschichten', 'Stoffeig. ändern'], h=16,
             loes=[['3D-Druck', 'Gießen'], ['Biegen', 'Walzen'], ['Sägen', 'Bohren'], ['Kleben', 'Nieten'], ['Lackieren'], ['Härten']]),
    ]),
    ('lebenslauf', [
        A('**M1:** Ein Schraubendreher wird gegossen, gewalzt, geschliffen, gehärtet und verchromt. Ordne jedem Schritt die Hauptgruppe zu.', 2, 'Gießen: Urformen · Walzen: Umformen · Schleifen: Trennen · Härten: Stoffeigenschaft ändern · Verchromen: Beschichten'),
    ]),
]),

'05_Werkstoffpruefung': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und erstelle ein Versuchsprotokoll zum Biegeversuch.',
    sections=[
    ('eigenschaften', [
        ZU('Ordne die Eigenschaften zu.', ['Härte', 'Elastizität', 'Dichte', 'Festigkeit'], ['Masse pro Volumen', 'geht in die alte Form zurück', 'Widerstand gegen Eindringen', 'Widerstand gegen Brechen'], loes=[3, 2, 4, 1]),
    ]),
    ('experiment', [
        GL('Ergänze die Schritte eines technischen Experiments.', ['Frage → [[Vermutung]] → [[Planung]] → Durchführung → [[Beobachtung]] → Auswertung']),
        A('Erkläre, warum man bei einem Experiment nur eine Größe verändert.', 1, 'Nur so weiß man, welche Größe das Ergebnis verursacht hat.'),
    ]),
    ('biege', [
        TAB('Biegeversuch bei 500 g – trage deine Werte ein.', ['Werkstoff', 'Durchbiegung', 'Beobachtung'], [['Fichte', '', ''], ['Aluminium', '', ''], ['Stahl', '', ''], ['Acrylglas', '', ''], ['PE', '', '']], h=6),
    ]),
    ('ritz', [
        GL('Ordne nach der Härte (weich → hart).', ['Glas, Wachs, Kupfer, Holz → [[Wachs]] → [[Holz]] → [[Kupfer]] → [[Glas]]']),
    ]),
]),

'06_Wiederholung': dict(ichkann=True, skip=['quiz-st'], heft_label='Notizen', heft_title='Das muss ich noch üben', heft_sub='Fragen, Merkpunkte, Begriffe',
    sections=[
    ('begriffe', [
        ZU('Ordne die Fachbegriffe zu.', ['Polymer', 'Thermoplast', 'Extrudieren', 'Urformen', 'Härte'],
           ['Widerstand gegen Eindringen', 'wird beim Erwärmen weich', 'lange Molekülkette', 'Rohre und Profile herstellen', 'aus formlosem Stoff ein Körper'], loes=[3, 2, 4, 5, 1]),
    ]),
    ('t1', [
        SORT('Sortiere.', ['PET-Flasche', 'Steckdose', 'Reifen', 'Acrylglas', 'Pfannengriff', 'Gummiband'], ['Thermoplast', 'Duroplast', 'Elastomer'], h=12,
             loes=[['PET-Flasche', 'Acrylglas'], ['Steckdose', 'Pfannengriff'], ['Reifen', 'Gummiband']]),
    ]),
    ('t2', [
        RF(['r|Biegen ist Umformen.', 'f|3D-Druck ist Trennen.|3D-Druck ist Urformen.', 'r|Härten ändert die Stoffeigenschaft.'], fix=False),
    ]),
    ('t3', [
        A('Nenne die drei Verwertungswege für Kunststoff.', 1, 'werkstofflich, rohstofflich, energetisch'),
    ]),
]),
}
