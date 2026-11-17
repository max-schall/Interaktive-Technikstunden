from render import *

WS = {
'01_Energie': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne die Energiekette Primär- → End- → Nutzenergie an einem eigenen Beispiel.',
    sections=[
    ('traeger', [
        SORT('Sortiere die Energieträger.', ['Braunkohle', 'Wind', 'Erdgas', 'Uran', 'Sonne', 'Biogas', 'Erdöl', 'Erdwärme'], ['fossil', 'nuklear', 'erneuerbar'], h=14,
             loes=[['Braunkohle', 'Erdgas', 'Erdöl'], ['Uran'], ['Wind', 'Sonne', 'Biogas', 'Erdwärme']]),
    ]),
    ('kette', [
        TAB('Primär-, End- oder Nutzenergie?', ['Beispiel', 'Energieart'], [['Rohöl im Boden', '[[Primärenergie]]'], ['Benzin an der Tankstelle', '[[Endenergie]]'], ['Bewegung des Autos', '[[Nutzenergie]]'], ['Strom aus der Steckdose', '[[Endenergie]]']], h=6, widths=[60, 40]),
    ]),
    ('mix', [
        A('Beschreibe, wie sich der Anteil erneuerbarer Energien am Strom seit 2000 entwickelt hat, und nenne einen Grund.', 2, 'Er ist von etwa 6 % auf über die Hälfte gestiegen – durch den Ausbau von Wind- und Solaranlagen und die Förderung erneuerbarer Energien.'),
    ]),
    ('einheiten', [
        GL('Rechne um.', ['2 kWh = [[7,2]] MJ', '18 MJ = [[5]] kWh', 'Föhn 2000 W, 30 min: E = [[1]] kWh']),
    ]),
]),

'02_Kraftwerke': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne das Schema eines Wärmekraftwerks mit Kessel, Turbine, Generator, Kondensator und Kühlturm.',
    sections=[
    ('generator', [
        L('Dreht sich ein [[Magnet]] in einer [[Spule]], entsteht eine Spannung. Das nennt man [[Induktion]]. Je [[schneller]] die Drehung, desto größer die Spannung.'),
    ]),
    ('kraftwerk', [
        GL('Ergänze den Ablauf im Wärmekraftwerk.', ['Brennstoff → [[Kessel]] (Dampf) → [[Turbine]] → [[Generator]] → Strom', 'Dampf → [[Kondensator]] → Wasser zurück in den Kessel; Abwärme → [[Kühlturm]]']),
        BOX('Zeichne das Schema eines Wärmekraftwerks mit Pfeilen für Dampf, Wasser und Strom.', 46, loes='Kessel → Dampfleitung → Turbine → Welle → Generator → Strom; Turbine → Kondensator → Speisewasser zurück zum Kessel; Kondensator ↔ Kühlturm.'),
    ]),
    ('kwk', [
        A('Erkläre, wie Kraft-Wärme-Kopplung den Wirkungsgrad erhöht.', 2, 'Die Abwärme wird nicht über den Kühlturm abgegeben, sondern als Fernwärme zum Heizen genutzt. So werden bis zu 85 % statt etwa 40 % der Brennstoffenergie genutzt.'),
    ]),
    ('ablauf', [
        GL('**M1:** Ergänze die Energieformen.', ['[[chemische]] Energie (Kohle) → [[thermische]] Energie (Dampf) → [[Bewegungs]]energie (Turbine) → [[elektrische]] Energie']),
    ]),
]),

'03_Wind_Wasser': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne ein Windrad und beschrifte Rotor, Gondel mit Generator, Turm und Fundament.',
    sections=[
    ('windrad', [
        ZU('Ordne die Bauteile zu.', ['Rotor', 'Gondel', 'Turm', 'Windmesser'], ['enthält Getriebe und Generator', 'misst Windrichtung und -stärke', 'wird vom Wind gedreht', 'bringt den Rotor in große Höhe'], loes=[3, 1, 4, 2]),
    ]),
    ('leistung', [
        A('Erkläre, warum ein Windrad bei 6 m/s nur etwa ein Achtel der Leistung von 12 m/s liefert.', 2, 'Die Leistung des Windes wächst mit der dritten Potenz der Geschwindigkeit: halbe Geschwindigkeit → (1/2)³ = 1/8 der Leistung.'),
    ]),
    ('wasser', [
        TAB('Wasserkraftwerke', ['Art', 'Funktion'], [['Laufwasserkraftwerk', '[[Fluss, läuft rund um die Uhr]]'], ['Speicherkraftwerk', '[[Stausee, Wasser fällt ins Tal]]'], ['Pumpspeicherkraftwerk', '[[pumpt bei Überschuss hoch, speichert]]']], h=7, widths=[35, 65]),
    ]),
    ('bewerten', [
        A('**M1:** Nenne je zwei Vor- und Nachteile der Windenergie.', 2, 'Vorteile: kein CO₂ im Betrieb, kostenloser „Brennstoff“, Flächen weiter nutzbar · Nachteile: schwankende Erzeugung, Landschaftsbild, Gefahr für Vögel, Lärm'),
    ]),
]),

