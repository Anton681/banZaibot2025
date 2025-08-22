from dataclasses import dataclass
from environs import Env
from typing import List


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту
    admin_ids: List[int]  # Список Telegram ID администраторов


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)

    admins_str = env.str('ADMINS', default='')
    admin_ids = list(map(int, filter(None, admins_str.split(','))))

    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN'),
            admin_ids=admin_ids
            )
            )