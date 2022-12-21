import sys
import argparse

from syn10.cli import api_register, auth_register


def main():
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers()
    sub_auth = subparsers.add_parser("authenticate")
    auth_register(sub_auth)

    sub_api = subparsers.add_parser("api")
    api_register(sub_api)

    args = parser.parse_args()
    args.func(args)

    return 0


if __name__ == "__main__":
    sys.exit(main())
