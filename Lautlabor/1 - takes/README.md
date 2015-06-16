## Import Lautlabor  - Teil 1 - takes

### In der excel-Tabelle (Register audio files takes.xlsx) vorhandene Spalten und ihre Zuordnung im Import Wizard (DWB Version 3.0.7.7)  

_lfd Nr._  
--> Specimen/AccessionNumber (als decisive markiert)  
--> Part 1/AccessionNumber (nicht decisive)  
--> Part 1/Notes (nicht decisive; mit Pre.: "ZFMK audio file no.:" + Leerzeichen; mit Post.: Leerzeichen + ; + Leerzeichen)  


_tape no._ (laufende Nummer des Bandes, dreistellig)    
--> Part 1/Notes (addiert, nicht decisive, mit Pre.: "tape no.:" + Leerzeichen; mit Post: Leerzeichen + ; + Leerzeichen)  


_take no._ (Nummer des Takes auf dem Band, dreistellig, wird auf jedem Band neu gezählt)  
--> Part 1/Notes (addiert, nicht decisive, mit Pre.: "take no.:" + Leerzeichen, mit Post: Leerzeichen + ; + Leerzeichen)  


_prior tape identification_  
--> Specimen/Depositor/DepositorsAccessionNumber (als decisive markiert)  


_take start [min:sec:msec]_  
--> Method 1/Parameter1.1/ **ParameterValue** (nicht decisive)  
-->       _zusätzlich_: Method 1/Parameter 1.1/ **ParameterID**: For all "Sound data (Gathering): take start" (als decisive markiert)   
--> Part 1/Notes (addiert; nicht decisive, mit Pre.: "take start:" + Leerzeichen, mit Post: Leerzeichen + ; + Leerzeichen)  


_take end [min:sec:msec]_  
--> Method 1/Parameter1.2/ **ParameterValue** (nicht decisive)  
-->       _zusätzlich_: Method 1/Parameter 1.2/ **ParameterID**: For all "Sound data (Gathering): take stop" (als decisive markiert)  
--> Part 1/Notes (addiert; nicht decisive, mit Pre.: "take end:" + Leerzeichen)  


_tape type_  
--> Method 1/Parameter1.3/ **ParameterValue** (nicht decisive)  
-->       _zusätzlich_: Method 1/Parameter 1.3/ **ParameterID**: For all "Sound data (Gathering): Tape Type"  (als decisive markiert)  


_recorder type_  
--> Method 1/Parameter1.4/ **ParameterValue** (nicht decisive)  
-->       _zusätzlich_: Method 1/Parameter 1.4/ **ParameterID**: For all "Sound data (Gathering): Recorder Type"  (als decisive markiert)  


_microphone type_  
--> Method 1/Parameter1.5/ **ParameterValue** (nicht decisive)  
-->       _zusätzlich_: Method 1/Parameter 1.5/ **ParameterID**: For all "Sound data (Gathering): Microphone Type"  (als decisive markiert)  


_microphone windshield_  
--> Method 1/Parameter1.28/ **ParameterValue** (nicht decisive)  
-->       _zusätzlich_: Method 1/Parameter 1.28/ **ParameterID**: For all "Sound data (Gathering): Microphone Windshield"  (als decisive markiert)  


_recordist_  
--> Agent 1/CollectorsName (als decisive markiert)  


_analog/digital_  
--> Method 1/Parameter1.6/ **ParameterValue** (nicht decisive)  
-->       _zusätzlich_: Method 1/Parameter 1.6/ **ParameterID**: For all "Sound data (Gathering): analog/digital"  (als decisive markiert)  


_original rec speed_  
--> Method 1/Parameter1.7/ **ParameterValue** (nicht decisive)  
-->       _zusätzlich_: Method 1/Parameter 1.7/ **ParameterID**: For all "Sound data (Gathering): Speed"  (als decisive markiert)  


_rec orig/copy/n-te copy_  
--> Method 1/Parameter1.8/ **ParameterValue** (nicht decisive)  
-->       _zusätzlich_: Method 1/Parameter 1./ **ParameterID**: For all "Sound data (Gathering): Origin"  (als decisive markiert)  


_input level set manual/auto_  
--> Method 1/Parameter1.9/ **ParameterValue** (nicht decisive)  
-->       _zusätzlich_: Method 1/Parameter 1.9/ **ParameterID**: For all "Sound data (Gathering): Input level set"  (als decisive markiert)  


_input level in take constant/changed_  
--> Method 1/Parameter1.10/ **ParameterValue** (nicht decisive)  
-->       _zusätzlich_: Method 1/Parameter 1.10/ **ParameterID**: For all "Sound data (Gathering): input level constant"  (als decisive markiert)  


_orig rec mono/stereo_  
--> Method 1/Parameter1.11/ **ParameterValue** (nicht decisive)  
-->       _zusätzlich_: Method 1/Parameter 1.11/ **ParameterID**: For all "Sound data (Gathering): Channel"  (als decisive markiert)  


_tracks recorded_  
--> Method 1/Parameter1.12/ **ParameterValue** (nicht decisive)  
-->       _zusätzlich_: Method 1/Parameter 1.12/ **ParameterID**: For all "Sound data (Gathering): Tracks"  (als decisive markiert)  


_file name_  
--> Part 1/Storage/StorageLocation (nicht decisive)  
         

