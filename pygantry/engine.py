"""Stable engine for venv-based environments (no fragile relocation)."""
import os
import shutil
import subprocess
import sys
import venv
import yaml
import typer

class PyGantryEngine:
    def __init__(self, manifest_path="Gantryfile", env_dir=".gantry"):
        self.manifest_path = manifest_path
        self.env_dir = env_dir
    
    def create_manifest(self, project_name="my_app"):
        config = {
            "project": project_name,
            "python": f"{sys.version_info.major}.{sys.version_info.minor}",
            "packages": ["cowsay"],
            "entrypoint": 'python -m cowsay -t "Pygantry v1.2 Online!"'
        }
        with open(self.manifest_path, "w", encoding="utf-8") as f:
            yaml.dump(config, f, sort_keys=False)
        typer.echo("[OK] Gantryfile created for '{}'".format(project_name))
    
    def build(self):
        if os.path.exists(self.env_dir):
            shutil.rmtree(self.env_dir, ignore_errors=True)
        typer.echo("Building environment...")
        venv.create(self.env_dir, with_pip=True, symlinks=False)
        
        with open(self.manifest_path, encoding="utf-8") as f:
            config = yaml.safe_load(f)
        
        packages = config.get("packages", [])
        if packages:
            typer.echo("   -> Installing packages: {}".format(', '.join(packages)))
            bin_dir = "Scripts" if os.name == "nt" else "bin"
            pip = os.path.join(self.env_dir, bin_dir, "pip.exe" if os.name == "nt" else "pip")
            subprocess.run([pip, "install", "-q"] + packages, check=True)
        typer.echo("[OK] Built in ./{}".format(self.env_dir))
    
    def run(self):
        if not os.path.exists(self.env_dir):
            raise RuntimeError("Run 'pyg build' first")
        
        with open(self.manifest_path, encoding="utf-8") as f:
            config = yaml.safe_load(f)
        
        bin_dir = "Scripts" if os.name == "nt" else "bin"
        python = os.path.join(self.env_dir, bin_dir, "python.exe" if os.name == "nt" else "python")
        env = os.environ.copy()
        env["VIRTUAL_ENV"] = os.path.abspath(self.env_dir)
        env["PATH"] = os.path.dirname(python) + os.pathsep + env.get("PATH", "")
        
        entry = config.get("entrypoint", "python --version")
        if entry.startswith("python "):
            entry = entry.replace("python ", '"{}" '.format(python), 1)
        
        typer.echo("Running: {}".format(entry))
        subprocess.run(entry, shell=True, env=env)
    
    def ship(self):
        if not os.path.exists(self.env_dir):
            raise RuntimeError("Run 'pyg build' first")
        
        with open(self.manifest_path, encoding="utf-8") as f:
            config = yaml.safe_load(f)
        
        project = config.get("project", "app")
        archive = "{}_v1.2".format(project)
        
        stage = ".ship_stage"
        if os.path.exists(stage):
            shutil.rmtree(stage)
        os.makedirs(stage)
        
        shutil.copytree(self.env_dir, os.path.join(stage, self.env_dir))
        shutil.copy2(self.manifest_path, os.path.join(stage, self.manifest_path))
        
        launcher = os.path.join(stage, "run.bat" if os.name == "nt" else "run.sh")
        with open(launcher, "w", encoding="utf-8") as f:
            if os.name == "nt":
                f.write("@echo off\n")
                f.write("echo [Pygantry] Starting...\n")
                f.write("call .gantry\\Scripts\\activate.bat >nul 2>&1\n")
                f.write('python -m cowsay "Shipped with Pygantry v1.2!"\n')
                f.write("pause\n")
            else:
                f.write("#!/bin/sh\n")
                f.write('echo "[Pygantry] Starting..."\n')
                f.write('source .gantry/bin/activate\n')
                f.write('python -m cowsay "Shipped with Pygantry v1.2!"\n')
        if os.name != "nt":
            os.chmod(launcher, 0o755)
        
        zip_path = shutil.make_archive(archive, "zip", stage)
        shutil.rmtree(stage)
        typer.echo("[OK] Shipped to: {}".format(zip_path))
        typer.echo("\n[WARNING] Note: Target machine needs same Python version installed")
        return zip_path