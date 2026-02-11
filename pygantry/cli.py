"""Minimal CLI - no bugs, no fancy features."""
import os
import sys
import typer
from . import __version__, PyGantryEngine

app = typer.Typer(no_args_is_help=True)
engine = PyGantryEngine()

@app.command()
def version():
    """Show version."""
    print(f"Pygantry v{__version__} (Python {sys.version_info.major}.{sys.version_info.minor})")

@app.command()
def init(name: str = typer.Option("my_app", "--name", "-n"), force: bool = False):
    """Create Gantryfile."""
    if not force and os.path.exists(engine.manifest_path):
        print(f"✗ Gantryfile exists. Use --force to overwrite.")
        raise typer.Exit(1)
    engine.create_manifest(name)

@app.command()
def build():
    """Build environment."""
    engine.build()

@app.command()
def run():
    """Run application."""
    engine.run()

@app.command()
def ship():
    """Create ZIP package."""
    engine.ship()