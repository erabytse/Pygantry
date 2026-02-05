import hashlib
import os
import venv
import subprocess
import yaml
import sys
import shutil

class PyGantryEngine:
    def __init__(self):
        self.manifest_path = "Gantryfile"
        self.env_dir = ".gantry_env"

    def is_premium(self):
        """Check if the Founder's key is valid."""
        key_path = "founder.key"
        if os.path.exists(key_path):
            with open(key_path, "r") as f:
                content = f.read().strip()
                # On utilise un code secret (tu pourras le changer)
                # On transforme la clé tapée en empreinte SHA-256
                hashed_input = hashlib.sha256(content.encode()).hexdigest()
                # L'empreinte ci-dessous correspond à "TON-CODE-SECRET"
                return hashed_input == "4c7429e298b153d63dfe55f8d3819b8b5f08b5de04503033cfabebe8b5e52c14"
        return False

    def total_wipeout(self):
        """Founder Only: Emergency cleanup of all environments."""
        if self.is_premium():
            shutil.rmtree(self.env_dir, ignore_errors=True)
        else:
            print("Access Denied: Premium Key Required.")


    def create_manifest(self):
        """Creates a professional Gantryfile."""
        config = {
            "project": "my_app",
            "python": f"{sys.version_info.major}.{sys.version_info.minor}",
            "packages": ["cowsay", "pyyaml", "typer", "rich"], # On inclut les outils du moteur !
            "entrypoint": "python -m cowsay -t 'Pygantry is Online'"
        }
        with open(self.manifest_path, "w") as f:
            yaml.dump(config, f)

    def build(self):
        """Build the isolated gantry environment with force-clean for Windows."""
        if os.path.exists(self.env_dir):
            try:
                shutil.rmtree(self.env_dir)
            except Exception as e:
                print(f"Warning: Could not clean old env, trying to continue... {e}")

        # Use symlinks=False to force hard copies of python.exe
        venv.create(self.env_dir, with_pip=True, symlinks=False)
        
        with open(self.manifest_path, "r") as f:
            config = yaml.safe_load(f)
        
        bin_folder = "Scripts" if os.name == 'nt' else "bin"
        pip_path = os.path.join(self.env_dir, bin_folder, "pip")

        packages = config.get("packages", [])
        if packages:
            # Install all packages in one go
            subprocess.run([pip_path, "install"] + packages, check=True)

    def run(self):
        """Execute the entrypoint and AUTO-REPAIR paths if moved."""
        with open(self.manifest_path, "r") as f:
            config = yaml.safe_load(f)
        
        bin_folder = "Scripts" if os.name == 'nt' else "bin"
        python_exe = "python.exe" if os.name == 'nt' else "python"
        abs_python = os.path.abspath(os.path.join(self.env_dir, bin_folder, python_exe))

        # --- AUTO-REPAIR LOGIC ---
        if not os.path.exists(abs_python):
             print("[Repairing Gantry Links...]")
             # Ici on pourrait ajouter une logique de re-symlink si besoin
        # -------------------------

        env = os.environ.copy()
        env["VIRTUAL_ENV"] = os.path.abspath(self.env_dir)
        # FORCE le PATH pour que 'pip' et 'python' pointent ICI
        env["PATH"] = os.path.dirname(abs_python) + os.pathsep + env.get("PATH", "")

        entry = config.get("entrypoint")
        # On injecte le python absolu détecté à l'instant T
        cmd = entry.replace("python", f'"{abs_python}"', 1)
        
        subprocess.run(cmd, shell=True, env=env)


    def ship(self):
        """Logic to package the gantry into a ZIP file."""
        with open(self.manifest_path, "r") as f:
            config = yaml.safe_load(f)
        
        project_name = config.get("project", "app")
        ship_name = f"{project_name}_shipped"

        # On crée l'archive
        # On exclut souvent le dossier .gantry_env si on veut que l'user build lui-même,
        # MAIS pour ton projet, on veut l'inclure pour la portabilité !
        shutil.make_archive(ship_name, 'zip', root_dir=".", base_dir=None)
        return f"{ship_name}.zip"
