from render import *

WINKEL = [[0, 0, 0], [1, 0, 0], [2, 0, 0], [0, 0, 1], [0, 1, 0], [1, 1, 0], [2, 1, 0], [0, 1, 1]]
TREPPE = [[0, 0, 0], [1, 0, 0], [2, 0, 0], [0, 0, 1], [1, 0, 1], [0, 0, 2], [0, 1, 0], [1, 1, 0], [2, 1, 0], [0, 1, 1], [1, 1, 1], [0, 1, 2]]
SAEULE = [[0, 0, 0], [1, 0, 0], [2, 0, 0], [0, 1, 0], [1, 1, 0], [2, 1, 0], [2, 1, 1], [2, 1, 2]]
UFORM = [[0, 0, 0], [1, 0, 0], [2, 0, 0], [0, 0, 1], [2, 0, 1], [0, 1, 0], [1, 1, 0], [2, 1, 0], [0, 1, 1], [2, 1, 1]]

PLATTE = ('<svg viewBox="0 0 120 70" style="width:62mm;height:36mm;font-family:Barlow Semi Condensed,sans-serif">'
          '<rect x="10" y="6" width="80" height="44" fill="none" stroke="#111" stroke-width="1.4"/><circle cx="50" cy="28" r="9" fill="none" stroke="#111" stroke-width="1.4"/>'
          '<path d="M36 28h28M50 14v28" stroke="#111" stroke-width=".4" stroke-dasharray="6 1.5 1 1.5"/><path d="M76 6v44" stroke="#111" stroke-width=".6" stroke-dasharray="3 1.5"/>'
          '<path d="M10 52v14M90 52v14M10 62h80M92 6h20M92 50h20M108 6v44" stroke="#111" stroke-width=".4"/>'
          '<text x="50" y="60" text-anchor="middle" font-size="7">80</text><text x="106" y="30" text-anchor="middle" font-size="7" transform="rotate(-90 106 30)">50</text><text x="60" y="20" font-size="6">Ø18</text></svg>')

WS = {
'01_Idee_Planung': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne die Phasen als Ablauf mit Pfeilen.',
    sections=[
    ('phasen', [
        GL('Ergänze die Phasen der Produktentwicklung.', ['Problem erkennen → [[Anforderungen festlegen]] → Ideen skizzieren → [[Lösung auswählen]] → planen → [[fertigen]] → bewerten']),
    ]),
    ('anforderungen', [
        SORT('Sortiere die Anforderungen an einen Handyhalter.', ['Handy steht sicher', 'Kabel passt durch', 'Name eingraviert', 'Fach für Kopfhörer', 'keine scharfen Kanten', 'farbig lackiert'], ['Muss', 'Wunsch'], h=16,
             loes=[['Handy steht sicher', 'Kabel passt durch', 'keine scharfen Kanten'], ['Name eingraviert', 'Fach für Kopfhörer', 'farbig lackiert']]),
    ]),
    ('bewerten', [
        TAB('Bewerte zwei eigene Ideen mit 1–5 Punkten.', ['Anforderung', 'Idee 1', 'Idee 2'], [['Handy steht sicher', '', ''], ['leicht herzustellen', '', ''], ['wenig Material', '', ''], ['sieht gut aus', '', ''], ['**Summe**', '', '']], h=6, widths=[50, 25, 25]),
    ]),
    ('unterlagen', [
        ZU('**M1:** Ordne die Planungsunterlagen zu.', ['technische Zeichnung', 'Stückliste', 'Arbeitsablaufplan'],
           ['Reihenfolge der Arbeitsschritte', 'Form und Maße', 'alle Teile mit Werkstoff und Maßen'], loes=[3, 1, 2]),
    ]),
]),

'02_Linien_Bemassung': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne die vier Linienarten jeweils 5 cm lang und beschrifte sie.',
    sections=[
    ('linien', [
        BILD('Benenne in der Zeichnung: sichtbare Kante, verdeckte Kante, Mittellinie, Maßlinie, Maßhilfslinie, Maßzahl.', PLATTE, n=2,
             loes='Umriss und Bohrung: breite Volllinie (sichtbare Kanten) · senkrechte Strichlinie: verdeckte Kante (Nut) · Strichpunktlinien in der Bohrung: Mittellinien · Linien mit 80 und 50: Maßlinien · senkrechte bzw. waagerechte Verlängerungen: Maßhilfslinien · 80, 50, Ø18: Maßzahlen'),
    ]),
    ('regeln', [
        RF(['r|Maße stehen in mm ohne Einheit.', 'f|Die Maßzahl steht unter der Maßlinie.|Sie steht über der Maßlinie.', 'r|Senkrechte Maße sind von rechts lesbar.', 'f|Maßlinien werden breit gezeichnet.|Maßlinien sind schmale Volllinien.']),
    ]),
    ('ablesen', [
        GL('Berechne mit den Maßen der Platte.', ['Umfang: 2 · (80 + 50) = [[260]] mm', 'Radius der Bohrung: [[9]] mm', 'Fläche ohne Bohrung: 80 · 50 = [[4000]] mm² = [[40]] cm²']),
    ]),
    ('m1', [
        TAB('**M1:** Ergänze die Tabelle zum Maßstab.', ['Maßstab', 'Werkstück', 'Zeichnung'], [['1 : 1', '60 mm', '[[60 mm]]'], ['1 : 2', '120 mm', '[[60 mm]]'], ['2 : 1', '15 mm', '[[30 mm]]'], ['1 : 5', '[[250 mm]]', '50 mm']], h=6),
    ]),
]),

