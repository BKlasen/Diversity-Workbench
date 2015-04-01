***In der excel-Tabelle vorhandene Spalten und ihre Zuordnung im Import Wizard (DWB Version 3.0.7.7 und 3.0.7.9, funktioniert nicht in Version 3.0.7.8):***

_Catalog Nr._  
--> Specimen/Accession/AccessionNumber (als decisive markiert)  
--> Part 1/AccessionNumber (als decisive markiert)  


_Type status_  
--> Organism 1/Identification 1.1/TypeStatus (nicht decisive, mit Transformation: Translation: HT - holotype, PT -> paratype)  


_Order_  
--> Organism 1/Hierarchy, name/OrderCache (nicht decisive)  


_Family_  
--> Organism 1/Hierarchy, name/FamilyCache (nicht decisive)  
--> Organism 1/Identification 1.1 /TaxonomicName (addiert als letztes, nicht decisive, als letzte Möglichkeit, wenn keine Artbestimmung vorliegt; mit Transformation: Filter: Import, if content in column  4 (Genus Name) = "blank"; aufpassen dass es blank ist und nicht ein Leerzeichen in die Abfrage eingesetzt wird)  


_Genus Name_  
--> Organism 1/Identification 1.1/TaxonomicName (als decisive markiert)  


_Species Name_  
--> Organism 1/Identification 1.1/TaxonomicName (addiert, nicht decisive, mit Pre.: Leerzeichen)  


_Author_  
--> Organism 1/Identification 1.1/TaxonomicName (addiert, nicht decisive, mit Pre.: Leerzeichen)  


_Date descr._  
--> Organism 1/Identification 1.1/TaxonomicName (addiert, nicht decisive, mit Pre.: Leerzeichen)  


_Determined by_  
--> Identification 1.1/Responsible/ResponsibleName (nicht decisive)  


_Date det._  
--> Identification 1.1/Date/IdentificationDateSupplement (nicht decisive)  


_Country_  
--> Event/CountryCache (als decisive markiert)  


_Locality_  
--> Event/LocalityDescription (als decisive markiert)  


_Lat_  
--> Coordinates WGS84/LocationNotes (addiert, nicht decisive, mit Pre.: "Original Latitude: ")   

_Long_  
--> Coordinates WGS84/LocationNotes (nicht decisive, mit Pre.: "Original Longitude: ", mit Post.: "Leerzeichen ; Leerzeichen")     


_Lat_dec_  
--> Coordinates WGS84/Lat.(NS) (als decisive markiert)  


_Long_dec_  
--> Coordinates WGS84/Long.(EW) (als decisive markiert)  


_coord_uncertainty_flag_  
--> Coordinates WGS84/LocationAccuracy (nicht decisive)  


_Ecology_  
--> Event/Notes (nicht decisive)  


_Altitude_  
--> Altitude (mNN)/Alt.from (als decisive markiert, mit Transformation: Schere, Position 1, Splitter - (Bindestrich), Seq. nach rechts)  
--> Altitude (mNN)/Alt.to (nicht decisive, mit Transformation: Schere, Position 2, Splitter - (Bindestrich), Seq. nach rechts)  


_Depth_  
--> Depth/Depth from (als decisive markiert; mit Transformation: Schere, Position 1, Splitter - (Bindestrich), Seq. nach rechts)  
--> Depth/to (nicht decisive, mit Transformation: Schere, Position 2, Splitter - (Bindestrich), Seq. nach rechts)  


_Coll. Date_  
--> Event/Date and time/CollectionDateSupplement (nicht decisive)  


_Collector_  
--> wird nicht importiert 


_Collectors_  
--> Agent 1, Agent 2 bzw. Agent 3/CollectorsName (jeweils als decisive markiert, mit Transformation: Schere, Position 1 (bzw. 2 und 3), Splitter "Komma", Seq. nach rechts)  


_Specimens_  
--> Organism 1/NumberOfUnits (nicht decisive)  


_Notes_  
--> Specimen/Notes/OriginalNotes (nicht decisive)  


_Host_  
--> Organism **1**/ Relation/RelationType (nicht decisive, mit Transformation: Filter: Import fixed value "Found on", if content in column 25 (Host) ungleich "blank", Vorsicht, richtige Schreibweise, da Foreign Key)  
--> Organism **1**/Notes etc./Notes (nicht decisive; mit Pre.:"Host: ")  
--> Organism **2**/Taxonomic Group (als decisive markiert; mit Transformation: Filter: Import fixed value "unknown", if content in column 25 (Host) ungleich "blank", Vorsicht richtige Schreibweise, da Foreign Key)     
--> Organism **2**/ Identification **2.1**/ TaxonomicName (nicht decisive)   


_last modified_  
--> Specimen/Notes/Additional Notes (nicht decisive; mit Pre.: "last modified: ")  
 


_weitere Einstellungen:_  

-  Attachment: als "Import as new data" markiert  
-  Merging: alles auf "Insert"  
-  Project 1: ProjectID: "For all: Crustacea" (als decisive markiert)  
-  Part 1/MaterialCategory: "For all: preserved specimen" (nicht decisive)  
-  Part 1/Storage/CollectionID: "For all: Section Arthropoda / Sektion Niedere Arthropoda" (nicht decisive)  
-  Organism 1/Taxonomic Group: "For all: arthropod" (als decisive markiert)  
-  Organism 1/Hierarchy, name/LastIdentificationCache: "For all: 1" (nicht decisive)
-  Organism 1/Identification 1.1/IdentificationSequence: "For all: 1" (nicht decisive)  
-  Organism 2/Relation/RelatedUnitID: "Organism 1" (nicht decisive)  
-  Organism 2/Hierarchy, name/LastIdentificationCache: "For all: 1" (nicht decisive)  
-  Organism 2/Identification 2.1/IdentificationSequence: "For all: 1" (als decisive markiert)  