_format_  
--> Method 1/Parameter1.13/ **ParameterValue** (nicht decisive)  
-->       _zusätzlich_: Method 1/Parameter 1.13/ **ParameterID**: For all "Sound data (Gathering): fileformat"  (als decisive markiert)  


_sampling rate_  
--> Method 1/Parameter1.14/ **ParameterValue** (nicht decisive)  
-->       _zusätzlich_: Method 1/Parameter 1.14/ **ParameterID**: For all "Sound data (Gathering): Samplingrate"  (als decisive markiert)  

_bitrate_  
--> Method 1/Parameter1.15/ **ParameterValue** (nicht decisive)  
-->       _zusätzlich_: Method 1/Parameter 1.15/ **ParameterID**: For all "Sound data (Gathering): Bitrate"  (als decisive markiert)  


_recording locality - Country_  
--> Event/CountryCache (als decisive markiert)  


_recording locality City/Locality_  
--> Event/LocalityDescription (nicht decisive)  


_recording date_  
--> Event/Date and Time/CollectionDateSupplement  (nicht decisive)  


_timeOfDay_  
--> Method 1/Parameter1.16/ **ParameterValue** (nicht decisive)  
-->       _zusätzlich_: Method 1/Parameter 1.16/ **ParameterID**: For all "Sound data (Gathering): timeOfDay"  (als decisive markiert)  


_weather during take_  
--> Method 1/Parameter1.17/ **ParameterValue** (nicht decisive)  
-->       _zusätzlich_: Method 1/Parameter 1.17/ **ParameterID**: For all "Sound data (Gathering): Weather"  (als decisive markiert)  


_background noise_  
--> Method 1/Parameter1.18/ **ParameterValue** (nicht decisive; mit Transformation: Translation 0 -> no, 1 -> low, 2 -> medium, 3 -> high)  
-->       _zusätzlich_: Method 1/Parameter 1.18/ **ParameterID**: For all "Sound data (Gathering): Background noise"  (als decisive markiert)  


_recorded in-/outdoors_  
--> Method 1/Parameter1.19/ **ParameterValue** (nicht decisive)  
-->       _zusätzlich_: Method 1/Parameter 1.19/ **ParameterID**: For all "Sound data (Gathering): Recording framework conditions"  (als decisive markiert)  


_comments_  
--> Specimen/Notes/OriginalNotes (nicht decisive)  


_License_  
--> Method 1/Parameter1.20/ **ParameterValue** (nicht decisive)  
-->       _zusätzlich_: Method 1/Parameter 1.20/ **ParameterID**: For all "Sound data (Gathering): License"  (als decisive markiert)  


_Copyright_  
--> Method 1/Parameter1.21/ **ParameterValue** (nicht decisive)  
-->       _zusätzlich_: Method 1/Parameter 1.21/ **ParameterID**: For all "Sound data (Gathering): Copyright"  (als decisive markiert)  


_Owner_  
--> Method 1/Parameter1.22/ **ParameterValue** (nicht decisive)  
-->       _zusätzlich_: Method 1/Parameter 1.22/ **ParameterID**: For all "Sound data (Gathering): Owner"  (als decisive markiert)  


_Creator_   
--> Method 1/Parameter1.23/ **ParameterValue** (nicht decisive)  
-->       _zusätzlich_: Method 1/Parameter 1.23/ **ParameterID**: For all "Sound data (Gathering): Creator"  (als decisive markiert)  


_Hardware_   
--> Method 1/Parameter1.24/ **ParameterValue** (nicht decisive)  
-->       _zusätzlich_: Method 1/Parameter 1.24/ **ParameterID**: For all "Sound data (Gathering): Hardware"  (als decisive markiert)  


_Software_  
--> Method 1/Parameter1.25/ **ParameterValue** (nicht decisive)  
-->       _zusätzlich_: Method 1/Parameter 1.25/ **ParameterID**: For all "Sound data (Gathering): Software"  (als decisive markiert)  


_Software Samplingrate_  
--> Method 1/Parameter1.26/ **ParameterValue** (nicht decisive)  
-->       _zusätzlich_: Method 1/Parameter 1.26/ **ParameterID**: For all "Sound data (Gathering): Software Samplingrate"  (als decisive markiert)  


_Software Bitrate_  
--> Method 1/Parameter1.27/ **ParameterValue** (nicht decisive)  
-->       _zusätzlich_: Method 1/Parameter 1.27/ **ParameterID**: For all "Sound data (Gathering): Software Bitrate"  (als decisive markiert)  


_Personen Name gesperrt ?_  
--> Agent 1/DataWithholdingReason (nicht decisive)  


_Datensatz gesperrt_  
--> Specimen/DataWithholdingReason (nicht decisive)  




_**weitere Einstellungen:**_  

-  Attachment: als "Import as new data" markiert  
-  Merging: alles auf "Insert"  
-  Method 1/MethodID: "For all: Sound data (Gathering)" (als decisive markiert, wichtig: richtige Methode auswählen, sonst gibt es Foreign Key-Fehler)
-  Project 1: ProjectID: "For all: Amibio oder ZFMK-Test" (als decisive markiert, wichtig: es muss mit der zweiten Datei übereinstimmen)  
-  Part 1: MaterialCategory: "For all: sound" (als decisive markiert)  
-  Part 1/Storage/CollectionID: "For all: ZFMK" (als decisive markiert)  





