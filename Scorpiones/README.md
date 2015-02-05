***In der excel-Tabelle vorhandene Spalten und ihre Zuordnung im Import Wizard (DWB Version 3.0.7.6):***

_Catalog Nr._  
-->  Specimen/Accession/AccessionNumber (als decisive markiert)  
-->  Part 1/AccessionNumber (als decisive markiert)

_Family_  
-->  Organism 1/Hierarchy, name/Family Cache (nicht decisive)  
-->  Identification 1.1 (nicht decisive, als letzte Möglichkeit, wenn keine Artbestimmung vorliegt; mit Transformation: Filter: Import, if content in column 2 (Species Name) = "blank"; aufpassen dass es blank ist und nicht ein Leerzeichen in die Abfrage eingesetzt wird) 

_Species Name_  
--> Identification 1.1/TaxonomicName (als decisive markiert)

_Author_  
--> Identification 1.1/TaxonomicName (addiert, nicht decisive, mit Pre.: Leerzeichen)

_Determined by_  
--> Identification 1.1/Responsible/ResponsibleName (als decisive markiert)

_Country_  
--> Event/CountryCache (als decisive markiert)

_Locality_  
--> Event/LocalityDescription (als decisive markiert)

_Lat. und Long._  
--> werden nicht importiert (alte Koordinaten, die in verschiedenen Formaten vorliegen, zum Import wurden die Spalten "Lat_dec." bzw. "Long_dec" eingefügt und über ein Script in Google refine in das WGS84-Format transformiert, bei Anwendung des Skriptes darauf achten, dass der Spaltenname exakt geschrieben ist, Punkte!!!)

_Lat_dec._  
--> Coordinates WGS84/Lat.(NS) (nicht decisive)

_Long_dec_  
--> Coordinates WGS84/Long.(EW) (als decisive markiert)

_Ecology_  
--> Event/Notes (nicht decisive)

_Altitude_  
--> wird nicht importiert (Höhenangaben vor Bereinigung)  

_Altitude (m)_  
--> Altitude (mNN)/Alt.from (als decisive markiert, mit Transformation: Schere, Position 1, Splitter - (Bindestrich), Seq. nach rechts)  
--> Altitude (mNN)/Alt.to (nicht decisive, mit Transformation: Schere, Position 2, Splitter - (Bindestrich), Seq. nach rechts)  

_Date_  
--> Event/Date and time/CollectionDateSupplement (als decisive markiert)

_Year_  
--> wird nicht importiert  

_Collector_  
--> wird nicht importiert  

_Collectors_  
--> Agent 1 und Agent 2 (jeweils als decisive markiert, mit Transformation: Schere, Position 1 (bzw. 2), Splitter / (Schrägstrich), Seq. nach rechts)

_Notes_  
-->  Specimen/Notes/OriginalNotes (nicht decisive)

_Sex_   
-->  Organism 1/Gender (nicht decisive)  

***weitere Einstellungen:***
* Attachment:  als "Import as new data" markiert  
* Merging:  alles auf "Insert"  
* Project 1: ProjectID: "For all: Scorpiones" (als decisive markiert)  
* Part 1: MaterialCategory: "For all: preserved specimen" (nicht decisive)  
* Part 1/Storage/CollectionID: "For all: Section Arthropoda / Sektion Niedere Arthropoda" (nicht decisive)    
* Organism 1/Taxonomic Group: "For all: arthropod" (als decisive markiert)  
* Organism 1/Hierarchy, name/LastIdentificationCache: "For all: 1" (nicht decisive) 
