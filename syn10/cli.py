import sys


def test_command(args):
    sys.stderr.write("info")
    sys.stderr.flush()
    print("info_print")


def api_register(parser):
    subparsers = parser.add_subparsers(help="All API subcommands")

    def help(args):
        parser.print_help()

    parser.set_defaults(func=help)

    sub = subparsers.add_parser("test")
    sub.set_defaults(func=test_command)
