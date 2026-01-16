<img width="1008" height="625" alt="image" src="https://github.com/user-attachments/assets/1de53b3d-c32b-45fc-b391-595d739cc832" />


# System Health Checker (Python)

## Syfte / Mål
Syftet med detta projekt är att skapa ett Python-script som automatiserar insamling av system- och nätverksinformation i en Linux-miljö.  
Scriptet används för recon (rekognosering), vilket är ett första steg i säkerhetsarbete och felsökning, där man skaffar sig en överblick över systemets status.

Målet är att samla relevant information på ett strukturerat sätt och kunna visa samt spara resultatet för vidare analys.

---

## Funktion
Scriptet erbjuder ett menybaserat gränssnitt där användaren kan välja mellan olika alternativ:

- Visa systemhälsa:
  - Systemets drifttid och belastning (uptime)
  - Minnesanvändning (RAM och swap)
  - Diskutrymme
  - Operativsystem och kernel
  - Aktiv användare
  - CPU-information och säkerhetsrelaterade flaggor
- Visa nätverksinformation:
  - Aktiva nätverksinterface
  - IPv4- och IPv6-adresser
- All output skrivs ut i terminalen och sparas även till en loggfil (`recon_output.txt`)

---

## Systemkrav
För att köra scriptet krävs:

- Linux-operativsystem (t.ex. Kali Linux eller Ubuntu)
- Python 3
- Tillgång till följande Linux-kommandon:
  - `uptime`
  - `free`
  - `df`
  - `uname`
  - `whoami`
  - `lscpu`
  - `ip`

Scriptet är testat i en Linux-miljö och är inte avsett att köras på Windows.

---

## Instruktioner
Kör scriptet:

bash
python3 recon_tool.py
Följ instruktionerna i menyn genom att välja ett alternativ.

Efter körning sparas all insamlad information automatiskt i filen:

recon_output.txt
