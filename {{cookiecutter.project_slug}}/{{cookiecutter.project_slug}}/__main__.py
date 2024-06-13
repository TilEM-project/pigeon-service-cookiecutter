from . import Service
import argparse


def main():
    parser = argparse.ArgumentParser(prog="{{ cookiecutter.project_slug }}")
    parser.add_argument("--host", type=str, help="The message broker to connect to.")
    parser.add_argument("--port", type=int, help="The port to use for the connection.")
    parser.add_argument(
        "--username",
        type=str,
        help="The username to use when connecting to the STOMP server.",
    )
    parser.add_argument(
        "--password",
        type=str,
        help="The password to use when connecting to the STOMP server.",
    )

    args = parser.parse_args()

    service = Service(
        host=args.host, port=args.port, username=args.username, password=args.password
    )
    service.run()


if __name__ == "__main__":
    main()
