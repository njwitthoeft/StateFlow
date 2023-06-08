from typer import Typer

app = Typer()


@app.command()
def say_hi(user: str) -> None:
    """Say hi with Typer."""
    print(f"Hi {user}!")


@app.command()
def say_bye(user: str) -> None:
    """Say hi with Typer."""
    print(f"Bye {user}!")
