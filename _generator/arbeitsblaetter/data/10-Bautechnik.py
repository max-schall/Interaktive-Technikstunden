from render import *

WS = {
'01_Bauen': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Skizziere je ein Haus in Massivbau und in Skelettbau und markiere, was trägt.',
    sections=[
    ('bauweisen', [
        TAB('Vergleiche die Bauweisen.', ['Bauweise', 'Was trägt?', 'Beispiel'], [['Massivbau', '[[die Wände]]', '[[Ziegelhaus]]'], ['Skelettbau', '[[Stützen und Träger]]', '[[Hochhaus, Fachwerkhaus]]'], ['Fertigbau', '[[vorgefertigte Elemente]]', '[[Holz-Fertighaus]]']], h=6),
    ]),
    ('baustoffe', [
        L('Beton besteht aus [[Zement]], Sand, Kies und [[Wasser]]. Er ist sehr [[druckfest]], aber wenig zugfest. Im [[Stahlbeton]] nimmt eingelegter Stahl die Zugkräfte auf.'),
    ]),
    ('beton', [
        GL('Mischung 1 : 4, Wasser = Zement : 2.', ['3 Eimer Zement → [[12]] Eimer Sand/Kies, [[1,5]] Eimer Wasser', '20 Eimer Sand/Kies → [[5]] Eimer Zement, [[2,5]] Eimer Wasser']),
        A('Erkläre, warum man Stahlbeton statt reinem Beton für eine Decke verwendet.', 2, 'Eine Decke wird auf Biegung belastet; unten entsteht Zug. Beton reißt unter Zug, der eingelegte Stahl nimmt die Zugkräfte auf.'),
    ]),
    ('oeko', [
        A('**M1:** Nenne zwei Möglichkeiten, ökologischer zu bauen, und begründe.', 2, 'Holz statt Beton (speichert CO₂, nachwachsend) · Recyclingbeton (spart Rohstoffe) · Lehm, Hanfdämmung (natürlich, wenig Energie bei der Herstellung) · regionale Baustoffe (kurze Wege)'),
    ]),
]),

'02_Kraefte': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne einen belasteten Balken und markiere Druck- und Zugzone farbig.',
    sections=[
    ('lasten', [
        SORT('Sortiere die Lasten.', ['Betondecke', 'Möbel', 'Schnee', 'Dachziegel', 'Menschen', 'Wind'], ['Eigenlast', 'Nutzlast', 'Umweltlast'], h=12,
             loes=[['Betondecke', 'Dachziegel'], ['Möbel', 'Menschen'], ['Schnee', 'Wind']]),
    ]),
    ('beanspruchung', [
        ZU('Ordne zu.', ['Zug', 'Druck', 'Biegung', 'Verdrehung', 'Abscherung'], ['Regalboden', 'Niet', 'Seil', 'Säule', 'Schraubendreher'], loes=[3, 5, 1, 4, 2]),
    ]),
    ('biegung', [
        BOX('Zeichne einen Balken auf zwei Auflagern mit Last in der Mitte. Markiere Druckzone, Zugzone und die Lage der Bewehrung.', 34, loes='Durchgebogener Balken: oben Druck (gestaucht), unten Zug (gedehnt); Stahlbewehrung unten in der Zugzone.'),
    ]),
    ('m1', [
        A('**M1:** Begründe, warum Stahlträger oft ein I-Profil haben.', 2, 'Bei Biegung werden vor allem Ober- und Unterseite belastet. Das I-Profil hat dort viel Material und in der Mitte wenig – es ist sehr steif und trotzdem leicht.'),
    ]),
]),

'03_Bruecken': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Skizziere drei Brückenarten und markiere Zug (blau) und Druck (rot).',
    sections=[
    ('arten', [
        ZU('Ordne die Brückenarten zu.', ['Balkenbrücke', 'Bogenbrücke', 'Hängebrücke', 'Fachwerkbrücke'], ['Seile über Pylone, große Spannweite', 'Stäbe in Dreiecken', 'Balken auf Stützen, Biegung', 'Last als Druck in die Widerlager'], loes=[3, 4, 1, 2]),
    ]),
    ('dreieck', [
        A('Erkläre, warum ein Rahmen aus vier Stäben mit einer Diagonale stabil wird.', 2, 'Die Diagonale teilt das Viereck in zwei Dreiecke. Ein Dreieck ist durch seine drei Seitenlängen festgelegt und lässt sich nicht verschieben.'),
    ]),
    ('kraefte', [
        SORT('Zug oder Druck?', ['Tragseil', 'Pylon', 'Steinbogen', 'Hänger', 'Brückenpfeiler'], ['Zug', 'Druck'], h=12,
             loes=[['Tragseil', 'Hänger'], ['Pylon', 'Steinbogen', 'Brückenpfeiler']]),
    ]),
    ('aufgabe', [
        BOX('**M1:** Skizziere eure Idee für die Papierbrücke und begründe die Konstruktion.', 40, loes='Individuell; Begründung mit Profilen (gefaltete Träger), Dreiecken (Fachwerk) und Zug/Druck.'),
    ]),
]),

