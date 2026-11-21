import os
import sys
import subprocess

def main():
    requirements = os.path.join(os.path.dirname(__file__), "requirements.txt")
    application = os.path.join(os.path.dirname(__file__), "ADDoS.py")

    print("[*] Installing dependencies...")

    result = subprocess.run([
        sys.executable, "-m", "pip", "install", "-r", requirements
    ])

    if result.returncode != 0:
        print("[!] Failed to install dependencies.")
        sys.exit(1)

    os.system("cls" if os.name == "nt" else "clear")

    print("[*] Starting ADDoS...\n")

    subprocess.run([sys.executable, application])


if __name__ == "__main__":
    main()
