from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    A dataclass to contain settings for our bot.
    Uses pydantic: see https://docs.pydantic.dev/usage/settings/ for more info.
    """

    token: str
    name: str = "Discord Bot"

    class Config:
        env_file = ".env"  # load from a .env file
        env_prefix = "BOT_"  # env vars are prefixed with BOT_
