**In der excel-Tabelle vorhandene Spalten und ihre Zuordnung im Import Wizard (DWB Version 3.0.7.7):**


_Catalog Nr._  
--> Specimen/Accession/AccessionNumber (als decisive markiert)  
--> Part 1/AccessionNumber (als decisive markiert)  


_Type status_  
--> Organism 1/Identification 1.1/TypeStatus (nicht decisive, mit Transformation: Translation: AT -> allotype, HT - holotype, PT -> paratype)  

_Family_  
--> Organism 1/Hierarchy, name/Family Cache (nicht decisive)  
--> Organism 1/Identification 1.1 /TaxonomicName (addiert als vorletztes, nicht decisive, als letzte Möglichkeit, wenn keine Artbestimmung vorliegt; mit Transformation: Filter: Import, if content in column 3 (Genus Name) = "blank"; aufpassen dass es blank ist und nicht ein Leerzeichen in die Abfrage eingesetzt wird)  
--> Organism 1/Identification1.1/TaxonomicName (addiert, als allerletzte Möglichkeit, wenn gar keine Bestimmung vorliegt, eine Spalte muss ausgewählt werden; mit Transformation: Filter: Import fixed value "Acari", if content in column 2 (Family) = "blank" AND if content in column 3 (Genus Name) = "blank")  


_Genus Name_  
--> Organism 1/Identification 1.1/TaxonomicName (als decisive markiert)  


_Species Name_  
--> Organism 1/Identification 1.1/TaxonomicName (addiert, nicht decisive, mit Pre.: Leerzeichen)  


_Subspecies Name_  
--> Organism 1/Identification 1.1/TaxonomicName (addiert, nicht decisive, mit Pre.: Leerzeichen)  


_Author_  
--> Organism 1/Identification 1.1/TaxonomicName (addiert, nicht decisive, mit Pre.: Leerzeichen)  


_Date descr._  
--> Organism 1/Identification 1.1/TaxonomicName (addiert, nicht decisive, mit Pre.: Leerzeichen)  


_Determined by_  
--> Identification 1.1/Responsible/ResponsibleName (nicht decisive)  


_Date det._  
--> Identification/Date/IdentificationDateSupplement (nicht decisive)  


_Host_  
--> Organism **1**/ Relation/RelationType (als decisive markiert, mit Transformation: Filter: Import fixed value "Found on", if content in column 10 (Host) ungleich "blank", Vorsicht, richtige Schreibweise, da Foreign Key)  
--> Organism **1**/Notes etc./Notes (nicht decisive; mit Pre.:"Host: ")  
--> Organism **2**/Taxonomic Group (als decisive markiert; mit Transformation: Filter: Import fixed value "unknown", if content in column 10 (Host) ungleich "blank", Vorsicht richtige Schreibweise, da Foreign Key)   
--> Organism **2**/ Identification **2.1**/ TaxonomicName (als decisive markiert)  


_Host Voucher_  
--> Organism 2/Notes etc./ Notes (nicht decisive, mit Pre.: "Host Voucher: ")  

 
_Country_  
--> Event/CountryCache (als decisive markiert)  

_Locality_  
--> Event/LocalityDescription (als decisive markiert)  

_Lat und Long_  
--> werden nicht importiert (alte Koordinaten, die in verschiedenen Formaten vorliegen, zum Import wurden die Spalten "Lat_dec." bzw. "Long_dec" eingefügt und über ein Script in Google refine in das WGS84-Format transformiert, bei Anwendung des Skriptes darauf achten, dass der Spaltenname exakt geschrieben ist, Punkte!!!)  


_Lat_dec_  
--> Coordinates WGS84/Lat.(NS) (als decisive markiert)  


_Long_dec_  
--> Coordinates WGS84/Long.(EW) (als decisive markiert)  


_Ecology_  
--> Event/Notes (nicht decisive)  


_Altitude_  
--> Altitude (mNN)/Alt.from (als decisive markiert, mit Transformation: Schere, Position 1, Splitter - (Bindestrich), Seq. nach rechts)  
--> Altitude (mNN)/Alt.to (nicht decisive, mit Transformation: Schere, Position 2, Splitter - (Bindestrich), Seq. nach rechts)  


_Coll. Date_  
--> Event/Date and time/CollectionDateSupplement (als decisive markiert)  



_Collector_  
--> Agent 1, Agent 2 bzw. Agent 3/CollectorsName (jeweils als decisive markiert, mit Transformation: Schere, Position 1 (bzw. 2 und 3), Splitter "Komma", Seq. nach rechts)  


_Collectors_  
--> wird nicht importiert  


_Specimens_  
--> Organism 1/NumberOfUnits (nicht decisive)  


_Gender_  
--> Organism 1/Gender (nicht decisive)  


_Notes_  
--> Specimen/Notes/OriginalNotes (nicht decisive)  


_Conservation_  
--> Part 1/MaterialCategory (mit Transformation: Translation: alcohol -> vial, slides -> micr. slide, nicht decisive)  
--> Part 1/Preparation/PreparationMethod (nicht decisive, mit Transformation: Import fixed value: "Alcohol", if content in column 26 (conservation) = "alcohol")  


_weitere Einstellungen:_  

-  Attachment: als "Import as new data" markiert  
-  Merging: alles auf "Insert"  
-  Project 1: ProjectID: "For all: Acari" (als decisive markiert)  
-  Part 1/Storage/CollectionID: "For all: Section Arthropoda / Sektion Niedere Arthropoda" (nicht decisive)  
-  Organism 1/Taxonomic Group: "For all: arthropod" (als decisive markiert)  
-  Organism 1/Hierarchy, name/LastIdentificationCache: "For all: 1" (nicht decisive)
-  Organism 1/Identification 1.1/IdentificationSequence: "For all: 1" (nicht decisive)  
-  Organism 2/Relation/RelatedUnitID: "Organism 1" (nicht decisive)  
-  Organism 2/Hierarchy, name/LastIdentificationCache: "For all: 1" (nicht decisive)  
-  Organism 2/Identification 2.1/IdentificationSequence: "For all: 1" (nicht decisive)  
