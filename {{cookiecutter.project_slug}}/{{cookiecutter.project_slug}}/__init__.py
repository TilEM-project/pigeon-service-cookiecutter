from pigeon import Pigeon
from pigeon.logging import setup_logging
import time


class Service:
    def __init__(
        self,
        host: str = "127.0.0.1",
        port: int = 61616,
        username: str = None,
        password: str = None,
    ):
        self._logger = setup_logging("{{ cookiecutter.project_slug }}")
        self.connection = Pigeon(
            "{{ cookiecutter.project_slug }}", host=host, port=port, logger=self._logger
        )
        self.connection.connect(username=username, password=password)
        self.connection.subscribe("example.message", self.example_callback)

    def example_callback(self, topic, msg):
        self._logger.info(msg)

    def send_message(self):
        self.connection.publish(
            "test.message", field1="this", field2="is a", field3="test"
        )

    def run(self):
        while True:
            self.send_message()
            time.sleep(1)
