import os
import sys
import argparse
import syn10
from syn10.cli import api_register


def main():
    parser = argparse.ArgumentParser()

    def help(args):
        parser.print_help()

    parser.set_defaults(func=help)

    subparsers = parser.add_subparsers()
    sub_api = subparsers.add_parser("api")
    api_register(sub_api)

    args = parser.parse_args()
    syn10.debug = bool(os.getenv("SYN10_DEBUG"))
    args.func(args)

    return 0


if __name__ == "__main__":
    sys.exit(main())
