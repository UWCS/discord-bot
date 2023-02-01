FROM python:3.11 AS builder

RUN pip install poetry

COPY pyproject.toml poetry.lock /app/

# Tell poetry not to create a virtualenv - we don't need one in docker
RUN poetry config virtualenvs.create false

WORKDIR /app

RUN poetry install --no-interaction

FROM python:3.11 AS runtime

WORKDIR /app

# copy venv into runtime
COPY --from=builder /app/.venv/ /app/.venv/

# add venv to path
ENV PATH=".venv/bin:$PATH"

# copy in discord_bot directory
COPY discord_bot /app

CMD [ "python", "discord_bot" ] 