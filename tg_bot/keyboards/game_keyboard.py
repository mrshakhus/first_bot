from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU

rock = KeyboardButton(text=LEXICON_RU['rock'])

scissors = KeyboardButton(text=LEXICON_RU['scissors'])

paper = KeyboardButton(text=LEXICON_RU['paper'])

game_keyboard_builder = ReplyKeyboardBuilder()

game_keyboard_builder.row(rock,
                          scissors,
                          paper,
                          width=3)

game_keyboard: ReplyKeyboardMarkup = game_keyboard_builder.as_markup(one_time_keyboard=True,
                                                                     resize_keyboard=True)

