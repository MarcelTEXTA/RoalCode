import sys
from interpreter import run

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py fichier.rc")
        return

    filename = sys.argv[1]
    with open(filename, 'r', encoding='utf-8') as f:
        code = f.read()

    run(code)

if __name__ == "__main__":
    main()
