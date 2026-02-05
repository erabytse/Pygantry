def log_success(message):
    from rich.console import Console
    Console().print(f"[bold green]✔[/bold green] {message}")
