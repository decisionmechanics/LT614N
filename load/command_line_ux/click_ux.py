import click

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version="1.0.0")
def main():
    pass


@main.command(help="Export as text file")
@click.argument("file_path")
@click.option(
    "--delimiter",
    "-d",
    type=str,
    default=",",
    help=r"Delimiter to use---e.g. ',', '|'.",
    show_default=True,
)
def text(*args, **kwargs):
    print("Exporting as text file")
    print(kwargs)


@main.command(help="Export as JOSN document")
@click.argument("file_path")
@click.option(
    "--indent",
    "-i",
    type=int,
    default=None,
    help="Indentation level for pretty printing.",
    show_default=True,
)
def json(*args, **kwargs):
    print("Exporting as JSON")
    print(kwargs)


if __name__ == "__main__":
    main()
