from render import *

WS = {
'01_Baugruppen': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne das Schema Antrieb → Übertragung → Arbeitseinheit mit Steuerung und Gestell für den Akkuschrauber.',
    sections=[
    ('akku', [
        TAB('Ordne die Teile des Akkuschraubers den Baugruppen zu.', ['Teil', 'Baugruppe'], [['Elektromotor', '[[Antrieb]]'], ['Planetengetriebe', '[[Übertragung]]'], ['Bohrfutter mit Bit', '[[Arbeitseinheit]]'], ['Schalter', '[[Steuerung]]'], ['Gehäuse', '[[Gestell]]']], h=6, widths=[50, 50]),
    ]),
    ('baugruppen', [
        A('Beschreibe die Aufgabe der Übertragung am Beispiel des Fahrrads.', 2, 'Kette und Zahnräder übertragen die Drehbewegung von den Pedalen (Antrieb) auf das Hinterrad (Arbeitseinheit) und verändern dabei Drehzahl und Kraft.'),
    ]),
    ('elemente', [
        SORT('Sortiere die Maschinenelemente.', ['Schraube', 'Kugellager', 'Zahnrad', 'Feder', 'Welle', 'Stift', 'Riemen', 'Stoßdämpfer'], ['Verbinden', 'Lagern', 'Übertragen', 'Federn'], h=14,
             loes=[['Schraube', 'Stift'], ['Kugellager'], ['Zahnrad', 'Welle', 'Riemen'], ['Feder', 'Stoßdämpfer']]),
        A('Erkläre den Unterschied zwischen Welle und Achse.', 1, 'Eine Welle dreht sich und überträgt ein Drehmoment; eine Achse trägt nur und überträgt kein Drehmoment.'),
    ]),
    ('demontage', [
        A('**M1:** Warum legt man bei der Demontage ein Protokoll an?', 1, 'Damit man die Teile beim Zusammenbau in der richtigen Reihenfolge und Lage wieder einbauen kann.'),
    ]),
]),

'02_Zahnradgetriebe': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne ein Zahnradgetriebe mit Zwischenrad und markiere die Drehrichtungen mit Pfeilen.',
    sections=[
    ('getriebe', [
        L('Zwei Zahnräder drehen sich [[gegensinnig]]. Ein Zwischenrad ändert die [[Drehrichtung]], aber nicht die [[Übersetzung]].'),
        BOX('Zeichne ein Getriebe aus Antriebsrad (12 Zähne), Zwischenrad und Abtriebsrad (36 Zähne). Markiere alle Drehrichtungen mit Pfeilen.', 34, loes='Antrieb und Abtrieb drehen gleichsinnig, das Zwischenrad gegensinnig; i = 36 : 12 = 3.'),
    ]),
    ('formel', [
        TAB('Ins Langsame oder ins Schnelle?', ['z₁', 'z₂', 'i', 'Art'], [['12', '36', '[[3]]', '[[ins Langsame]]'], ['40', '20', '[[0,5]]', '[[ins Schnelle]]'], ['15', '45', '[[3]]', '[[ins Langsame]]']], h=6),
    ]),
    ('rechnen', [
        GL('Berechne i = z₂ : z₁ und n₂ = n₁ : i.', ['z₁ = 10, z₂ = 30, n₁ = 900 1/min → i = [[3]], n₂ = [[300]] 1/min', 'z₁ = 48, z₂ = 16, n₁ = 60 1/min → i = [[0,33]], n₂ = [[180]] 1/min']),
    ]),
    ('richtung', [
        A('**M1:** Fünf Zahnräder greifen in einer Reihe. Das erste dreht im Uhrzeigersinn. Wie dreht das letzte? Begründe.', 1, 'Im Uhrzeigersinn – jedes Rad kehrt die Richtung um; bei ungerader Anzahl dreht das letzte wie das erste.'),
    ]),
]),

