import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str, help="Path to file.")
    parser.add_argument(
        "-f",
        "--format",
        type=str,
        choices=["CSV", "TSV", "JSON"],
        default="CSV",
        help=r"File format.",
    )

    return parser.parse_args()


def main():
    args = parse_arguments()

    print(args)


if __name__ == "__main__":
    main()
