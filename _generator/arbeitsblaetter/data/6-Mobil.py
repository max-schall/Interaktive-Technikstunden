from render import *

WS = {
'01_Mobil_sein': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne den Gummiflitzer von oben und beschrifte Grundplatte, Achse, Rad, Lager und Gummiband.',
    sections=[
    ('antrieb', [
        SORT('Sortiere die Fahrzeuge nach ihrem Antrieb.', ['Fahrrad', 'Segelboot', 'Lkw', 'E-Scooter', 'Aufziehauto', 'Ruderboot', 'Straßenbahn', 'Gummiflitzer'],
             ['Muskelkraft', 'Wind', 'Kraftstoff', 'Strom', 'gespeichert'], h=16,
             loes=[['Fahrrad', 'Ruderboot'], ['Segelboot'], ['Lkw'], ['E-Scooter', 'Straßenbahn'], ['Aufziehauto', 'Gummiflitzer']]),
    ]),
    ('rollen', [
        L('Beim Schieben bremst die [[Gleitreibung]], beim Rollen die [[Rollreibung]]. Die Rollreibung ist viel [[kleiner]]. Darum haben Fahrzeuge [[Räder]].'),
    ]),
    ('teile', [
        ZU('Ordne die Bauteile ihrer Aufgabe zu.', ['Grundplatte', 'Achse', 'Lager', 'Gummiband'],
           ['speichert Energie und dreht die Achse', 'Bohrung, in der sich die Achse dreht', 'trägt alle anderen Teile', 'Rundstab, auf dem die Räder sitzen'], loes=[4, 3, 1, 2]),
    ]),
    ('lager', [
        A('Erkläre, warum die Lagerbohrung etwas größer sein muss als die Achse – aber nicht viel größer.', 2, 'Ist sie zu eng, klemmt die Achse und dreht sich schwer. Ist sie viel zu weit, wackelt das Rad und das Fahrzeug fährt nicht geradeaus.'),
    ]),
]),

'02_Gummiflitzer': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne den Gummiflitzer von der Seite und markiere, wo die Energie gespeichert wird.',
    sections=[
    ('antrieb', [
        L('Beim Aufwickeln wird das Gummiband gedehnt und speichert [[Spannenergie]]. Beim Loslassen dreht es die [[Achse]]. Die Spannenergie wird zu [[Bewegungsenergie]]. Danach rollt der Flitzer aus, bis die [[Reibung]] ihn stoppt.'),
    ]),
    ('stueck', [
        TAB('Ergänze die Stückliste.', ['Pos.', 'Menge', 'Benennung', 'Werkstoff', 'Maße in mm'],
            [['1', '1', 'Grundplatte', '[[Sperrholz]]', '200 × 80 × 6'], ['2', '[[2]]', 'Lagerleiste', 'Kiefer', '80 × 15 × 15'], ['3', '2', '[[Achse]]', 'Buche', 'Ø 6 × 110'], ['4', '[[4]]', 'Rad', 'Holz', 'Ø 40 × 10']], h=7, widths=[10, 12, 26, 24, 28]),
    ]),
    ('ablauf', [
        A('Bringe in die richtige Reihenfolge: schleifen · bohren · anreißen · Räder aufleimen · sägen. Schreibe die Schritte nummeriert auf.', 2, '1 anreißen · 2 sägen · 3 bohren · 4 schleifen · 5 Räder aufleimen'),
        A('Begründe, warum die Lagerbohrungen parallel liegen müssen.', 1, 'Sonst stehen die Achsen schief und der Flitzer fährt im Kreis.'),
    ]),
    ('werkzeug', [
        ZU('Ordne die Werkzeuge den Arbeitsschritten zu.', ['Anreißen', 'Aussägen', 'Bohren', 'Verbinden'],
           ['Tischbohrmaschine', 'Holzleim und Schraubzwinge', 'Maßstab und Anschlagwinkel', 'Laubsäge'], loes=[3, 4, 1, 2]),
    ]),
]),

