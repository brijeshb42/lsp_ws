import argparse

from lsp_ws import start_server


def main(args):
    parser = argparse.ArgumentParser()
    parser.description = 'Python LSP over websocket'

    parser.add_argument(
        '--host',
        default='0.0.0.0',
        help='Bind to this address'
    )
    parser.add_argument(
        '--port',
        default=2087,
        help='Bind to this port'
    )
    args = parser.parse_args()
    start_server(args.host, args.port)


if __name__ == '__main__':
    print("Started server on - http://{}:{}/".format(args.host, args.port))
    main()
