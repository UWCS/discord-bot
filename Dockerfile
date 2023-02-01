FROM python:3.11 

RUN curl -sSL https://install.python-poetry.org | python3 -

COPY pyproject.toml poetry.lock /app/

# Tell poetry not to create a virtualenv - we don't need one in docker
RUN poetry config virtualenvs.create false

WORKDIR /app

# don't install dev deps
# fail the build if lockfile not up to date
# don't try to prompt us for stuff
RUN poetry install --without dev --sync --no-interaction

# copy source files in
ADD discord_bot /app/discord_bot

CMD [ "python3", "discord_bot" ] 