'04_Versorgung': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne einen Siphon im Schnitt und erkläre seine Funktion.',
    sections=[
    ('haus', [
        ZU('Ordne die Teile zu.', ['Stromzähler', 'Sicherungskasten', 'Wasserzähler', 'Siphon'], ['misst Wasser in m³', 'sperrt Kanalgase aus', 'misst Energie in kWh', 'Leitungsschutzschalter und FI'], loes=[3, 4, 1, 2]),
    ]),
    ('strom', [
        GL('Ergänze den Weg des Stroms.', ['Ortsnetz → [[Hausanschlusskasten]] → [[Stromzähler]] → [[Sicherungskasten]] → Stromkreis → Steckdose']),
    ]),
    ('abwasser', [
        GL('Ergänze den Weg des Abwassers.', ['Waschbecken → [[Siphon]] → [[Fallrohr]] → Grundleitung → Kanal → [[Kläranlage]]']),
        BOX('Zeichne einen Siphon im Schnitt und markiere das Sperrwasser.', 26, loes='U-förmig gebogenes Rohr unter dem Abfluss; im unteren Bogen steht Wasser.'),
        A('Erkläre, warum es unter Waschbecken einen gebogenen Rohrbogen gibt.', 1, 'Im Bogen bleibt immer Wasser stehen; es sperrt Gerüche aus dem Kanal ab (Geruchsverschluss).'),
    ]),
    ('m1', [
        A('**M1:** Nenne drei Möglichkeiten, Trinkwasser zu sparen.', 2, 'Duschen statt Baden, Spartaste an der Toilette, Wasserhahn beim Zähneputzen zu, Regenwasser für den Garten, Waschmaschine voll beladen'),
    ]),
]),

'05_Heizen_Daemmen': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Notiere fünf Energiespartipps für eure Wohnung.',
    sections=[
    ('heizung', [
        ZU('Ordne die Heizungsarten zu.', ['Wärmepumpe', 'Pelletheizung', 'Fernwärme', 'Solarthermie'], ['heißes Wasser vom Kraftwerk', 'Kollektoren erwärmen Wasser', 'verbrennt gepresstes Holz', 'Umweltwärme mit Strom'], loes=[4, 3, 1, 2]),
    ]),
    ('verlust', [
        GL('Berechne den Wärmeverlust mit U · A · ΔT.', ['ungedämmt: U = 1,4; A = 100 m²; ΔT = 20 K → [[2800]] W', 'gedämmt: U = 0,24; A = 100 m²; ΔT = 20 K → [[480]] W', 'Einsparung: [[2320]] W ≈ [[83]] %']),
    ]),
    ('haus', [
        A('Nenne zu drei Stellen am Haus, wo Wärme verloren geht, je eine Maßnahme.', 3, 'Außenwand: Fassadendämmung · Dach: Dämmung der Sparren · Fenster: Dreifachverglasung · Keller: Kellerdecke dämmen · Lüftung: Wärmerückgewinnung, Stoßlüften'),
    ]),
    ('sparen', [
        RF(['f|Gekippte Fenster sparen Energie.|Stoßlüften spart Energie.', 'r|1 °C weniger spart etwa 6 % Heizenergie.', 'f|Standby verbraucht keinen Strom.|Standby verbraucht Strom.']),
    ]),
]),

'06_Wiederholung': dict(ichkann=True, skip=['quiz-st'], heft_label='Notizen', heft_title='Das muss ich noch üben', heft_sub='Fragen, Merkpunkte, Formeln',
    sections=[
    ('begriffe', [
        ZU('Ordne die Fachbegriffe zu.', ['Skelettbau', 'Stahlbeton', 'Fachwerk', 'Siphon', 'U-Wert'],
           ['Geruchsverschluss', 'Stützen tragen', 'Wärmeverlust pro m² und K', 'Dreiecke', 'Beton und Stahl'], loes=[2, 5, 4, 1, 3]),
    ]),
    ('t1', [
        RF(['r|Ein Seil kann nur Zug aufnehmen.', 'f|Bei Biegung ist die Oberseite auf Zug belastet.|Die Oberseite wird auf Druck belastet.', 'r|Ein Bogen leitet die Last als Druck ab.'], fix=False),
    ]),
    ('t2', [
        GL('Rechne.', ['U = 0,5; A = 80 m²; ΔT = 25 K → [[1000]] W']),
    ]),
    ('t3', [
        GL('Ergänze.', ['Hausanschlusskasten → [[Zähler]] → Sicherungskasten → [[Stromkreis]]']),
    ]),
]),
}
