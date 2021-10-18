import click


@click.version_option(version="1.0.0")
@click.command()
@click.argument("filename", type=click.Path(exists=True))
@click.option(
    "-f",
    "--format",
    type=click.Choice(["CSV", "TSV", "JSON"]),
    default="CSV",
    help="File format.",
    show_default=True,
)
def main(**kwargs):
    "FILENAME: Path to file." ""

    print(kwargs)


if __name__ == "__main__":
    main()
