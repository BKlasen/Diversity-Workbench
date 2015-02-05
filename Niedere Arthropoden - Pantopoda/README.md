**In der excel-Tabelle vorhandene Spalten und ihre Zuordnung im Import Wizard (DWB Version 3.0.7.6):**

_Catalog Nr._  
-->  Specimen/Accession/AccessionNumber (als decisive markiert)  
-->  Part 1/AccessionNumber (als decisive markiert)

_Type status_  
--> Identification 1.1/TypeStatus (nicht decisive, mit Transformation: Translation: HT, PT wird zu Holotype bzw. Paratype)  

_Family_  
-->  Organism 1/Family Cache (nicht decisive)  
-->  Identification 1.1 (als decisive markiert, als letzte Möglichkeit, wenn keine Artbestimmung vorliegt; mit Transformation: Filter: Import, if content in column 3 (Genus Name) = "blank"; aufpassen dass es blank ist und nicht ein Leerzeichen in die Abfrage eingesetzt wird) 

_Genus Name_  
--> Identification 1.1/TaxonomicName (als decisive markiert)

_Species Name_  
--> Identification 1.1/TaxonomicName (addiert, nicht decisive, mit Pre.: Leerzeichen)

_Author_  
--> Identification 1.1/TaxonomicName (addiert, nicht decisive, mit Pre.: Leerzeichen)

_Date descr._  
--> Identification 1.1/TaxonomicName (addiert, nicht decisive, mit Pre.: Leerzeichen) 
 
_Determined by_  
--> Identification 1.1/Responsible/ResponsibleName (als decisive markiert)

_Date det._  
--> Identification 1.1/Date/IdentificationDateSupplement (nicht decisive)

_Country_  
--> Event/CountryCache (als decisive markiert)

_Locality_  
--> Event/LocalityDescription (nicht decisive)

_Lat und Long_  
--> werden nicht importiert (alte Koordinaten, die in verschiedenen Formaten vorliegen, zum Import wurden die Spalten "Lat_dec" bzw. "Long_dec" eingefügt und über ein Script in Google refine in das WGS84-Format transformiert, bei Anwendung des Skriptes darauf achten, dass der Spaltenname exakt geschrieben ist)

_Lat_dec_  
--> Coordinates WGS84/Lat.(NS) (als decisive markiert)  

_Long_dec_  
--> Coordinates WGS84/Long.(EW) (als decisive markiert)  

_Ecology_  
--> Event/Notes (nicht decisive)

_Altitude_  
--> Altitude (mNN)/Alt.from (als decisive markiert, mit Transformation: Schere, Position 1, Splitter - (Bindestrich), Seq. nach rechts)  
--> Altitude (mNN)/Alt.to (nicht decisive, mit Transformation: Schere, Position 2, Splitter - (Bindestrich), Seq. nach rechts) 

_Date_  
--> Event/Date and time/CollectionDateSupplement (nicht decisive)

_Collector_  
--> Agent 1 (als decisive markiert)  

_Specimens  
--> Organism 1/Notes etc./Notes (nicht decisive)  

_feature_  
--> wird nicht importiert

_Male_  
--> Organism 1/LifeStage (addiert, nicht decisive, Pre.: Leerzeichen, mit Transformation: Filter: import fixed value "adult", if content in column 21(also Male) ungleich "blank" AND if content in column 22 (also Female) gleich "blank")  
--> Organism 1/Gender (nicht decisive, ohne Pre/Post) für die Anzahl an männlichen Tieren  
--> Organism 1/Gender (addiert, nicht decisive, Pre.: Leerzeichen, mit Transformation: Filter: Import fixed value "male", if content in column 21 ungleich "blank")

_Female_  
--> Organism 1/LifeStage (addiert, nicht decisive, Pre.: Leerzeichen, mit Transformation: Filter: Import fixed value "adult", if content in column 22 (also Female) ungleich "blank")    
-->  Organism 1/Gender (addiert, nicht decisive, Pre.: Leerzeichen), für die Anzahl an weiblichen Tieren  
--> Organism 1/Gender (addiert, nicht decisive, Pre.: Leerzeichen, mit Transformation: Filter: Import fixed value "female", if content in column 22 (also Female) ungleich "blank")

_juvenile_  
-->  Organism 1/Lifestage (nicht decisive, Pre.: Leerzeichen, mit Transformation: Filter: Import fixed value "juvenil", if content in column 23 (also juvenil) ungleich "blank")  

_Age_  
--> wird nicht importiert  

_Gender_  
--> wir nicht importiert  

_Anzahl_  
--> Organism 1/NumberOfUnits (nicht decisive)
 
_Notes_  
-->  Specimen/Notes/OriginalNotes (nicht decisive)

***weitere Einstellungen:***

* Attachment:  als "Import as new data" markiert  
* Merging:  alles auf "Insert"  
* Project 1: ProjectID: "For all: Pantopoda" (als decisive markiert)  
* Part 1: MaterialCategory: "For all: preserved specimen" (nicht decisive)  
* Part 1/Storage/CollectionID: "For all: Section Arthropoda / Sektion Niedere Arthropoda" (als decisive markiert)    
* Organism 1/Taxonomic Group: "For all: arthropod" (als decisive markiert)  
* Organism 1/Hierarchy, name/LastIdentificationCache: "For all: 1" (nicht decisive)  
