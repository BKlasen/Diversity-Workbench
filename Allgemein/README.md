**Anwendung des Skriptes in google refine:**

  *  Spalte auswählen, die geändert werden soll (enthalten Längengrade und Breitengrade in verschiedenen Schreibweisen)
  *  "Edit column / Add column based on this column..." auswählen
  *  Einen neuen Spaltennamen eingeben
  *  Language umstellen auf "Jython"
  *  Das Skript in das Bearbeitungsfeld kopieren
  *  Umbedingt darauf achten, dass in der ersten Zeile beim Setzen der Variable long_lat (long_lat = "Lat.") der 	  Spaltenname der basierenden Spalte verwendet wird (Punkte.... nicht übersehen). Für die Spalte Long diesen anpassen.
  *  Im Textfeld unten kontrollieren, ob alles richtig eingestellt ist und umgerechnet wird. Gegebenenfalls vorher   über "Text facet" Reihen mit Koordinatenangaben auswählen.
  *  Mit "ok" bestätigen.
  
  ***


**Verknüpfen des taxonomischen Namens mit der TaxonNames Insecta**

-	Administration ->Database ->  Maintenance -> 
-	Tab „Synchronize Database“ (oben ganz links) auswählen
-	Tab „Collection <> Taxon Names“ auswählen (ganz links)
-	Tab “Synchronize taxonomic names missing a connection”  auswählen
-	Taxonomic database: “Diversity TaxonNames_Insecta” auswählen
-	Taxonomy project: “Orthopteroidea” auswählen
-	Project: “Orthoptera” auswählen
-	Taxonomic project: “Insect” auswählen
-	“Compare first parts” anklicken  und “2” eingeben
-	„Update similar name“ mit Rank:“species“ auswählen

Dann:  	„Check for identical names“ starten 

-	Weiß: der Name stimmt exakt überein und wird verknüpft (ist schon vorne angehakt)
-	Gelb: Abweichungen beim Autor (z.B. Klammern, Vorname), kann manuell angehakt werden
-	Rot: Größere Abweichungen bei den Hauptteilen des Namens,  kann manuell angehakt werden.
-	Blau: zu einem Namen gibt es mehrere gleiche Namen

Start update: Die angehakten Namen werden in der Datenbank überschrieben mit dem Namen aus der TaxonNames_Insecta.
Das Feld „Tax. Name“ ist hellgelb hinterlegt, wenn eine Verknüpfung besteht.

  ***
  
  **Family, Order und Hierarchy eintragen:**

-	Administration ->Database ->  Maintenance -> 
-	Tab „Synchronize Database“ (1., oben ganz links) auswählen
-	Tab „Collection <> Taxon Names“  auswählen (2., ganz links)
-	Tab “Hierarchy”  auswählen (3., ganz rechts)
-	Taxonomy database: “Diversity TaxonNames_Insecta” auswählen
-	Taxonomy project: “Orthopteroidea” auswählen
-	Project: “Orthoptera” auswählen
-	Taxonomic project: “Insect” auswählen
-	Entweder „Family“, „Order“ oder „Hierarchy“ auswählen
-	„Check for Differences“ anklicken und warten bis der Vergleich durchgelaufen ist
-	Wenn alles richtig ist, „Start update“ drücken und die Hierarchy, etc.  wird eingetragen

  ***
  
 **Koordinaten richtig in Excel einlesen**
  
  (Problem: Wenn man die aus DWS exportierte .txt-Datei einfach mit Excel öffnet, rechnet dieses die Koordinaten automatisch in ein falsches Format um.)
  - Excel starten
  - die exportierte txt-Datei aus Excel aufrufen (nicht umgekehrt)
  - es erscheint der "Textkonvertierungs-Assistent"
  - Schritt 1 von 3: "Getrennt" anklicken (Voreinstellung lassen) -> weiter 
  - Schritt 2 von 3: Trennzeichen "Tabstopp" anklicken (Voreinstellung) -> weiter
  - Schritt 3 von 3: Das Datenformat der Spalten mit den Koordinaten auf "Text" ändern -> Fertig stellen
  
GGf. das Datenformat des Datums auch ändern. 
Dies funktioniert nur mit der .txt-Datei, nicht mit der .csv-Datei.




