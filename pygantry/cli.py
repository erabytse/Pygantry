"""Minimal CLI - no bugs, no fancy features."""
import os
import sys
import typer
from . import __version__, PyGantryEngine

# Fix Windows console encoding
if sys.platform == "win32":
    import codecs
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.buffer, "strict")
    sys.stderr = codecs.getwriter("utf-8")(sys.stderr.buffer, "strict")

app = typer.Typer(
    name="pyg",
    help="Pygantry: Docker-like simplicity for Python projects",  
    no_args_is_help=True,
    add_completion=True
)

engine = PyGantryEngine()

@app.command()
def version():
    """Show Pygantry version."""
    typer.echo(f"Pygantry v{__version__} (Python {sys.version_info.major}.{sys.version_info.minor})")

@app.command()
def init(
    name: str = typer.Option("my_app", "--name", "-n", help="Project name"),
    force: bool = typer.Option(False, "--force", "-f", help="Overwrite existing Gantryfile")
):
    """Create a new Gantryfile manifest."""
    if not force and os.path.exists(engine.manifest_path):
        typer.echo("[ERROR] Gantryfile exists. Use --force to overwrite.")
        raise typer.Exit(1)
    engine.create_manifest(name)

@app.command()
def build():
    """Build the virtual environment from Gantryfile."""
    engine.build()

@app.command()
def run():
    """Run the application in the isolated environment."""
    engine.run()

@app.command()
def ship():
    """Create a portable ZIP package for deployment."""
    engine.ship()

if __name__ == "__main__":
    app()