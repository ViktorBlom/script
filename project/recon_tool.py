#!/usr/bin/env python3
"""
Log Cleaner & System Health Checker

Kurs: Applied Script (AS20)
Syfte:
Detta script automatiserar insamling av systeminformation i en Linux-miljö.
Scriptet används för recon (rekognosering) genom att samla information om
systemets hälsa, nätverk, användare och hårdvara.
"""

# Importerar subprocess-modulen som gör det möjligt
# att köra Linux-kommandon från Python
import subprocess


def run(cmd, logfile=None):
    """
    Kör ett Linux-kommando och skriver ut resultatet i terminalen.
    Om en loggfil anges sparas även resultatet till fil.

    :param cmd: Linux-kommando som lista, t.ex. ["free", "-h"]
    :param logfile: (valfritt) filnamn där output ska sparas
    """

    # Visar vilket kommando som körs (för tydlighet)
    print(f"\n$ {' '.join(cmd)}")

    # Kör kommandot och fångar output som text
    result = subprocess.run(cmd, capture_output=True, text=True)

    # Skriver ut kommandots output i terminalen
    print(result.stdout)

    # Om loggfil är angiven, skriv även output till fil
    if logfile:
        with open(logfile, "a") as f:
            f.write(f"\n$ {' '.join(cmd)}\n")
            f.write(result.stdout)


def main():
    """
    Huvudfunktionen som innehåller programmets meny och logik.
    Körs när scriptet startas.
    """

    # Välkomstmeddelande
    print("Välkommen till System Health Checker (Python)")

    # Fil där all systeminformation sparas
    logfile = "recon_output.txt"

    # Meny-loop som körs tills användaren väljer att avsluta
    while True:
        print("\n1) Visa systemhälsa")
        print("2) Visa nätverk")
        print("3) Avsluta")

        # Tar emot användarens val
        choice = input("Välj ett alternativ: ").strip()

        # Alternativ 1: Systemhälsa / recon
        if choice == "1":
            # Visar hur länge systemet varit igång och belastning
            run(["uptime"], logfile)

            # Visar minnesanvändning
            run(["free", "-h"], logfile)

            # Visar diskutrymme
            run(["df", "-h"], logfile)

            # Visar OS, kernel och arkitektur
            run(["uname", "-a"], logfile)

            # Visar vilken användare scriptet körs som
            run(["whoami"], logfile)

            # Visar CPU-information och säkerhetsrelaterade flaggor
            run(["lscpu"], logfile)

        # Alternativ 2: Nätverksinformation
        elif choice == "2":
            # Visar nätverksinterface och IP-adresser
            run(["ip", "a"])

        # Alternativ 3: Avsluta programmet
        elif choice == "3":
            print("Hejdå!")
            break

        # Felhantering vid ogiltigt val
        else:
            print("Ogiltigt val, försök igen.")


# Startpunkt för programmet
# Detta säkerställer att main() endast körs
# när filen startas direkt och inte importeras
if __name__ == "__main__":
    main()


