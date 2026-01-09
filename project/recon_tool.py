#!/usr/bin/env python3
import subprocess

def run(cmd):
    print(f"\n$ {' '.join(cmd)}")
    subprocess.run(cmd)

def main():
    print("Välkommen till System Health Checker (Python)")

    while True:
        print("\n1) Visa systemhälsa")
        print("2) Visa nätverk")
        print("3) Avsluta")
        choice = input("Välj ett alternativ: ").strip()

        if choice == "1":
            run(["uptime"])
            run(["free", "-h"])
            run(["df", "-h"])
        elif choice == "2":
            run(["ip", "a"])
        elif choice == "3":
            print("Hejdå!")
            break
        else:
            print("Ogiltigt val, försök igen.")

if __name__ == "__main__":
    main()

