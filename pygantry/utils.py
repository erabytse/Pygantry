"""Utility functions for Pygantry - logging, helpers, etc."""
from rich.console import Console

console = Console()

def log_success(message: str) -> None:
    """Print a success message in green with checkmark."""
    console.print(f"[bold green]✔[/bold green] {message}")

def log_error(message: str) -> None:
    """Print an error message in red with cross."""
    console.print(f"[bold red]✘[/bold red] {message}")

def log_info(message: str) -> None:
    """Print an info message in blue."""
    console.print(f"[bold blue]ℹ[/bold blue] {message}")

def log_warning(message: str) -> None:
    """Print a warning message in yellow."""
    console.print(f"[bold yellow]⚠[/bold yellow] {message}")