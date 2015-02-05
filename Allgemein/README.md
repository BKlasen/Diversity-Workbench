Anwendung des Skriptes in google refine:

    Spalte auswählen, die geändert werden soll (enthalten Längengrade und Breitengrade in verschiedenen Schreibweisen)
    "Edit column / Add column based on this column..." auswählen
    Einen neuen Spaltennamen eingeben
    Language umstellen auf "Jython"
    Das Skript in das Bearbeitungsfeld kopieren
    Umbedingt darauf achten, dass in der ersten Zeile beim Setzen der Variable long_lat (long_lat = "Lat.") der Spaltenname der basierenden Spalte verwendet wird (Punkte.... nicht übersehen). Für die Spalte Long diesen anpassen.
    Im Textfeld unten kontrollieren, ob alles richtig eingestellt ist und umgerechnet wird. Gegebenenfalls vorher über "Text facet" Reihen mit Koordinatenangaben auswählen.
    Mit "ok" bestätigen.
