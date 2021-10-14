import click

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}


@click.group(context_settings=CONTEXT_SETTINGS, chain=True)
@click.version_option(version="1.0.0")
@click.pass_context
@click.option(
    "--imperial",
    "-i",
    is_flag=True,
    help="Convert from metric to imperial",
    show_default=True,
)
def main(ctx, imperial):
    ctx.obj["imperial"] = imperial


@main.command(help="Convert distance")
@click.pass_context
@click.argument("value", type=float)
def distance(ctx, value):
    if not ctx.obj["imperial"]:
        print(f"{value} miles is {value * 1.609344:.2f} km")
    else:
        print(f"{value} km is {value / 1.609344:.2f} miles")


@main.command(help="Convert weight")
@click.pass_context
@click.argument("value", type=float)
def weight(ctx, value):
    if not ctx.obj["imperial"]:
        print(f"{value} lbs is {value * 0.4535924:.2f} kg")
    else:
        print(f"{value} kg is {value / 0.4535924:.2f} lbs")


@main.command(help="Convert temperature")
@click.pass_context
@click.argument("value", type=float)
def temperature(ctx, value):
    if not ctx.obj["imperial"]:
        print(f"{value} degF is {(value - 32) * 5 / 9:.2f} degC")
    else:
        print(f"{value} degC is {value * 9 / 5 + 32:.2f} degF")


if __name__ == "__main__":
    main(obj={})
