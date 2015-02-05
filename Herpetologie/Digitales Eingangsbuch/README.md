Importschema zum neuen Digitalen Eingangsbuch
In der excel-Tabelle vorhandene Spalten und ihre Zuordnung im Import Wizard (DWB Version 3.0.7.6):

Code
--> Specimen/Accession/AccessionNumber (als decisive markiert)
--> Part 1/AccessionNumber (als decisive markiert)
--> Transaction 1.1/AccessionNumber (nicht decisive)
--> Organism 1/TaxonomicGroup (als decisive markiert, Filter: Translation: AMP -> amphibian, REP-> reptile)
--> Project 1/ProjectID (als decisive markiert, Filter: Translation: AMP -> Amphibiam ausw�hlen, Projektnr. 36813, REP-> reptiles ausw�hlen, Projektnr. 36812)

ZFMK
--> Specimen/Accession/AccessionNumber (addiert, als decisive markiert, Pre: Leerzeichen)
--> Part 1/AccessionNumber (addiert, als decisive markiert, Pre: Leerzeichen)
--> Transaction 1.1/AccessionNumber (addiert, nicht decisive, Pre: Leerzeichen)

Prep
--> Part 1/MaterialCategory (nicht decisive, Filter: Translation: ALK -> preserved specimen; OST -> bones)

Species / Genus
--> Identification 1.1/TaxonomicName (als decisive markiert)

Species
--> Identification 1.1/TaxonomicName (addiert, nicht decisive)

Subspecies
--> Identification 1.1/TaxonomicName (addiert, nicht decisive)

Quali. --> Identification 1.1/IdentificationQualifier (nicht decisive, Filter: Translation)

Type
--> Identification 1.1/TypeStatus (nicht decisive, Filter: Translation: HT -> Holotype, PT -> paratype)

Sex --> Organism 1/Gender (nicht decisive, Filter: Translation: f und w -> female, m -> male, juv -> juvenil)

Age --> Organism 1/LifeStage (nicht decisive, Filter: Translation: ad -> adult, immat -> immature, juv -> juvenil, larva -> larval, subad -> subadult)

Locality Country
--> Event/CountryCache (f�r Vergleich mit Schl�ssel markiert)

Admin1
--> Named area (Diversity Gezetteer)/Location (als decisive markiert, f�r Vergleich mit Schl�ssel markiert)

Locality
--> Event/LocalityDescription (als decisive markiert, f�r Vergleich mit Schl�ssel markiert)

Lat WGS84
--> Coordinates WGS84/Lat.(NS) (nicht decisive, f�r Vergleich mit Schl�ssel markiert)

Long WGS84 --> Coordinates WGS84/Long.(EW) (als decisive markiert, f�r Vergleich mit Schl�ssel markiert)

Alt (mNN) --> Altitude (mNN)/Alt.from (als decisive markiert, f�r Vergleich mit Schl�ssel markiert; Filter: Schere: Position1, Splitter ist Semikolon)
--> Altitude (mNN)/Alt.to (nicht decisive, f�r Vergleich mit Schl�ssel markiert; Filter: Schere: Position2, Splitter ist Semikolon)

Remarks
--> Event/Notes (nicht decisive)

Collected Y
--> Event/Date and Time/CollectionYear (als decisive markiert, f�r Vergleich mit Schl�ssel markiert)

M --> Event/Date and Time/CollectionMonth (nicht decisive, f�r Vergleich mit Schl�ssel markiert)

D
--> Event/Date and Time/CollectionDay (nicht decisive, f�r Vergleich mit Schl�ssel markiert)

period
--> Event/Date and Time/CollectionDateSupplement (nicht decisive, f�r Vergleich mit Schl�ssel markiert)

Leg. --> Agent 1/CollectorsName (als decisive markiert; Filter: Schere: Position 1, Splitter ist Semikolen)
zus�tzlich ist bei "Agent 1/DataWithholdingReason/for all: nicht!" eingetragen (die Sammler sollen nicht ver�ffentlich werden)
--> bei Agent 2 bis 5 analoge Einstellungen zu Agent 1

Fieldnr.
--> Event/CollectorsEventNumber (nicht decisive)

Old collectionnr.
--> Specimen/Depositor/DepositorsAccessionNumber (nicht decisive)

Iventory Y
--> Specimen/Accession/AccessionYear (nicht decisive)

M2
--> Specimen/Accession/AccessionMonth (nicht decisive)

Dedit
--> Specimen/Depositor/DepositorsName (nicht decisive)

General Remarks
--> Specimen/Notes/OriginalNotes (nicht decisive)

last modified
--> Specimen/Notes/AdditionalNotes (nicht decisive)

nicht mehr im Bestand
--> Transaction 1.1/TransactionID/for all: Transfer_Herpetologie (als decisive markiert)

zus�tzliche Einstellungen:

    Attachment: "Import as new data" eingestellt
    Merging: Event, Coordinates WGS84, Named area und Altitude auf Merge eingestellt --> wenn alle Daten gleich sind, wird nur ein Fundort angelegt (ersichtlich an der EventID)
    (Vorsicht: Bei der �nderung des Fundortes in einem Datensatz, wird dieser Fundort auch in allen anderen Datens�tzen automatisch ge�ndert.)
    alle anderen Eingaben (Specimen bis Agent) stehen auf "Insert"