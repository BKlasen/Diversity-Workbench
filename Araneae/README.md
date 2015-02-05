***In der excel-Tabelle vorhandene Spalten und ihre Zuordnung im Import Wizard (DWB Version 3.0.7.6):***

_Catalog Nr._  
-->  Specimen/Accession/AccessionNumber (als decisive markiert)  
-->  Part 1/AccessionNumber (als decisive markiert)

_Type status_  
--> Identification 1.1/TypeStatus (mit Transformation: Translation: HT, PT wird zu Holotype bzw. Paratype)  

_Reservierung_  
--> Specimen/DataWitholdingReason  (nicht decisive)  
--> Specimen/Notes/InternalNotes (nicht decisive)

_Family_  
-->  Organism 1/Family Cache (nicht decisive)  
-->  Identification 1.1 (nicht decisive, als letzte Möglichkeit, wenn keine Artbestimmung vorliegt; mit Transformation: Filter: Import, if content in column 4 (Genus Name) = "blank"; aufpassen dass es blank ist und nicht ein Leerzeichen in die Abfrage eingesetzt wird) 

_Genus Name_  
--> Identification 1.1/TaxonomicName (als decisive markiert; mit Post.: Leerzeichen)

_Species Name_  
--> Identification 1.1/TaxonomicName (addiert, nicht decisive, mit Post.: Leerzeichen)

_Author_  
--> Identification 1.1/TaxonomicName (addiert, nicht decisive, mit Post.: Leerzeichen)

_Date descr._  
--> Identification 1.1/TaxonomicName (addiert, nicht decisive, ohne Pre/Post) 

_Species revision_  
--> wird nicht importiert
 
_Determined by_  
--> Identification 1.1/Responsible/ResponsibleName (als decisive markiert)

_Date det._  
--> Identification 1.1/Date/IdentificationDateSupplement (nicht als decisive markiert)

_Country_  
--> Event/CountryCache ((als decisive markiert)

_Admin._  
--> Event/LocalityDescription (als decisive markiert, mit Post.: ,Leerzeichen)

_Locality_  
--> Event/LocalityDescription (addiert, ohne Pre/Post)

_Lat und Long_  
--> werden nicht importiert (alte Koordinaten, die in verschiedenen Formaten vorliegen, zum Import wurden die Spalten "Lat_dec" bzw. "Long_dec" eingefügt und über ein Script in Google refine in das WGS84-Format transformiert, bei Anwendung des Skriptes darauf achten, dass der Spaltenname exakt geschrieben ist)

_Lat_dec_  
--> Coordinates WGS84/Lat.(NS) (als decisive markiert)

_Long_dec_  
--> Coordinates WGS84/Long.(EW) (als decisive markiert)

_coord_uncertainty_flag__  
--> Coordinates WGS84/LocationAccuracy (nicht decisive)

_coord_info_  
--> Coordinate WGS84/LocationNotes (nicht decisive)

_Ecology_  
--> Event/Notes (nicht decisive)

_Altitude m_  
--> Altitude (mNN)/Alt.from (als decisive markiert, mit Transformation: Schere, Position 1, Splitter - (Bindestrich), Seq. nach rechts)  
--> Altitude (mNN)/Alt.to (nicht decisive, mit Transformation: Schere, Position 2, Splitter - (Bindestrich), Seq. nach rechts) 

_Coll_Year_  
--> wird nicht importiert  

_Coll_date_  
--> Event/Date and time/CollectionDateSupplement (nicht decisive)

_Collector_  
--> wird nicht importiert  

_Collectors_  
--> Agent 1, Agent 2 und Agent 3 (jeweils als decisive markiert, mit Transformation: Schere, Position 1 (bzw. 2 und 3), Splitter / (Schrägstrich), Seq. nach rechts)

_m (male)_  
--> Organism 1/LifeStage (addiert, nicht decisive, kein Pre/Post, mit Transformation: Filter: import fixed value "adult", if content in column 27(also m) ungleich "blank" AND if content in column 28 (also f) gleich "blank" AND if content in column 27 ungleich "0")  
--> Organism 1/Gender (nicht decisive, ohne Pre/Post) für die Anzahl an männlichen Tieren  
--> Organism 1/Gender (addiert, nicht decisive, Pre.: Leerzeichen, Transformation: Filter: Import fixed value "male", if content in column 27 ungleich "blank" AND if content in column 27 ungleich "0"

_f (female)_  
--> Organism 1/LifeStage (addiert, nicht decisive, ohne Pre/Post, mit Transformation: Filter: Import fixed value "adult", if content in column 28 (also f) ungleich "blank" AND if content in column 28 ungleich "0"  
-->  Organism 1/Gender (addiert, nicht decisive, Pre.: Leerzeichen), für die Anzahl an weiblichen Tieren  
--> Organism 1/Gender (addiert, nicht decisive, Pre.: Leerzeichen, mit Transformation: Filter: Import fixed value "female", if content in column 28 (also f) ungleich "blank" AND if content in column 28 ungleich "0"

_j (juvenil)_  
-->  Organism 1/Lifestage (nicht decisive, Post.: Leerzeichen, mit Transformation: Filter: Import fixed value "juvenil", if content in column 29 (also j) ungleich "blank" AND if content in column 29 ungleich "0"

_Anzahl_  
--> Organism 1/NumberOfUnits (nicht decisive, ohne Pre/Post)
 
_Notes_  
-->  Specimen/Notes/OriginalNotes (nicht decisive, ohne Pre/Post)

_Gender_   
--> wird nicht importiert 


***weitere Einstellungen:***

 -  Attachment: als "Import as new data" markiert
 -  Merging: alles auf "Insert"
 -  Project 1: ProjectID: "For all: Araneae" (als decisive markiert)
 -  Part 1: MaterialCategory: "For all: preserved specimen" (als decisive markiert)
 -  Part 1/Storage/CollectionID: "For all: Section Arthropoda / Sektion Niedere Arthropoda" (als decisive markiert)
 -  Organism 1/Taxonomic Group: "For all: arthropod" (als decisive markiert)
 -  Organism 1/Hierarchy, name/LastIdentificationCache: "For all: 1" (nicht decisive)
