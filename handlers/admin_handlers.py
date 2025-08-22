from aiogram import Router, F, Bot
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.types import (CallbackQuery, InlineKeyboardButton, InputMediaPhoto,
                           InlineKeyboardMarkup, Message, PhotoSize, InputFile, FSInputFile, URLInputFile, BufferedInputFile, LinkPreviewOptions)
from lexicon.lexicon import LEXICON_RU

from tools.db import add_user, get_all_users

router = Router()

options_1 = LinkPreviewOptions(is_disabled=True)
