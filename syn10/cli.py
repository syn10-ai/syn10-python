from syn10 import main


def authenticator(args):
    main.authenticate(client_id=args.client_id, client_secret=args.client_secret)
    print(f'SYN10_TOKEN="{main._auth.token}"')


def auth_register(parser):
    parser.add_argument("-i", "--client_id")
    parser.add_argument("-s", "--client_secret")
    parser.set_defaults(func=authenticator)


def api_register(parser):
    pass