'03_Riemen_Kette': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Berechne für dein Fahrrad die Strecke pro Kurbelumdrehung im leichtesten und im schwersten Gang.',
    sections=[
    ('riemen', [
        GL('Riemengetriebe: Berechne.', ['d₁ = 50 mm, d₂ = 150 mm → i = [[3]]', 'n₁ = 1500 1/min → n₂ = [[500]] 1/min']),
    ]),
    ('kette', [
        TAB('Riemen oder Kette?', ['Eigenschaft', 'Riemen', 'Kette'], [['Schlupf', '[[möglich]]', '[[keiner]]'], ['Geräusch', '[[leise]]', '[[lauter]]'], ['Wartung', '[[wenig]]', '[[schmieren]]'], ['Beispiel', '[[Waschmaschine]]', '[[Fahrrad]]']], h=6),
    ]),
    ('fahrrad', [
        A('Erkläre, warum man bergauf ein kleines Kettenblatt und ein großes Ritzel wählt.', 2, 'Die Übersetzung wird kleiner: Das Hinterrad dreht sich pro Kurbelumdrehung weniger oft. Man fährt langsamer, braucht aber weniger Kraft.'),
    ]),
    ('rechnen', [
        GL('Fahrrad mit Radumfang 2,1 m.', ['Kettenblatt 42, Ritzel 14 → [[3]] Radumdrehungen → [[6,3]] m pro Kurbelumdrehung', 'Kettenblatt 34, Ritzel 34 → [[1]] Radumdrehung → [[2,1]] m']),
    ]),
]),

'04_Energiewandler': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne das Energieflussbild eines Benzinmotors mit Nutzen und Verlusten.',
    sections=[
    ('formen', [
        TAB('Ergänze die Energieumwandlung.', ['Wandler', 'zugeführt', 'genutzt'], [['Elektromotor', '[[elektrische E.]]', '[[Bewegungsenergie]]'], ['Generator', '[[Bewegungsenergie]]', '[[elektrische E.]]'], ['Solarzelle', '[[Strahlung]]', '[[elektrische E.]]'], ['Wasserkocher', '[[elektrische E.]]', '[[Wärme]]']], h=6),
    ]),
    ('fluss', [
        BOX('Zeichne das Energieflussbild einer LED-Lampe (40 % Licht, 60 % Wärme).', 34, loes='Breiter Eingangspfeil 100 %, schmalerer grüner Pfeil 40 % Licht geradeaus, breiterer roter Pfeil 60 % Wärme nach unten.'),
    ]),
    ('eta', [
        GL('Berechne den Wirkungsgrad η = genutzt : zugeführt.', ['zugeführt 500 J, genutzt 450 J → η = [[90]] %', 'zugeführt 2000 J, genutzt 600 J → η = [[30]] %', 'zugeführt 800 J, η = 25 % → genutzt [[200]] J']),
    ]),
    ('kette', [
        A('**M1:** Kraftwerk 40 %, Leitung 95 %, Motor 90 %. Berechne den Gesamtwirkungsgrad.', 1, '0,40 · 0,95 · 0,90 ≈ 0,34 = 34 %'),
    ]),
]),