'04_Sonne': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Skizziere den Tagesverlauf der Leistung einer Süd-Solaranlage.',
    sections=[
    ('pv', [
        L('Solarzellen wandeln [[Licht]] direkt in elektrische Energie um. Sie liefern [[Gleichstrom]]. Der [[Wechselrichter]] wandelt ihn in Wechselstrom um.'),
        BOX('Skizziere den Tagesverlauf der Leistung einer Südanlage an einem sonnigen Tag.', 30, loes='Glockenkurve: ab Sonnenaufgang ansteigend, Maximum mittags um 13 Uhr, abends wieder auf null.'),
    ]),
    ('thermie', [
        SORT('Photovoltaik oder Solarthermie?', ['liefert Strom', 'erwärmt Wasser', 'Wechselrichter', 'Kollektor mit Rohren', 'Silizium'], ['Photovoltaik', 'Solarthermie'], h=12,
             loes=[['liefert Strom', 'Wechselrichter', 'Silizium'], ['erwärmt Wasser', 'Kollektor mit Rohren']]),
    ]),
    ('balkon', [
        GL('Balkonkraftwerk: 400 €, 700 kWh/Jahr, 70 % selbst genutzt, 35 ct/kWh.', ['selbst genutzt: [[490]] kWh', 'Ersparnis: [[171,50]] € pro Jahr', 'bezahlt nach etwa [[2,3]] Jahren']),
    ]),
    ('weitere', [
        A('**M1:** Warum sind Biomasse und Erdwärme eine gute Ergänzung zu Sonne und Wind?', 1, 'Sie liefern Energie unabhängig von Tageszeit und Wetter, auch nachts und bei Windstille.'),
    ]),
]),

'05_Speicher_Netz': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne den Tagesverlauf von Verbrauch und Solarstrom und markiere Überschuss und Lücke.',
    sections=[
    ('tag', [
        A('Beschreibe das Problem, das an einem sonnigen Tag im Stromnetz entsteht.', 2, 'Mittags liefern Solaranlagen mehr Strom als gebraucht wird (Überschuss), abends ist der Verbrauch hoch, aber es gibt keinen Solarstrom (Lücke). Erzeugung und Verbrauch müssen aber immer gleich sein.'),
    ]),
    ('speicher', [
        ZU('Ordne die Speicher zu.', ['Akku', 'Pumpspeicher', 'Wasserstoff', 'Wärmespeicher'], ['monatelang lagerbar', 'heißes Wasser im Tank', 'chemisch, schnell, für Stunden', 'Wasser wird hochgepumpt'], loes=[3, 4, 1, 2]),
    ]),
    ('smart', [
        SORT('Wann sinnvoll?', ['E-Auto laden', 'Speicher entladen', 'Waschmaschine starten', 'Gaskraftwerk einschalten', 'Wärmepumpe heizt vor'], ['mittags (viel Sonne)', 'abends (wenig Sonne)'], h=12,
             loes=[['E-Auto laden', 'Waschmaschine starten', 'Wärmepumpe heizt vor'], ['Speicher entladen', 'Gaskraftwerk einschalten']]),
    ]),
    ('m1', [
        A('**M1:** Erkläre, was ein Smart Grid ist.', 2, 'Ein digital vernetztes Stromnetz: Erzeuger, Speicher und Verbraucher tauschen Daten aus. Geräte laufen bevorzugt, wenn viel erneuerbarer Strom verfügbar ist.'),
    ]),
]),

'06_Wiederholung': dict(ichkann=True, skip=['quiz-st'], heft_label='Notizen', heft_title='Das muss ich noch üben', heft_sub='Fragen, Merkpunkte, Formeln',
    sections=[
    ('begriffe', [
        ZU('Ordne die Fachbegriffe zu.', ['Induktion', 'Kühlturm', 'Wechselrichter', 'Pumpspeicher', 'Smart Grid'],
           ['vernetztes Stromnetz', 'gibt Abwärme ab', 'Wasser hochpumpen', 'Magnet in Spule erzeugt Spannung', 'Gleichstrom → Wechselstrom'], loes=[4, 2, 5, 3, 1]),
    ]),
    ('t1', [
        SORT('Sortiere.', ['Kohle', 'Wind', 'Erdgas', 'Sonne', 'Biogas'], ['fossil', 'erneuerbar'], h=12, loes=[['Kohle', 'Erdgas'], ['Wind', 'Sonne', 'Biogas']]),
    ]),
    ('t2', [
        GL('Rechne.', ['5 kWh = [[18]] MJ', '3000 W für 2 h: [[6]] kWh']),
    ]),
    ('t3', [
        GL('Ergänze.', ['Kessel → [[Turbine]] → [[Generator]] → Strom']),
    ]),
]),
}
