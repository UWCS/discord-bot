FROM python:3.11 AS builder

RUN pip install poetry

# Tell poetry to create venv in the current directory
RUN poetry config virtualenvs.in-project true

# only copy in lockfile - install from locked deps
COPY poetry.lock /app/poetry.lock

WORKDIR /app

RUN poetry install

FROM python:3.11 AS runtime

WORKDIR /app

# copy venv into runtime
COPY --from=builder /app/.venv/ /app/.venv/

# add venv to path
ENV PATH=".venv/bin:$PATH"

# copy in discord_bot directory
COPY discord_bot /app

CMD [ "python", "discord_bot" ] 