'05_Motoren': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne die vier Takte als kleine Skizzen mit Ventilstellung und Kolbenrichtung.',
    sections=[
    ('viertakt', [
        TAB('Ergänze die vier Takte.', ['Takt', 'Kolben', 'Einlass', 'Auslass'], [['1. [[Ansaugen]]', '[[nach unten]]', '[[offen]]', '[[zu]]'], ['2. [[Verdichten]]', '[[nach oben]]', '[[zu]]', '[[zu]]'], ['3. [[Arbeiten]]', '[[nach unten]]', '[[zu]]', '[[zu]]'], ['4. [[Ausstoßen]]', '[[nach oben]]', '[[zu]]', '[[offen]]']], h=6),
    ]),
    ('teile', [
        ZU('Ordne zu.', ['Kolben', 'Pleuel', 'Kurbelwelle', 'Zündkerze'], ['zündet das Gemisch', 'wandelt Auf und Ab in Drehung', 'wird vom Gas nach unten gedrückt', 'verbindet Kolben und Kurbelwelle'], loes=[3, 4, 2, 1]),
    ]),
    ('emotor', [
        A('Erkläre die Aufgabe des Kommutators im Elektromotor.', 2, 'Er polt den Strom in der Spule jede halbe Umdrehung um. Dadurch tauschen die Pole der Spule, und sie wird weiter angezogen und abgestoßen – die Drehung hört nicht auf.'),
    ]),
    ('vergleich', [
        A('**M1:** Nenne je zwei Vorteile von Elektromotor und Verbrennungsmotor im Auto.', 2, 'Elektro: hoher Wirkungsgrad, leise, keine Abgase vor Ort, Energierückgewinnung · Verbrenner: große Reichweite, schnell getankt, ausgebautes Tankstellennetz'),
    ]),
]),

'06_Mobilitaet': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Berechne das CO₂ deines Schulwegs pro Woche für zwei Verkehrsmittel.',
    sections=[
    ('antriebe', [
        ZU('Ordne die Antriebe zu.', ['Hybrid', 'Elektroauto', 'Brennstoffzelle', 'Diesel'], ['Selbstzündung', 'Wasserstoff wird zu Strom', 'Verbrenner + Elektromotor', 'Akku und Elektromotor'], loes=[3, 4, 2, 1]),
    ]),
    ('vergleich', [
        GL('Schulweg 6 km einfach, 5 Tage (Werte pro Personenkilometer).', ['Strecke pro Woche: [[60]] km', 'Pkw (165 g/km): [[9,9]] kg CO₂', 'Bus (80 g/km): [[4,8]] kg CO₂', 'Fahrrad: [[0]] kg CO₂']),
    ]),
    ('sicherheit', [
        SORT('Sortiere die Sicherheitssysteme.', ['ABS', 'Airbag', 'Gurt', 'ESP', 'Knautschzone', 'Notbremsassistent'], ['aktive Sicherheit', 'passive Sicherheit'], h=14,
             loes=[['ABS', 'ESP', 'Notbremsassistent'], ['Airbag', 'Gurt', 'Knautschzone']]),
    ]),
    ('m1', [
        A('**M1:** Wann ist ein Elektroauto wirklich klimafreundlich? Begründe.', 2, 'Wenn der Strom aus erneuerbaren Energien stammt und das Auto lange genutzt wird, sodass die Emissionen der Akkuherstellung ausgeglichen werden.'),
    ]),
]),

'07_Wiederholung': dict(ichkann=True, skip=['quiz-st'], heft_label='Notizen', heft_title='Das muss ich noch üben', heft_sub='Fragen, Merkpunkte, Formeln',
    sections=[
    ('begriffe', [
        ZU('Ordne die Fachbegriffe zu.', ['Welle', 'Zwischenrad', 'Wirkungsgrad', 'Kommutator', 'Knautschzone'],
           ['passive Sicherheit', 'überträgt Drehmoment', 'polt den Strom um', 'kehrt die Drehrichtung um', 'genutzt : zugeführt'], loes=[2, 4, 5, 3, 1]),
    ]),
    ('t1', [
        GL('Rechne.', ['z₁ = 20, z₂ = 50, n₁ = 1000 1/min → i = [[2,5]], n₂ = [[400]] 1/min']),
    ]),
    ('t2', [
        GL('Rechne.', ['zugeführt 1000 J, genutzt 250 J → η = [[25]] %']),
    ]),
    ('t3', [
        RF(['r|ABS gehört zur aktiven Sicherheit.', 'f|Der Airbag vermeidet Unfälle.|Er mindert die Folgen (passiv).', 'r|Im Arbeitstakt wird Energie abgegeben.'], fix=False),
    ]),
]),
}
