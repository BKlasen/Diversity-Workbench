Anwendung des Skriptes in google refine:

    Spalte ausw�hlen, die ge�ndert werden soll (enthalten L�ngengrade und Breitengrade in verschiedenen Schreibweisen)
    "Edit column / Add column based on this column..." ausw�hlen
    Einen neuen Spaltennamen eingeben
    Language umstellen auf "Jython"
    Das Skript in das Bearbeitungsfeld kopieren
    Umbedingt darauf achten, dass in der ersten Zeile beim Setzen der Variable long_lat (long_lat = "Lat.") der Spaltenname der basierenden Spalte verwendet wird (Punkte.... nicht �bersehen). F�r die Spalte Long diesen anpassen.
    Im Textfeld unten kontrollieren, ob alles richtig eingestellt ist und umgerechnet wird. Gegebenenfalls vorher �ber "Text facet" Reihen mit Koordinatenangaben ausw�hlen.
    Mit "ok" best�tigen.
