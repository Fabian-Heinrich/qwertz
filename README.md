# Aufgabe

Sortierverfahren QWERTZ

Bei diesem Verfahren wird das zu sortierende Feld in zwei Teile zerlegt, wobei der erste Teil alle Elemente <= einem Vergleichselement enthält, der rechte Teil alle Elemente > dem Vergleichselement.

Mit beiden Teilen wird dann analog verfahren (also die Felder werden wieder je in zwei Felder zerlegt, wobei für jedes mal natürlich ein neues Vergleichselement gewählt werden muss), bis nur noch einelementige Teile vorliegen. Diese werden dann wieder zusammengesetzt, wodurch das Feld sortiert ist (weil die Teilfelder ja von links nach rechts aufsteigend sortiert sind).

Wer dem Verfahren nicht traut, kann gerne Probeläufe mit Zetteln duirchführen.

Erstellen Sie ein NSD und laden Sie es hier hoch. Kommentieren Sie dabei genau, wie Sie das Vergleichselement wählen.


# Ansatz

Kleinste der ersten beiden zahlen als Vergleichselement

897346125 -> 8
	87346125 -> 7
		7346125 -> 3
			312 -> 1
				1
				32 -> 2
					2
					3
			7465 -> 4
				4
				765 -> 6
					65 -> 5
						5
						6
					7
		8
	9
	
	
	
	
