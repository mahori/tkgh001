from rich.console import Console


def main() -> None:
    console = Console(soft_wrap=True, emoji=False, highlight=False)

    console.print("[green]Hello from [bold]tkgh001[/bold]![/green]")
