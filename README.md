# Discord Bot 

This repo is a template that can be used as a starting point for building a Discord bot using Python. Click 'Use this template' in the top right to get started.

## Poetry

Poetry is used as the build tool for this template, and manages dependencies and virtual environments. Run `poetry install` to create a venv and install all the dependencies, then `poetry shell` to drop into the venv and work on your project. See https://python-poetry.org/docs/basic-usage/ for full documentation. Run `poetry run python discord_bot` to start the bot.

## Discord.py

Discord.py is used as a framework for building a Discord bot, see https://discordpy.readthedocs.io/en/stable/ for more information on using Discord.py, or our own Discord bot, [Apollo](https://github.com/uwcs/apollo), as an example.

Discord.py requires an API token to start, see https://discordpy.readthedocs.io/en/stable/discord.html for more info.

## Settings using Pydantic

Pydantic is used to provide a convenient method for managing application config. There are two config settings in `settings.py`: the bot token and the bot's name. These can be specified by environment variables, in a `.env` file, or from a standalone config file. See https://docs.pydantic.dev/usage/settings/ for full docs. 

## Tests with Pytest 

Tests under `/tests` can all be run using `poetry run pytest`. **You should write unit tests for your bot!**

## Docker

A `Dockerfile` is provided to allow you to build a container image of your bot easily, which makes it easy to [deploy your bot using our container host](https://techteam.uwcs.co.uk/en/services/containers). `docker compose up` will build and run the container using the config specified in `docker-compose.yml`, including using the environment variables there to provide configuration.  

## GitHub Actions

GitHub Actions runs the CI jobs specified in `.github/workflows/ci.yml` on every push to `main` and every pull request opened against `main`. The CI does a few things:

- Checks that your `poetry.lock` matches your `pyproject.toml`
- Runs `black` and `isort` to ensure that your code formatting is consistent
- Runs `mypy` to try to catch any type errors
- Runs all your tests using `pytest` 

If all of these checks are successful, the CI will then build a container image and publish it to `ghcr.io`, which allows you to easily share and deploy your bot anywhere. The image published from a build of this repo is at https://github.com/UWCS/discord-bot/pkgs/container/discord-bot.


