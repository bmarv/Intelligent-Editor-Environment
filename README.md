# Intelligent-Editor-Environment

Das Programm *Intelligent Editor Environment* bietet eine
Möglichkeit zur Textanalyse hinsichtlich der Zipf-Verteilung der Wörter
des Textes. Unter anderem sind ein Texteditor, ein Tool zur Textgenerierung 
sowie die Berechnung der Probability-Mass-Function des Zipfschen Gesetzes implementiert. 

Eine vollständige [Dokumentation](https://github.com/bmarv/Intelligent-Editor-Environment/blob/master/Dokumentation/Simulation%20und%20Modellierung%20-%20Textstatistik%20-%20Intelligent%20Editor%20Environment-%20Marvin%20Beese.pdf) 
mit einer detaillierten Beschreibung aller Programmteile und der 
mathematischen Hintergründe ist unter [./Dokumentation/](https://github.com/bmarv/Intelligent-Editor-Environment/tree/master/Dokumentation) einsehbar. 

Zudem ist ein [Jupyter-Notebook](https://github.com/bmarv/Intelligent-Editor-Environment/blob/master/Jupyter/IEE%20-%20Textstatistik.ipynb)
mit relevanten Code-Fragmenten und einer Analyse unter [./Jupyter/](https://github.com/bmarv/Intelligent-Editor-Environment/tree/master/Jupyter) vorhanden.

## Nutzung

Über die herkömmliche Ausführung von Python-Programmen hinaus sind auch ausführbare Windows-Executable Dateien
im Verzeichnis [./dist/](https://github.com/bmarv/Intelligent-Editor-Environment/tree/master/dist) vorhanden.

## Programmteile

Das Programm ist unterteilt in mehrere Bestandteile. Die Benutzeroberfläche
und elementare Programmteile sind im Package [Basic Gui](https://github.com/bmarv/Intelligent-Editor-Environment/tree/master/Basic_Gui) beinhaltet. 

Die Analysen zur Texteingabe, Dateiinformation und mathematischen Metriken sind im
Package [Statistics](https://github.com/bmarv/Intelligent-Editor-Environment/tree/master/Statistics) und die Textgenerierung im Package Generation implementiert.
Alle relevanten mathematischen und Textgenerierungs-Funktionen wurden im Package [Testing](https://github.com/bmarv/Intelligent-Editor-Environment/tree/master/Testing) mithilfe von *Pytest* auf ihre Korrektheit getestet.

## Zusammenfassung

Mithilfe dieses Programmes ist berechenbar, dass
alle hinreichend großen Texte eine Wortverteilung haben, die einer Zipf-Verteilung
entsprechen. Hierbei ist die Sprache des Textes nicht ausschlaggebend, da dies ein
physikalisches Phänomen ist, das auch in anderen Gebieten außerhalb der Linguistik Anwendung findet. 
In diesem Programm kann die Steigung der Verteilung, der Exponent der Verteilung
und mit der Probability-Mass-Function die Anzahl der Vorkommen berechnet werden.

Dieses Programm skaliert als Editor problemlos auch für große Dokumente. 
Bei der mathematischen Analyse gibt es eine deutliche Verzögerung bei der Berechnung 
und grafischen Darstellung von großen Daten hohen Ranges, weswegen
von einer Limit-Setzung von über 1000 dringend abgeraten wird. Die zufällige
Textgenerierung skaliert hingegen auch bei einer Limitsetzung von über 20000
Zeichen problemlos und mit einer sehr geringen Verzögerung.

Eine Kurzfassung des Programmes gibt mittels [Jupyter-Dokument](https://github.com/bmarv/Intelligent-Editor-Environment/blob/master/Jupyter/IEE%20-%20Textstatistik.ipynb) Auskunft
über Programmabschnitte und Ergebnisse der Analyse von *Die Leiden des jungen Werthers*.

## Entwicklungsumgebung

Das Programm wurde mit *Python 3.8* und *Windows 10 x64-based processor*
entwickelt und unter *Ubuntu Gnome 18.04* getestet.

Die Packages *tkinter, ttkthemes, os, matplotlib, numpy,
string, re, getpass* und *unittest* wurden verwendet.

## Selbstständigkeitserklärung

Dieses Projekt wurde in alleiniger Arbeit und ohne Mithilfe anderer Personen 
oder Programme erstellt.
