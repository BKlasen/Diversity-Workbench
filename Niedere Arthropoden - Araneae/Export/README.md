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


