FROM python:3-bookworm

RUN --mount=source=requirements.txt,target=/requirements.txt pip install -r /requirements.txt

RUN --mount=source=.,target=/{{ cookiecutter.project_slug }}/,rw pip install /{{ cookiecutter.project_slug }}
