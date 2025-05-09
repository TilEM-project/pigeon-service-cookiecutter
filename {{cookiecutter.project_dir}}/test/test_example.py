import {{ cookiecutter.project_slug }}
import pytest


@pytest.fixture
def pigeon(mocker):
    Pigeon = mocker.MagicMock()
    mocker.patch("{{ cookiecutter.project_slug }}.Pigeon", Pigeon)
    return Pigeon


@pytest.fixture
def logger(mocker):
    logger = mocker.MagicMock()
    mocker.patch("{{ cookiecutter.project_slug}}.logging.getLogger", logger)
    return logger


def test_service(pigeon, logger):
    service = {{ cookiecutter.project_slug }}.{{ cookiecutter.class_name }}(
        host="1.2.3.4", port=4321, username="test_user", password="wordpass"
    )

    logger.assert_called_with("{{ cookiecutter.project_slug }}")
    pigeon.assert_called_with(
        "{{ cookiecutter.project_slug }}", host="1.2.3.4", port=4321
    )
    service.connection.connect.assert_called_with(username="test_user", password="wordpass")
    service.connection.subscribe.assert_called_with("example.message", service.example_callback)

    service.example_callback("example.message", "message_data")

    service._logger.info.assert_called_with("message_data")

    service.send_message()

    service.connection.publish.assert_called_with(
        "test.message", field1="this", field2="is a", field3="test"
    )
