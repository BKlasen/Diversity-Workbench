## Import Lautlabor  - Teil 2 - individuals

### In der excel-Tabelle (Register audio files individuals.xlsx) vorhandene Spalten und ihre Zuordnung im Import Wizard (DWB Version 3.0.7.7)  



_lfd Nr._  
--> Specimen/AccessionNumber (als decisive markiert, zum Vergleich mit Schlüssel markiert, muss blau hinterlegt sein)  
--> Analysis 1.1/AnalysisNumber (nicht decisive)  


_tape no._ (laufende Nummer des Bandes, dreistellig)    
wird nicht importiert  


_take no._ (Nr. des Takes auf dem Band, dreistellig)  
wird nicht importiert   
  

_genus_  
--> Identification 1.1/Taxonomic name (nicht decisive)  
  

_species_  
--> Identification 1.1/Taxonomic name (addiert, nicht decisive, mit Pre.: Leerzeichen)  


_sex_  
--> Organism 1/Gender (nicht decisive)  


_age class/age_  
--> Organism 1/Life stage (nicht decisive)  


_individual (name)_  
--> Identification 1.1/Notes (nicht decisive; mit Pre.: "personal name:" + Leerzeichen)  



_recording locality - circumstances_  
--> Organism 1/Circumstances (nicht decisive)  



_recording distance_  
--> Analysis 1.1/Method 1.1.1/Parameter1.1.1.1/ **ParameterValue** (nicht decisive)  
-->       _zusätzlich_: Analysis 1.1/Method 1.1.1/Parameter1.1.1.1/ **ParameterID**: For all "Sound data (Analysis): Distance (in m)"  (als decisive markiert)  



_change of rec distance_  
--> Analysis 1.1/Method 1.1.1/Parameter1.1.1.2/ **ParameterValue** (nicht decisive)  
-->       _zusätzlich_: Analysis 1.1/Method 1.1.1/Parameter1.1.1.2/ **ParameterID**: For all "Sound data (Analysis): Change of Distance"  (als decisive markiert)  



_vocalization type(s)_  
--> Analysis 1.1/Method 1.1.1/Parameter1.1.1.3/ **ParameterValue** (nicht decisive)  
-->       _zusätzlich_: Analysis 1.1/Method 1.1.1/Parameter1.1.1.3/ **ParameterID**: For all "Sound data (Analysis): Vocalization Types(s)"  (als decisive markiert)  




_behavioural context(s)_  
--> Analysis 1.1/Method 1.1.1/Parameter1.1.1.4/ **ParameterValue** (nicht decisive)  
-->       _zusätzlich_: Analysis 1.1/Method 1.1.1/Parameter1.1.1.4/ **ParameterID**: For all "Sound data (Analysis): Call Type(s)"  (als decisive markiert)  


_individual start_  
--> Analysis 1.1/Method 1.1.1/Parameter1.1.1.5/ **ParameterValue** (nicht decisive)  
-->       _zusätzlich_: Analysis 1.1/Method 1.1.1/Parameter1.1.1.5/ **ParameterID**: For all "Sound data (Analysis): Individual start"  (als decisive markiert)  



_individual stop_  
--> Analysis 1.1/Method 1.1.1/Parameter1.1.1.6/ **ParameterValue** (nicht decisive)  
-->       _zusätzlich_: Analysis 1.1/Method 1.1.1/Parameter1.1.1.6/ **ParameterID**: For all "Sound data (Analysis): Individual stop"  (als decisive markiert)  




_orig rec overloaded_  
--> Analysis 1.1/Method 1.1.1/Parameter1.1.1.7/ **ParameterValue** (nicht decisive, mit Transformation: Translation: 0 -> no, 1 -> low, 2 -> moderate, 3 -> high)  
-->       _zusätzlich_: Analysis 1.1/Method 1.1.1/Parameter1.1.1.7/ **ParameterID**: For all "Sound data (Analysis): Overloaded"  (als decisive markiert)  



_recording quality_  
--> Analysis 1.1/Method 1.1.1/Parameter1.1.1.8/ **ParameterValue** (nicht decisive, mit Transformation: Translation: 0 -> poor, 1 -> low, 2 -> moderate, 3 -> medium, 4 -> good, 5 -> very good)  
-->       _zusätzlich_: Analysis 1.1/Method 1.1.1/Parameter1.1.1.8/ **ParameterID**: For all "Sound data (Analysis): Recording Quality"  (als decisive markiert)  


_editing_  
--> Analysis 1.1/Method 1.1.1/Parameter1.1.1.9/ **ParameterValue** (nicht decisive)  
-->       _zusätzlich_: Analysis 1.1/Method 1.1.1/Parameter1.1.1.9/ **ParameterID**: For all "Sound data (Analysis): Editing"  (als decisive markiert)  



_editor_  
--> Analysis 1.1/Method 1.1.1/Parameter1.1.1.10/ **ParameterValue** (nicht decisive)  
-->       _zusätzlich_: Analysis 1.1/Method 1.1.1/Parameter1.1.1.10/ **ParameterID**: For all "Sound data (Analysis): Editor"  (als decisive markiert)  




_**weitere Einstellungen:**_  

-  Attachment: als Attachment markiert, verknüpft (angehakt) durch die AccessionNumber  
-  Merging: Specimen und Project 1 auf "Attach"; alles weitere auf "Insert"  
-  Project 1: ProjectID: "For all: Amibio oder ZFMK-Test" (als decisive markiert, wichtig: muss mit 1. Tabelle übereinstimmen)  
-  Analysis 1.1/AnalysisID (als decisive markiert, "For all: Soundfile", wichtig, da Sound data (Analysis) Soundfile zugeordnet ist und sonst ein foreign key Fehler kommt)  
-  Analysis 1.1/Methode 1.1.1/MethodID: "For all: Sound data (Analysis)" (als decisive markiert)
-  Identification 1.1/IdentificationSequence: "For all: 1" (als decisive markiert)  
-  Organism 1/Taxonomic Group: "For all: animal" (als decisive markiert)  
-  Organism 1/OnlyObserved: "For all: angehakt" (nicht decisive)  
-  Organism 1/Hierarchy, name/LastIdentificationCache: "For all: 1" (als decisive markiert)





