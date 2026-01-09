#!/usr/bin/env python3
"""
Log Cleaner & System Health Checker
Kurs: Applied Script (AS20)
Syfte: Samla in systeminformation i Linux-miljö
"""
import subprocess

def run(cmd, logfile=None):
    print(f"\n$ {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)

    print(result.stdout)

    if logfile:
        with open(logfile, "a") as f:
            f.write(f"\n$ {' '.join(cmd)}\n")
            f.write(result.stdout)

def main():
    print("Välkommen till System Health Checker (Python)")

    logfile = "recon_output.txt"

    while True:
        print("\n1) Visa systemhälsa")
        print("2) Visa nätverk")
        print("3) Avsluta")
        choice = input("Välj ett alternativ: ").strip()

        if choice == "1":
            run(["uptime"], logfile)
            run(["free", "-h"], logfile)
            run(["df", "-h"], logfile)
            run(["uname", "-a"], logfile)
            run(["whoami"], logfile)
            run(["lscpu"], logfile)
        elif choice == "2":
            run(["ip", "a"])
        elif choice == "3":
            print("Hejdå!")
            break
        else:
            print("Ogiltigt val, försök igen.")

if __name__ == "__main__":
    main()

