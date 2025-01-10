Arithmetic Expression Parser mit ANTLR und Python ✨

Willkommen zum Arithmetic Expression Parser-Projekt! 🎉
Dieses Projekt ermöglicht das Parsen und Auswerten von arithmetischen Ausdrücken wie 3 + 5 * (2 - 1) unter Verwendung von ANTLR für die Grammatik und Python für die Implementierung des Lexers und Parsers.



🔧 Projektstruktur

Arithmetic/
│
├── arithmetic.g4          # ANTLR Grammatikdatei für arithmetische Ausdrücke
├── arithmetic1.py         # Python-Implementierung des Parsers und Lexers
└── README.md              # Dieses Dokument



📖 Grammatikbeschreibung (arithmetic.g4)

Diese ANTLR-Grammatik definiert eine einfache arithmetische Sprache mit den folgenden Regeln:

Parser-Regeln:
	•	expr: Ein Ausdruck besteht aus einem oder mehreren terms, verbunden durch Addition (+) oder Subtraktion (-).
	•	term: Ein Term besteht aus einem oder mehreren factors, verbunden durch Multiplikation (*) oder Division (/).
	•	factor: Ein Faktor ist entweder eine ganze Zahl (INT) oder ein verschachtelter Ausdruck in Klammern.

Lexer-Regeln:
	•	Operatoren:
	•	PLUS: +
	•	MINUS: -
	•	MUL: *
	•	DIV: /
	•	Klammern:
	•	LPAREN: (
	•	RPAREN: )
	•	INT: Eine ganze Zahl.
	•	Whitespace: Leerzeichen, Tabulatoren und Zeilenumbrüche werden ignoriert.

Beispiel für einen gültigen Ausdruck:
expr: term ((PLUS | MINUS) term)* ;
term: factor ((MUL | DIV) factor)* ;
factor: INT | LPAREN expr RPAREN ;



🐍 Python-Implementierung (arithmetic1.py)

Die Python-Datei enthält die Implementierung eines Lexers und Parsers:
	•	Lexer: Zerlegt den Eingabetext in Tokens wie Zahlen, Operatoren und Klammern.
	•	Parser: Verarbeitet die Tokens und berechnet das Ergebnis des arithmetischen Ausdrucks, indem er die Grammatikregeln anwendet.

evaluate():
	•	Eine Hilfsfunktion, die den arithmetischen Ausdruck parst und das Ergebnis berechnet.

🧮 Beispiel für einen gültigen Ausdruck
"3 + 5 * (2 - 1)"

Tokenisierung:

Der Lexer zerlegt den Ausdruck in folgende Tokens:
	•	3 (INT)
	•	+ (PLUS)
	•	5 (INT)
	•	* (MUL)
	•	( (LPAREN)
	•	2 (INT)
	•	- (MINUS)
	•	1 (INT)
	•	) (RPAREN)

Ausgabe:

Der Parser berechnet das Ergebnis des Ausdrucks als 8.



🛠️ Verwendung

1. Installiere ANTLR und die Python-Bibliothek

Falls ANTLR noch nicht installiert ist, kannst du es mit den folgenden Befehlen installieren:
	•	ANTLR installieren: brew install antlr
 	•	Python-ANTLR-Binding installieren: pip install antlr4-python3-runtime
  
2. Grammatik kompilieren

Verwende ANTLR, um den Parser und Lexer zu generieren:
antlr4 arithmetic.g4 -Dlanguage=Python3

Dies erstellt die notwendigen Python-Dateien für den Lexer und den Parser.

3. Python-Skript verwenden

Erstelle einen Ausdruck und lasse ihn auswerten:

from arithmetic1 import evaluate

# Beispiel:
result = evaluate("3 + 5 * (2 - 1)")
print(f"Ergebnis: {result}")  # Ausgabe: 8

4. Testen

Du kannst das Python-Skript ausführen, um verschiedene arithmetische Ausdrücke zu testen:
python3 arithmetic1.py



🚨 Fehlerbehandlung

Der Parser gibt eine Fehlermeldung aus, wenn der Ausdruck ungültig ist, z. B.:
Ungültiges Zeichen: x



🚀 Erweiterbarkeit

Du kannst diese Grammatik leicht erweitern, um zusätzliche Funktionen hinzuzufügen:
	•	Exponenten: Zum Beispiel 2 ^ 3 für Potenzen.
	•	Variablen: Definiere Variablen und verwende sie in Ausdrücken.
	•	Funktionen: Erweitere den Parser um benutzerdefinierte Funktionen.




Zusammenfassung

Dieses Projekt bietet eine vollständige Implementierung eines einfachen Parsers für arithmetische Ausdrücke. Es ist sowohl als Lernressource als auch als Grundlage für komplexere mathematische Ausdrücke und Erweiterungen nützlich.
