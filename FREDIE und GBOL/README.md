*Anhängen der BOLD Process ID und Genbank Accession Nummer an schon in DWB bestehende Datensätze.*


**In der Excel-Tabelle vorhandene Spalten und ihre Zuordnung in DWB (für DWB Version 3.0.7.8)**


_Acc.Nr._  
-> wird nicht importiert (da für die Datensätze nicht eindeutig)  


_specimen ID_  
-> Specimen/CollectionSpecimenID (als decisive markiert, mit gelben Schlüssel markiert, soll mit vorhandenen Datensatz verknüpfen)  


_ Dep.Acc.Nr._  
-> wird nicht importiert  


_BOLD Process ID_  
-> Relation 1/RelatedSpecimenURI (als decisive markiert; mit Pre.: "http://www.boldsystems.org/index.php/Public_RecordView?processid=")  
-> Relation 1/RelatedSpecimenDisplayText (nicht decisive; mit Pre.: "http://www.boldsystems.org/index.php/Public_RecordView?processid=")  
-> Relation 1/ RelatedSpecimenDescription (nicht decisive, mit Pre.: "BOLD ProcessID: ")  



_COI-5P-Accession_  
-> Relation 1/Notes (nicht decisive, mit Pre.: "COI-5P Genbank Accession: ")


_Institut_  
-> Specimen/ExternalDatasourceID (nicht decisive, mit Transformation: Translation: MfN -> MfN (16); ZFMK -> ZFMK-Ichthyologie (19); ZSM -> ZSM (17))  

 






_Zusätzliche Einstellungen:_  
- Attachment: Specimen/CollectionSpecimenID    
- Merging: Specimen auf Update (da die externe data source geändert wird)  
- Merging: Project 1: Attach (da nur ein Projekt angegeben wird, aber einige Datensätze zwei Projekten zugeordnet sind)  
- Merging: Relation 1: Insert  
- Project 1: ProjektID: For all: FREDIE (mit gelbem Schlüssel zum Vergleich markiert)  
- Relation 1: RelationType: For all: Public database)
- Relation 1: IsInternalRelationCache: For all: nicht angehakt (man muss erst einmal anhaken und dann das Häkchen wieder wegmachen; dadurch wird 0 für eine externe Relation gesetzt, 1 steht für eine DWB-interne Relation)  

