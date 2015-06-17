***In der DWB vorhandene Datenfelder und ihre Zuordnung beim Export (Version 3.0.7.9zl):***

_Specimen / AccessionNumber_  
-->  Catalog Nr.  


_Organism1 / FamilyCache_    
-->  Family


_Organism1 / Identification1.1 / Taxonomic Name_  
--> Genus Name (mit Transformation: Splitter, Position 1, Trennzeichen : "Leerzeichen")  


_Organism1 / Identification1.1 / Taxonomic Name_  
--> Species Name (mit Transformation: Splitter, Position 2, Trennzeichen : "Leerzeichen")  


_Specimen / Organism 1 / Gender_  
--> Gender  


_Part 1 / AccessionNumber_  (dient dazu, die Material-Kategorie auszugeben (Alcohol, Skull, Tissue,...)
--> Material Part 1  (mit Transformation: Splitter, Position 3, Trennzeichen: "Bindestrich")  


_Part 1 / Notes_  
--> Notes Part 1  


_Part 2 / AccessionNumber_  (dient dazu, die Material-Kategorie auszugeben (Alcohol, Skull, Tissue,...)
--> Material Part 2  (mit Transformation: Splitter, Position 3, Trennzeichen: "Bindestrich")  


_Part 2 / Notes_  
--> Notes Part 2  


_Part 3 / AccessionNumber_  (dient dazu, die Material-Kategorie auszugeben (Alcohol, Skull, Tissue,...)
--> Material Part 3  (mit Transformation: Splitter, Position 3, Trennzeichen: "Bindestrich")  


_Part 3 / Notes_  
--> Notes Part 3  


_Part 4 / AccessionNumber_  (dient dazu, die Material-Kategorie auszugeben (Alcohol, Skull, Tissue,...)
--> Material Part 4  (mit Transformation: Splitter, Position 3, Trennzeichen: "Bindestrich")  


_Part 4 / Notes_  
--> Notes Part 4  


_Event / CountryCache_  
--> Country  


_Event / LocalityDescription_  
--> Locality  


_Event / WGS84 / AverageLatitudeCache_  
--> Lat_dec  


_Event / WGS84 / AverageLongitudeCache_  
--> Long_dec  


_Event / HabitatDescription_  
--> Ecology  


_Event / Altitude / AverageAltitudeCache_  
--> Altitude (m)  


_Event / CollectionDate_  
--> Coll_Date (mit Transformation: Splitter: Position 1, Trennzeichen "Leerzeichen") dadurch wird der Stunden/Minuten-Teil abgeschnitten  


_Specimen / Collector 1 / CollectorsName_  
--> Collectors  


_Specimen / Collector 2 / CollectorsName_  
--> Collectors  (mit Pre: ", "; den Spaltentrenner (dunkelgrauer Balken zwischen den Spalten anklicken -> wird aufgehoben (hellgrau) und alle Sammler werden in eine Spalte geschrieben)  


_____________________________________________________________________________
Abfrage über MAterial Kategorie noch nicht komplett eingebaut, da einige Material Kategorien doppelt belegt sind (pelt für skin- und alkohol-Präparate)
_____________________________________________________________________________


_weitere Hinweise:_  
- bei Organism 1 / Identification 1.1 / IdentificationSequence muss das kleine Dreieck nach unten zeigen (dann wird die aktuellste Bestimmung ausgegeben)
- die exportierte Datei wird immer in den Ordner "Export" der verwendeten DWB-Version gespeichert; man kann einen anderen Speicherort auswählen, aber es wird immer der übergeordnetet Ordner von dem Ordner, den man ausgewählt hat, genommen; dies muss man bei jedem Start neu einstellen  
- um die Koordinaten richtig in Excel anzeigen zu lassen, s. bei Allgemeines  
- im Tab "Export" nicht auf die Anzeige "Reading data" warten, sondern direkt "Export data" anklicken
