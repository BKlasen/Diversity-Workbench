**Importschema zum neuen Digitalen Eingangsbuch**

***In der excel-Tabelle vorhandene Spalten und ihre Zuordnung im Import Wizard (DWB Version 3.0.7.6):***

_Code_    
-->  Specimen/Accession/AccessionNumber (als decisive markiert)  
-->  Part 1/AccessionNumber (als decisive markiert)  
-->  Transaction 1.1/AccessionNumber (nicht decisive)  
-->  Organism 1/TaxonomicGroup (als decisive markiert, Filter: Translation: AMP -> amphibian, REP-> reptile)  
-->  Project 1/ProjectID (als decisive markiert, Filter: Translation: AMP -> Amphibiam auswählen, Projektnr. 36813, REP-> reptiles auswählen, Projektnr. 36812)

_ZFMK_  
-->  Specimen/Accession/AccessionNumber (addiert, als decisive markiert, Pre: Leerzeichen)  
-->  Part 1/AccessionNumber (addiert, als decisive markiert, Pre: Leerzeichen)  
-->  Transaction 1.1/AccessionNumber (addiert, nicht decisive, Pre: Leerzeichen)  

_Prep_  
-->  Part 1/MaterialCategory (nicht decisive, Filter: Translation: ALK -> preserved specimen; OST -> bones)  

_Species / Genus_  
--> Identification 1.1/TaxonomicName (als decisive markiert)

_Species_  
--> Identification 1.1/TaxonomicName (addiert, nicht decisive)  

_Subspecies_  
--> Identification 1.1/TaxonomicName (addiert, nicht decisive)  

_Quali._
--> Identification 1.1/IdentificationQualifier (nicht decisive, Filter: Translation)  

_Type_  
--> Identification 1.1/TypeStatus (nicht decisive, Filter: Translation: HT -> Holotype, PT -> paratype)  

_Sex_
--> Organism 1/Gender (nicht decisive, Filter: Translation: f und w -> female, m -> male, juv -> juvenil)  

_Age_
--> Organism 1/LifeStage (nicht decisive, Filter: Translation: ad -> adult, immat -> immature, juv -> juvenil, larva -> larval, subad -> subadult)  

_Locality Country_  
--> Event/CountryCache (für Vergleich mit Schlüssel markiert)  

_Admin1_  
--> Named area (Diversity Gezetteer)/Location (als decisive markiert, für Vergleich mit Schlüssel markiert)  

_Locality_  
-->  Event/LocalityDescription (als decisive markiert, für Vergleich mit Schlüssel markiert)  

_Lat WGS84_  
--> Coordinates WGS84/Lat.(NS) (nicht decisive, für Vergleich mit Schlüssel markiert)  

_Long WGS84_
--> Coordinates WGS84/Long.(EW) (als decisive markiert, für Vergleich mit Schlüssel markiert)  

_Alt (mNN)_
--> Altitude (mNN)/Alt.from (als decisive markiert, für Vergleich mit Schlüssel markiert; Filter: Schere: Position1, Splitter ist Semikolon)  
--> Altitude (mNN)/Alt.to (nicht decisive, für Vergleich mit Schlüssel markiert; Filter: Schere: Position2, Splitter ist Semikolon)  

_Remarks_  
--> Event/Notes (nicht decisive)  

_Collected Y_  
--> Event/Date and Time/CollectionYear (als decisive markiert, für Vergleich mit Schlüssel markiert)  

_M_
--> Event/Date and Time/CollectionMonth (nicht decisive, für Vergleich mit Schlüssel markiert)  

_D_  
--> Event/Date and Time/CollectionDay (nicht decisive, für Vergleich mit Schlüssel markiert)  

_period_  
--> Event/Date and Time/CollectionDateSupplement (nicht decisive, für Vergleich mit Schlüssel markiert)  

_Leg._
-->  Agent 1/CollectorsName (als decisive markiert; Filter: Schere: Position 1, Splitter ist Semikolen)  
zusätzlich ist bei "Agent 1/DataWithholdingReason/for all: nicht!" eingetragen (die Sammler sollen nicht veröffentlich werden)  
--> bei Agent 2 bis 5 analoge Einstellungen zu Agent 1  

_Fieldnr._  
--> Event/CollectorsEventNumber (nicht decisive)  

_Old collectionnr._  
--> Specimen/Depositor/DepositorsAccessionNumber (nicht decisive)  

_Iventory Y_  
--> Specimen/Accession/AccessionYear  (nicht decisive)  

_M2_  
--> Specimen/Accession/AccessionMonth  (nicht decisive)  

_Dedit_  
--> Specimen/Depositor/DepositorsName  (nicht decisive)  

_General Remarks_  
--> Specimen/Notes/OriginalNotes  (nicht decisive)  

_last modified_  
--> Specimen/Notes/AdditionalNotes  (nicht decisive)  

_nicht mehr im Bestand_  
--> Transaction 1.1/TransactionID/for all: Transfer_Herpetologie  (als decisive markiert)  


***weitere Einstellungen:***
* Attachment: "Import as new data" eingestellt  
* Merging: Event, Coordinates WGS84, Named area und Altitude auf Merge eingestellt --> wenn alle Daten gleich sind, wird nur ein Fundort angelegt (ersichtlich an der EventID)   
(Vorsicht: Bei der Änderung des Fundortes in einem Datensatz, wird dieser Fundort auch in allen anderen Datensätzen automatisch geändert.)  
* alle anderen Eingaben (Specimen bis Agent) stehen auf "Insert"  
