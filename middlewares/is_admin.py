# middlewares/is_admin.py
from aiogram import BaseMiddleware
from aiogram.types import Message
from config import load_config


class IsAdmin(BaseMiddleware):
    async def __call__(self, handler, event: Message, data):
        config = load_config()
        if event.from_user.id not in config.tg_bot.admin_ids:
            await event.answer("Доступ запрещён.")
            return False
        else:
            return await handler(event, data)