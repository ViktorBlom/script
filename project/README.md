## Log cleaner and system health checker
Scriptet automatiserar insamling av system- och nätverksinformation i en Linux-miljö och presenterar resultatet via ett menybaserat gränssnitt i terminalen.

---

## Syfte

Syftet med scriptet är att automatisera vanliga rekognoserings och systemkontroller samt systemadministration och incidenthantering.

På detta sätt skapas en pedagogisk överblick över datorns och nätverkets hälsotillstånd


## Funktioner

- Menybaserat och interaktivt gränssnitt
- Automatiserar flera Linux-kommandon
- Samlar in systeminformation:
  - systemets drifttid (uptime)
  - minnesanvändning
  - diskutrymme
  - CPU-information
- Visar nätverksgränssnitt
- Loggar utdata till fil för senare analys

## Krav

- Linux-operativsystem
- Python 3.8 eller senare
- Det räcker med Pythons standardbibliotek

## Användning

Kör scriptet från terminalen:

```bash
python3 recon_tool.py
