In der excel-Tabelle vorhandene Spalten und ihre Zuordnung im Import Wizard (DWB Version 3.0.7.6):

Catalog Nr.
--> Specimen/Accession/AccessionNumber (als decisive markiert)
--> Part 1/AccessionNumber (als decisive markiert)

Type status
--> Identification 1.1/TypeStatus (mit Transformation: Translation: HT, PT wird zu Holotype bzw. Paratype)

Reservierung
--> Specimen/DataWitholdingReason (nicht decisive)
--> Specimen/Notes/InternalNotes (nicht decisive)

Family
--> Organism 1/Family Cache (nicht decisive)
--> Identification 1.1 (nicht decisive, als letzte Möglichkeit, wenn keine Artbestimmung vorliegt; mit Transformation: Filter: Import, if content in column 4 (Genus Name) = "blank"; aufpassen dass es blank ist und nicht ein Leerzeichen in die Abfrage eingesetzt wird)

Genus Name
--> Identification 1.1/TaxonomicName (als decisive markiert; mit Post.: Leerzeichen)

Species Name
--> Identification 1.1/TaxonomicName (addiert, nicht decisive, mit Post.: Leerzeichen)

Author
--> Identification 1.1/TaxonomicName (addiert, nicht decisive, mit Post.: Leerzeichen)

Date descr.
--> Identification 1.1/TaxonomicName (addiert, nicht decisive, ohne Pre/Post)

Species revision
--> wird nicht importiert

Determined by
--> Identification 1.1/Responsible/ResponsibleName (als decisive markiert)

Date det.
--> Identification 1.1/Date/IdentificationDateSupplement (nicht als decisive markiert)

Country
--> Event/CountryCache ((als decisive markiert)

Admin.
--> Event/LocalityDescription (als decisive markiert, mit Post.: ,Leerzeichen)

Locality
--> Event/LocalityDescription (addiert, ohne Pre/Post)

Lat und Long
--> werden nicht importiert (alte Koordinaten, die in verschiedenen Formaten vorliegen, zum Import wurden die Spalten "Lat_dec" bzw. "Long_dec" eingefügt und über ein Script in Google refine in das WGS84-Format transformiert, bei Anwendung des Skriptes darauf achten, dass der Spaltenname exakt geschrieben ist)

Lat_dec
--> Coordinates WGS84/Lat.(NS) (als decisive markiert)

Long_dec
--> Coordinates WGS84/Long.(EW) (als decisive markiert)

coord_uncertainty_flag_
--> Coordinates WGS84/LocationAccuracy (nicht decisive)

coord_info
--> Coordinate WGS84/LocationNotes (nicht decisive)

Ecology
--> Event/Notes (nicht decisive)

Altitude m
--> Altitude (mNN)/Alt.from (als decisive markiert, mit Transformation: Schere, Position 1, Splitter - (Bindestrich), Seq. nach rechts)
--> Altitude (mNN)/Alt.to (nicht decisive, mit Transformation: Schere, Position 2, Splitter - (Bindestrich), Seq. nach rechts)

Coll_Year
--> wird nicht importiert

Coll_date
--> Event/Date and time/CollectionDateSupplement (nicht decisive)

Collector
--> wird nicht importiert

Collectors
--> Agent 1, Agent 2 und Agent 3 (jeweils als decisive markiert, mit Transformation: Schere, Position 1 (bzw. 2 und 3), Splitter / (Schrägstrich), Seq. nach rechts)

m (male)
--> Organism 1/LifeStage (addiert, nicht decisive, kein Pre/Post, mit Transformation: Filter: import fixed value "adult", if content in column 27(also m) ungleich "blank" AND if content in column 28 (also f) gleich "blank" AND if content in column 27 ungleich "0")
--> Organism 1/Gender (nicht decisive, ohne Pre/Post) für die Anzahl an männlichen Tieren
--> Organism 1/Gender (addiert, nicht decisive, Pre.: Leerzeichen, Transformation: Filter: Import fixed value "male", if content in column 27 ungleich "blank" AND if content in column 27 ungleich "0"

f (female)
--> Organism 1/LifeStage (addiert, nicht decisive, ohne Pre/Post, mit Transformation: Filter: Import fixed value "adult", if content in column 28 (also f) ungleich "blank" AND if content in column 28 ungleich "0"
--> Organism 1/Gender (addiert, nicht decisive, Pre.: Leerzeichen), für die Anzahl an weiblichen Tieren
--> Organism 1/Gender (addiert, nicht decisive, Pre.: Leerzeichen, mit Transformation: Filter: Import fixed value "female", if content in column 28 (also f) ungleich "blank" AND if content in column 28 ungleich "0"

j (juvenil)
--> Organism 1/Lifestage (nicht decisive, Post.: Leerzeichen, mit Transformation: Filter: Import fixed value "juvenil", if content in column 29 (also j) ungleich "blank" AND if content in column 29 ungleich "0"

Anzahl
--> Organism 1/NumberOfUnits (nicht decisive, ohne Pre/Post)

Notes
--> Specimen/Notes/OriginalNotes (nicht decisive, ohne Pre/Post)

Gender
--> wird nicht importiert

weitere Einstellungen:

    Attachment: als "Import as new data" markiert
    Merging: alles auf "Insert"
    Project 1: ProjectID: "For all: Araneae" (als decisive markiert)
    Part 1: MaterialCategory: "For all: preserved specimen" (als decisive markiert)
    Part 1/Storage/CollectionID: "For all: Section Arthropoda / Sektion Niedere Arthropoda" (als decisive markiert)
    Organism 1/Taxonomic Group: "For all: arthropod" (als decisive markiert)
    Organism 1/Hierarchy, name/LastIdentificationCache: "For all: 1" (nicht decisive)
