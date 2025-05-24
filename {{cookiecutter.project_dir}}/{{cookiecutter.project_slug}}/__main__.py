from . import {{ cookiecutter.class_name }}
import argparse
from pigeon.utils import setup_logging


def main():
    parser = argparse.ArgumentParser(prog="{{ cookiecutter.project_slug }}")
    parser.add_argument("--host", type=str, default="127.0.0.1", help="The message broker to connect to.")
    parser.add_argument("--port", type=int, default=61616, help="The port to use for the connection.")
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

    setup_logging()

    {{ cookiecutter.project_slug }} = {{ cookiecutter.class_name }}(
        host=args.host, port=args.port, username=args.username, password=args.password
    )
    {{ cookiecutter.project_slug }}.run()


if __name__ == "__main__":
    main()
