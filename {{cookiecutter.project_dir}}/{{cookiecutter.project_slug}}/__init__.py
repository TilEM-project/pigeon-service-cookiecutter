from pigeon import Pigeon
import time
import logging


class {{ cookiecutter.class_name }}:
    def __init__(
        self,
        host: str = "127.0.0.1",
        port: int = 61616,
        username: str = None,
        password: str = None,
        logger: logging.Logger = None,
    ):
        self._logger = logger if logger is not None else logging.getLogger(__name__)
        self.connection = Pigeon("{{ cookiecutter.project_slug }}", host=host, port=port)
        self.connection.connect(username=username, password=password)
        self.connection.subscribe("example.message", self.example_callback)

    def example_callback(self, msg):
        self._logger.info(msg)

    def send_message(self):
        self.connection.publish(
            "test.message", field1="this", field2="is a", field3="test"
        )

    def run(self):
        while True:
            self.send_message()
            time.sleep(1)
