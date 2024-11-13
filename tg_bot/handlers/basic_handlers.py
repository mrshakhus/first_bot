from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from bot import get_bot
from lexicon.lexicon_ru import LEXICON_RU
from keyboards.start_keyboard import whether_play_keyboard


router = Router()
bot = get_bot()

@router.message(CommandStart())
async def process_start(message: Message):
    await message.answer(LEXICON_RU['/start'], reply_markup=whether_play_keyboard)

@router.message(Command(commands=['help']))
async def process_help(message: Message):
    await message.answer(LEXICON_RU['/help'], reply_markup=whether_play_keyboard)
