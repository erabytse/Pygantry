import os
import sys

# On ajoute le dossier actuel au chemin de recherche de Python
sys.path.append(os.getcwd())

def main():
    try:
        from pygantry.cli import app
        # On appelle directement Typer
        app()
    except ImportError as e:
        print(f"Error: Could not find pygantry module. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
