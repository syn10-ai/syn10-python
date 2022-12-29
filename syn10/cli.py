import syn10
from syn10 import main


class Assets:
    @classmethod
    def info(cls, args):
        asset_info = syn10.Dataset(asset_id=args.id).info
        print(asset_info)


def authenticator(args):
    main.authenticate(client_id=args.client_id, client_secret=args.client_secret)
    print(f'SYN10_TOKEN="{main._auth.token}"')


def auth_register(parser):
    parser.add_argument("-i", "--client_id")
    parser.add_argument("-s", "--client_secret")
    parser.set_defaults(func=authenticator)


def api_register(parser):
    subs = parser.add_subparsers()
    sub = subs.add_parser("assets.info")
    sub.add_argument("-i", "--id", required=True)
    sub.set_defaults(func=Assets.info)
