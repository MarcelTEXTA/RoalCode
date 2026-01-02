import sys
from interpreter import run

def main():
    if len(sys.argv) < 2:
        print("Usage: roalcode fichier.rc")
        return

    filename = sys.argv[1]
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            code = f.read()
    except FileNotFoundError:
        print(f"Erreur : fichier {filename} introuvable.")
        return

    run(code)

if __name__ == "__main__":
    main()