'03_Dreitafelbild': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne die Anordnung der drei Ansichten mit den Beschriftungen Breite, Höhe und Tiefe.',
    sections=[
    ('ansichten', [
        VOX('Zeichne die drei Ansichten des Körpers auf das Karofeld (eine Würfelkante = zwei Kästchen).', WINKEL, h=46),
    ]),
    ('anordnung', [
        TAB('Welche Maße zeigt die Ansicht, wo steht sie?', ['Ansicht', 'zeigt', 'steht'], [['Vorderansicht', '[[Breite und Höhe]]', '[[oben links]]'], ['Draufsicht', '[[Breite und Tiefe]]', '[[unter der Vorderansicht]]'], ['Seitenansicht von links', '[[Tiefe und Höhe]]', '[[rechts neben der Vorderansicht]]']], h=6, widths=[28, 32, 40]),
    ]),
    ('vorhersage', [
        VOX('Zeichne das Dreitafelbild.', SAEULE, h=46),
    ]),
    ('quiz-v', [
        A('Erkläre, warum eine einzige Ansicht oft nicht reicht, um einen Körper eindeutig darzustellen.', 2, 'Eine Ansicht zeigt nur zwei der drei Maße. Verschiedene Körper können von vorn gleich aussehen, erst Draufsicht und Seitenansicht zeigen die Tiefe.'),
    ]),
]),

'04_Raeumlich': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne einen Quader 40 × 20 × 30 mm einmal in Kabinettprojektion und einmal isometrisch.',
    sections=[
    ('vergleich', [
        TAB('Vergleiche die beiden Verfahren.', ['', 'Kabinettprojektion', 'Isometrie'], [['Winkel der Tiefenkanten', '[[45°]]', '[[30°]]'], ['Länge der Tiefenkanten', '[[halbiert]]', '[[wahre Länge]]'], ['Vorderansicht', '[[unverzerrt]]', '[[verzerrt (30°)]]']], h=6, widths=[34, 33, 33]),
    ]),
    ('tiefe', [
        GL('Wie lang zeichnest du die Tiefenkante?', ['Tiefe 60 mm, Kabinettprojektion: [[30]] mm', 'Tiefe 60 mm, Isometrie: [[60]] mm', 'Tiefe 35 mm, Kabinettprojektion: [[17,5]] mm']),
    ]),
    ('schritte', [
        VOX('Zeichne den Körper in Kabinettprojektion auf das Karofeld.', TREPPE, h=44, loes='Vorderfläche (Treppenform) in wahrer Größe, Tiefenkanten unter 45° um eine halbe Würfelkante, Rückflächen verbinden, sichtbare Kanten nachziehen.'),
    ]),
    ('m1', [
        A('**M1:** Nenne einen Vorteil der Isometrie gegenüber der Kabinettprojektion.', 1, 'Alle Kanten haben die wahre Länge; der Körper wirkt natürlicher und unverzerrt.'),
    ]),
]),

'05_Wiederholung': dict(ichkann=True, skip=['quiz-st'], heft_label='Notizen', heft_title='Das muss ich noch üben', heft_sub='Fragen, Merkpunkte, Begriffe',
    sections=[
    ('begriffe', [
        ZU('Ordne die Fachbegriffe zu.', ['Stückliste', 'Strichlinie', 'Draufsicht', 'Kabinettprojektion', 'Maßhilfslinie'],
           ['Tiefe unter 45° halbiert', 'verdeckte Kante', 'verlängert die Kante', 'alle Teile mit Maßen', 'Ansicht von oben'], loes=[4, 2, 5, 1, 3]),
    ]),
    ('t1', [
        GL('Ergänze die Phasen.', ['Problem → Anforderungen → [[Ideen]] → Auswahl → [[Planen]] → Fertigen → [[Bewerten]]']),
    ]),
    ('t2', [
        ZU('Ordne die Linienarten zu.', ['breite Volllinie', 'Strichlinie', 'Strichpunktlinie', 'schmale Volllinie'], ['Mittellinie', 'Maßlinie', 'sichtbare Kante', 'verdeckte Kante'], loes=[3, 4, 1, 2]),
    ]),
    ('t3', [
        VOX('Zeichne das Dreitafelbild.', UFORM, h=40),
    ]),
]),
}
