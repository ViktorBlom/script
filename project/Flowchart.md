# Flödesschema – System Health Checker (Python)

## Översikt
Scriptet kör i en loop och visar en meny. Beroende på användarens val körs systemkontroller eller nätverkskontroller.
All output från “Systemhälsa” sparas även i en loggfil (`recon_output.txt`).

## Flödesschema (ASCII)

```text
   [Start]
      |
      v
[Importera moduler]
      |
      v
[Print välkomsttext]
      |
      v
[Sätt logfile = recon_output.txt]
      |
      v
+---------------------------+
|        while True         |
|   Visa meny + input()     |
+---------------------------+
      |
      v
   [Val == "1"?]---------------------------\
   /   \                                    |
 JA     NEJ                                  |
 |       |                                   |
 v       v                                   |
[Systemhälsa]                                |
- uptime                                     |
- free -h                                    |
- df -h                                      |
- uname -a                                   |
- whoami                                     |
- lscpu                                      |
(Sparas till logfile + visas i terminal)     |
 |                                           |
 v                                           |
(Tillbaka till meny) <------------------------/

   [Val == "2"?]----------------------------\
   /   \                                     |
 JA     NEJ                                   |
 |       |                                    |
 v       v                                    |
[Nätverk]                                     |
- ip a                                        |
(visas i terminal)                            |
 |                                            |
 v                                            |
(Tillbaka till meny) <-------------------------/

   [Val == "3"?]
   /     \
 JA      NEJ
 |        |
 v        v
[Avsluta] [Ogiltigt val -> tillbaka]
      |
      v
    [Stop]