'03_Optimieren': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Lege eine Tabelle als Messprotokoll für deine eigenen Fahrten an.',
    sections=[
    ('fair', [
        RF(['r|Nur das Gummiband wird getauscht, alles andere bleibt gleich.', 'f|Räder und Gummiband werden gleichzeitig getauscht.|Nur eine Größe darf geändert werden.', 'f|Nur die beste Fahrt zählt.|Mehrere Fahrten messen und den Mittelwert bilden.']),
    ]),
    ('sim', [
        TAB('Messprotokoll: Trage drei faire Versuche aus dem Simulator ein.', ['Nr.', 'Was habe ich geändert?', 'Strecke'], [['1', '', ''], ['2', '', ''], ['3', '', '']], h=8, widths=[10, 65, 25]),
        A('Welche Änderung hat am meisten gebracht? Begründe.', 2, 'z. B. Strohhalm-Lager mit Wachs: weniger Reibung in den Lagern, oder Gummiring: Räder drehen nicht mehr durch.'),
    ]),
    ('mittel', [
        GL('Berechne den Mittelwert.', ['(3,2 m + 3,6 m + 3,4 m) : 3 = [[3,4 m]]', '(4,1 m + 4,5 m + 4,6 m) : 3 = [[4,4 m]]']),
    ]),
    ('ideen', [
        ZU('Ordne jedem Problem eine Lösung zu.', ['Räder drehen durch', 'Flitzer fährt im Kreis', 'Achse dreht schwer', 'Räder schleifen an der Platte'],
           ['Abstandsscheiben', 'Bohrung glätten, Wachs', 'Gummiring auf die Räder', 'Lager parallel bohren'], loes=[4, 3, 2, 1]),
    ]),
]),

'04_Beurteilen': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Notiere je ein Kriterium zu Funktion, Verarbeitung, Gestaltung und Arbeitsweise für deinen Flitzer.',
    sections=[
    ('kriterien', [
        SORT('Sortiere die Kriterien.', ['fährt geradeaus', 'Kanten entgratet', 'eigene Idee erkennbar', 'Zeitplan eingehalten', 'große Strecke', 'Bohrungen sitzen genau'],
             ['Funktion', 'Verarbeitung', 'Gestaltung', 'Arbeitsweise'], h=14,
             loes=[['fährt geradeaus', 'große Strecke'], ['Kanten entgratet', 'Bohrungen sitzen genau'], ['eigene Idee erkennbar'], ['Zeitplan eingehalten']]),
    ]),
    ('bogen', [
        TAB('Beurteile deinen Flitzer (1–5 Punkte).', ['Kriterium', 'ich', 'Partner/in'], [['fährt geradeaus', '', ''], ['Kanten und Flächen sauber', '', ''], ['Räder laufen rund', '', ''], ['sicher gearbeitet', '', '']], h=7, widths=[60, 20, 20]),
    ]),
    ('rennen', [
        A('Rakete fährt 5,1 m, 3,0 m und 4,8 m, Schnecke 4,4 m, 4,6 m und 4,5 m. Wer gewinnt nach Mittelwert? Rechne.', 3, 'Rakete: 12,9 m : 3 = 4,3 m · Schnecke: 13,5 m : 3 = 4,5 m · Die Schnecke gewinnt, weil sie im Mittel weiter fährt.'),
    ]),
    ('praesent', [
        A('Formuliere ein Feedback nach der Regel „Lob – Frage – Vorschlag“ zu einem Flitzer deiner Klasse.', 3, 'z. B. Lob: Die Räder laufen sehr rund. Frage: Wie habt ihr die Achsen geglättet? Vorschlag: Mit einem Gummiring drehen die Räder beim Start nicht durch.'),
    ]),
]),

'05_Wiederholung': dict(ichkann=True, skip=['quiz-st'], heft_label='Notizen', heft_title='Das muss ich noch üben', heft_sub='Fragen, Merkpunkte, Begriffe',
    sections=[
    ('begriffe', [
        ZU('Ordne die Fachbegriffe zu.', ['Rollreibung', 'Lager', 'Spannenergie', 'fairer Versuch', 'Mittelwert'],
           ['Summe durch Anzahl', 'im gedehnten Gummiband gespeichert', 'nur eine Größe ändern', 'bremst beim Rollen, klein', 'Bohrung, in der sich die Achse dreht'], loes=[5, 3, 4, 1, 2]),
    ]),
    ('t1', [
        A('Nenne zwei Möglichkeiten, die Reibung im Lager zu verringern.', 1, 'Bohrung und Achse glätten · Wachs auftragen · Strohhalm als Lager'),
    ]),
    ('t2', [
        L('Aufwickeln: Das Gummiband speichert [[Spannenergie]]. Loslassen: Sie wird zu [[Bewegungsenergie]].'),
    ]),
    ('t3', [
        GL('Berechne den Mittelwert.', ['(2,8 m + 3,1 m + 3,4 m) : 3 = [[3,1 m]]']),
    ]),
]),
}
