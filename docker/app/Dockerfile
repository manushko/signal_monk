FROM python:3.8.3-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.0.5 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry'

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app
COPY ./poetry.lock ./pyproject.toml /app/
RUN poetry install --no-interaction --no-ansi

RUN groupadd -r web && useradd -d /app -r -g web web && chown web:web -R /app
USER web