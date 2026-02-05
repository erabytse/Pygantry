import os
import shutil
import sys
import typer
from rich.console import Console
import yaml
from pygantry.engine import PyGantryEngine

app = typer.Typer(help="Pygantry: The ultra-lightweight Python container engine.")
console = Console()
engine = PyGantryEngine()

__version__ = "1.0.0"

@app.command()
def version():
    """Display the Pygantry version."""
    if engine.is_premium():
        console.print(f"[bold gold1]Pygantry Premium v{__version__} (Founder Edition)[/bold gold1]")
    else:
        console.print(f"[bold cyan]Pygantry Standard v{__version__}[/bold cyan]")

@app.command()
def init():
    """Initialize a new Gantryfile."""
    engine.create_manifest() # Ajoute une méthode pour créer 'Gantryfile'
    console.print("[bold green]✔[/bold green] Gantryfile initialized!")

@app.command()
def init(name: str = "my_app"):
    """Initialize a new Gantryfile with a custom name."""
    engine.create_manifest(name)
    console.print(f"[bold green]✔[/bold green] Gantryfile for '{name}' initialized!")

@app.command()
def build():
    """Build the containerized environment."""
    with console.status("[bold blue]Lifting the gantry (Building)...") as status:
        engine.build()
    console.print("[bold green]✔[/bold green] Gantry is ready for deployment!")

@app.command()
def run():
    """Run the application inside the gantry."""
    engine.run()

@app.command()
def ship():
    """Package the gantry into a portable ZIP for international distribution."""
    with console.status("[bold magenta]Shipping in progress...") as status:
        filename = engine.ship()
    console.print(f"[bold green]✔[/bold green] Package created: [yellow]{filename}[/yellow]")
    console.print("[bold cyan]Ready to conquer the world![/bold cyan]")

@app.command()
def activate(key: str):
    """Activate your Pygantry Premium License."""
    with open("founder.key", "w") as f:
        f.write(key)
    if engine.is_premium():
        console.print("[bold gold1]✨ Premium Mode Activated! Welcome Founder.[/bold gold1]")
    else:
        console.print("[bold red]❌ Invalid Key. Standard mode only.[/bold red]")  

@app.command(hidden=True)
def founder_debug():
    """SECRET: Founder access to system internals."""
    console.print(f"[bold gold1]Welcome, Founder.[/bold gold1]")
    console.print(f"System: {sys.platform} | Python: {sys.version}")

@app.command(hidden=True)
def founder_clean():
    """SECRET: Force wipe all gantries on this machine."""
    engine.total_wipeout() # On va créer cette méthode
    console.print("[bold red]All gantries have been dismantled.[/bold red]")

@app.command(hidden=True)
def founder_stats():
    """SECRET: Show premium statistics."""
    if engine.is_premium():
        console.print("[bold cyan]--- GANTRY PREMIUM STATS ---[/bold cyan]")
        console.print("Optimization Level: MAXIMUM")
        console.print("Compression: TITANIUM")
    else:
        console.print("[red]Unauthorized access.[/red]")

@app.command(hidden=True)
def stealth():
    """SECRET: Toggle stealth mode for the environment folder."""
    if engine.is_premium():
        if os.name == 'nt':
            # Commande Windows pour cacher le dossier
            os.system(f'attrib +h {engine.env_dir}')
            console.print(f"[bold]Dossier {engine.env_dir} maintenant invisible (Stealth).[/bold]")
    else:
        console.print("[red]Premium key needed for Stealth Mode.[/red]")
