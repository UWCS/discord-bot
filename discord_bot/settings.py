from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    A dataclass to contain settings for our bot.
    Uses pydantic: see https://docs.pydantic.dev/usage/settings/ for more info.
    """

    token: str
    name: str = "Discord Bot"

    class Config:
        env_prefix = "BOT_"
