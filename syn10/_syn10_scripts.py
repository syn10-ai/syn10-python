import sys
import argparse

from syn10.cli import api_register


def main():
    parser = argparse.ArgumentParser(description=None)

    def help(args):
        parser.print_help()

    parser.set_defaults(func=help)

    subparsers = parser.add_subparsers()
    sub_api = subparsers.add_parser("api", help="Direct API calls")

    api_register(sub_api)

    args = parser.parse_args()
    args.func(args)

    return 0


if __name__ == "__main__":
    sys.exit(main())
