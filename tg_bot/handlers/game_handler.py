from aiogram import F, Dispatcher, Router
from aiogram.types import Message

from keyboards.game_keyboard import game_keyboard
from lexicon.lexicon_ru import LEXICON_RU
from keyboards.start_keyboard import whether_play_keyboard
from enums.elements import game_elements
from service.define_game_result import define_game_result


router = Router()
dp = Dispatcher()

@router.message(F.text == LEXICON_RU['wanna_play'])
async def start_game(message: Message):
    await message.answer(text=LEXICON_RU['reply_to_yes'], reply_markup=game_keyboard)


@router.message(F.text == LEXICON_RU['dont_wanna_play'])
async def start_game(message: Message):
    await message.answer(text=LEXICON_RU['reply_to_no'], reply_markup=whether_play_keyboard)

@router.message(F.text.in_(game_elements))
async def start_game(message: Message):
    user_element = message.text
    reply = await define_game_result(user_element)
    await message.answer(text=reply, reply_markup=whether_play_keyboard)

@router.message()
async def process_random_input(message: Message):
    await message.answer(LEXICON_RU['reply_to_random_input'], reply_markup=whether_play_keyboard)