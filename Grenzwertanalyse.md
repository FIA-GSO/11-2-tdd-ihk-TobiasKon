# Grenzwertanalyse
Tipp: benutzen Sie einen [Tabellengenerator für Markdown](https://www.tablesgenerator.com/markdown_tables)

## Muster
### percent_calculator
| # 	| erreichte Punkte 	| Gesamtpunkte 	| erwartetes Ergebnis 	|
|---	|------------------	|--------------	|---------------------	|
| 1 	| 10               	| 100          	| 10                  	|
| 2 	| 0                	| 100          	| 0                   	|
| 3 	| 0                	| 6            	| 0                   	|
| 4 	| -1               	| 100          	| ValueError          	|
| 5 	| 0                	| 5            	| ValueError          	|
| 6 	| 11               	| 10           	| ValueError          	|
| 7 	| "text"           	| 100          	| TypeError           	|
| 8 	| 10               	| "text"       	| TypeError           	|

### calc_ihk_grade
| #  	| Prozentwert 	| erwartetes Ergebnis 	|
|----	|-------------	|---------------------	|
| 1  	| 100         	| "sehr gut"          	|
| 2  	| 92          	| "sehr gut"          	|
| 3  	| 91          	| "gut"               	|
| 4  	| 81          	| "gut"               	|
| 5  	| 80          	| "befriedigend"      	|
| 6  	| 67          	| "befriedigend       	|
| 7  	| 66          	| "ausreichend"       	|
| 8  	| 50          	| "ausreichend"       	|
| 9  	| 49          	| "mangelhaft"        	|
| 10 	| 30          	| "mangelhaft"        	|
| 11 	| 29          	| "ungenügend         	|
| 12 	| 0           	| "ungenügend"        	|
| 13 	| 101         	| ValueError          	|
| 14 	| -1          	| ValueError          	|
| 15 	| "text"      	| TypeError           	|