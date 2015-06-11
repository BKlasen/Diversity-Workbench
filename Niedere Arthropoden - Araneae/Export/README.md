***In der DWB vorhandene Datenfelder und ihre Zuordnung beim Export (Version 3.0.7.9zl- für Relations):***

_Specimen / AccessionNumber_  
-->  Catalog Nr.  (dort wird die vom Script vergebene Übergangsnr. (mit AAC) eingetragen, diese kann später überschrieben werden und die richtige Sammlungsnummer eingetragen werden)


_Specimen / CollectionSpecimenID_  
---> Collection Specimen ID (zur sicheren Zuordnung, da später die Catalog Nr. überschrieben wird)


_Organism 1 / Identification 1.1 / TypeStatus_  
--> Type Status (mit Transformation: Translation: Holotype wird HT, Paratype zu PT, etc.)  


_Specimen / DataWithholding Reason_  
--> Reservierung


_Organism1 / FamilyCache_    
-->  Family


_Organism1 / Identification1.1 / Taxonomic Name_  
--> Genus Name (mit Transformation: Splitter, Position 1, Trennzeichen : Leerzeichen)  


_Organism1 / Identification1.1 / Taxonomic Name_  
--> Species Name (mit Transformation: Splitter, Position 2, Trennzeichen : Leerzeichen)  


_Organism1 / Identification1.1 / Taxonomic Name_  
--> Author (mit Transformation: Splitter, Position 3, Trennzeichen : Leerzeichen; Replace, ersetze "(" durch "Nichts" und Replace, ersetze "," durch "nichts")  


_Organism1 / Identification1.1 / Taxonomic Name_  
--> Date descr. (mit Transformation: Splitter, Position 4, Trennzeichen : Leerzeichen; Replace: ersetze ")" durch "nichts")  


_Organism1 / Identification1.1 / Taxonomic Name_  
--> _Species  
 
 
_Organism1 / Identification1.1 / ResponsibleName_  
--> Determined by


_Organism1 / Identification1.1 / Identification Year_  
--> Date det.  


_Event / CountryCache_  
--> Country  


_Event / Plot / Location 1_  
--> Admin.


_Event / LocalityDescription_  
--> Locality  


_Event / WGS84 / AverageLatitudeCache_  
--> Lat_dec  


_Event / WGS84 / AverageLongitudeCache_  
--> Long_dec  


_Event / WGS84 / LocationAccuracy_  
--> coord_uncertainty_flag  


_Event / WGS84 / RecordingMethod_  
--> coord_info  


_Event / HabitatDescription_  
--> Ecology  


_Event / Altitude / AverageAltitudeCache_  
--> Altitude (m)  


_Event / CollectionYear_  
--> Coll_Year  


_Event / CollectionDate_  
--> Coll_Date (mit Transformation: Splitter: Position 1, Trennzeichen "Leerzeichen") dadurch wird der Stunden/Minuten-Teil abgeschnitten  


_Specimen / Collector 1 / CollectorsName_  
--> Collectors  


_Specimen / Collector 2 / CollectorsName_  
--> Collectors  (mit Pre: ", "; den Spaltentrenner (dunkelgrauer Balken zwischen den Spalten anklicken -> wird aufgehoben (hellgrau) und alle Sammler werden in eine Spalte geschrieben)  


_Specimen / Collector 3 / CollectorsName_  
--> Collectors  (mit Pre: ", "; den Spaltentrenner (dunkelgrauer Balken zwischen den Spalten anklicken -> wird aufgehoben (hellgrau) und alle Sammler werden in eine Spalte geschrieben)  


_Specimen / Organism 1 / Gender_  
--> male (mit Transformation: Filter: "Export fixed value "1" if content in column "Organism 1, Gender" = male"), die aktive Spalte ist gelb hinterlegt, falls man andere Spalten verschiebt, erscheint eine Warnmeldung, diese wieder anzupassen)  


_Specimen / Organism 1 / Gender_  
--> female (mit Transformation: Filter: "Export fixed value "1" if content in column "Organism 1, Gender" = female"), die aktive Spalte ist gelb hinterlegt, falls man andere Spalten verschiebt, erscheint eine Warnmeldung, diese wieder anzupassen)  


_Specimen / Organism 1 / NumberOfUnits_  
--> Anzahl  


_Specimen / OriginalNotes_  
--> Notes  


_Specimen / Organism 1 / Gender_  
--> Gender  


_Specimen / Relation invers 1 / RelatedSpecimenAccessionNumber_  
--> GBOL-LaborNummer (die Nummer, die im Labor als Probennummer vergeben wird (ZFMK-TIS-...)  


_Specimen / Identification 1.1 / IdentificationUnitID_  
--> IdentificationUnitID (für den Reimport)  


_Specimen / Identification 1.1 / IdentificationSequence_  
--> IdentificationSequence (für den Reimport)  


_Event / CollectionEventID_  
--> CollectionEventID  



_weitere Hinweise:_  
- der Export der zu dem Datensatz in Relation stehenden AccessionNumber (GBOL-Labor-Nummer) geht erst ab DWB Version 3.0.7.9zl  
- die exportierte Datei wird immer in den Ordner "Export" der verwendeten DWB-Version gespeichert; man kann einen anderen Speicherort auswählen, aber es wird immer der übergeordnetet Ordner von dem Ordner, den man ausgewählt hat, genommen; dies muss man bei jedem Start neu einstellen  
- um die Koordinaten richtig in Excel anzeigen zu lassen, s. bei Allgemeines  
- im Tab "Export" nicht auf die Anzeige "Reading data" warten, sondern direkt "Export data" anklicken
