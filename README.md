# 3d-print-helper
Eine visuelle Umgebung, die es ermöglicht barrierefrei 3D Modelle zu slicen und auf einen USB Stick zu exportieren.

Diese Software wurde explizit für die Nutzung durch Menschen mit Sehbeeinträchtigungen entwickelt. Slicer Porgramme weisen komplexe visuelle Userinterfaces auf, die es Menschen mit Sehbeeinträchtigung nicht ermöglichen, die selbstständig zu bedienen. Diese Software nutzt die Command-Line-Interface Versionen von PrusaSlicer und eine grafische Oberfläche die für die barrierefreie Nutzung geeignet ist.

Es wird der PrusaSlicer und ein Prusa Drucker hier verwendet, weil die Prusa Drucker die Eigenschaft haben automatisch die neueste gcode Datei auf einem angeschlossenen USB Stick zu öffnen. Der Prozess muss am Drucker also nur noch gestartet werden. Eine weitere Auswahl ist nicht notwendig.

Voraussetzungen:
1. Windows Betriebssystem
2. PrusaSlicer ist auf dem System installiert -> [Download & Installation](https://www.prusa3d.com/en/page/prusaslicer_424/)
3. Python ist auf dem System installiert (optional)

Im Ordner "working-executable" des Repositories befindet sich eine vollständig eigenständige Version des 3D Print Helpers. Es ist für die Nutzung nicht notwendig eine Pythoninstallation auf dem System zu haben.

### Interaktion mit dem 3D Print Helper
Das Programm besteht aus den folgenden Elementen, die in den nächsten Schritten näher beschrieben werden:
- einem Dropdownmenü zur Auswahl des Druckerprofils
- Button zur Auswahl von 3D Modellen
- ein Textfeld, dass den Namen der ausgewählten Datei anzeigt
- Button zum Start des Slicens
- Button zur Auswahl des Dateipfades zum Slicer
- Button zum Beenden des Helpers

Zusätzlich gibt das Programm Audiosignale aus, wenn eine Aktion abgeschlossen ist.
Ein einfaches kurzes Signal gibt an, dass die Aktion erfolgreich war. Ein doppeltes kurzes Signal, das ein Fehler aufgetreten ist.

## Einrichtung des Programms
Es sind zwei Schritte zur Einrichtung notwendig.
### 1. Erstellung eine Konfigurationsdatei
Um das Programm zu nutzen, muss eine Konfigurationsdatei des Druckers erstellt werden. Sie enthält Informationen über den Drucker, die Druckereinstellungen, das verwendete Material und weitere Parameter.
Im Ordner config_files sind standardmäßig drei verschiedene Profile enthalten. Alle für den Prusa Mini. Sie heißen PrusaMini10, PrusaMini15 und PrusaMini20. Die zahl gibt jeweils an, wie hoch die einzelnen Druckschichten sind. Eine geringere Zahl bedeutet, eine feinere Auflösung.

Eigene Profile können im PrusaSlicer erstellt und in den Ordner config_files kopiert werden. Das Programm wird sie beim Starten automatisch laden. Eine Anleitung [hier](https://help.prusa3d.com/de/article/wie-importiert-und-exportiert-man-benutzerdefinierte-profile-in-prusaslicer_382766).

[ACHTUNG] Bei der Dateibennenung muss darauf geachtet werden, dass sie keine Leerzeichen, Sonderzeichen oder Umlaute enthält.

### 2.Der Slicer Pfad
Diese Einstellung muss einmalig vorgenommen werden. Das 3D Print Helper Programm greift auf die Command Line Interface (CLI) Version des Prusa Slicers zu. Hierzu wird der Pfad benötigt. Wurden bei der Installation des Prusa Slicers die Standardeinstellungen gewählt, befindet sich das Programm normalerweise im Ordner "C:/Programme/Prusa3D/PrusaSlicer". Der Name des CLI Tools ist "prusa-slicer-console.exe"

Das 3D Print Helper Programm hat eine Schaltfläche integriert, über die diese Datei gesucht werden kann. Nach einmaliger Auswahl hierrüber, wird der Pfad in der Datei "slicerpath.txt" gespeichert und muss nicht erneut eingegeben werden.


## Slicen
Um eine Datei zu Slicen müssen die folgenden Bedingungen erfüllt sein:
- eine 3D Modell Datei vom Typ STL wurde ausgewählt
- der Slicer Pfad wurde einmalig einrichtet
- ein Druckerprofil wurde ausgewählt (standardmäßig ist das erste Profil im Ordner ausgewählt)

Beim Start des Slicens ögffnet sich ein Menü in dem ein Speicherort und ein Dateiname gewählt werden. Es bietet sich an hierfür im Vorfeld einen USB-Stick an den Computer zu stecken um die Datei direkt darauf zu speichern.

Der restiche Prozess läuft automatisch ab. Wurde das Modell erfolgriech gesliced ertönt ein einfach Piepton. Gab es einen Fehler, ertönt ein doppelter Piepton.

Danach kann direkt gedruckt werden.
Viel Spaß :)

