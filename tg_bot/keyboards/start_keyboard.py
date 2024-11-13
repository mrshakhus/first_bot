from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU

wanna_play_button = KeyboardButton(text=LEXICON_RU['wanna_play'])
dont_wanna_play_button = KeyboardButton(text=LEXICON_RU['dont_wanna_play'])

play_buttons_builder = ReplyKeyboardBuilder()

play_buttons_builder.row(wanna_play_button, 
                         dont_wanna_play_button, 
                         width=2)

whether_play_keyboard: ReplyKeyboardMarkup = play_buttons_builder.as_markup(one_time_keyboard=True,
                                                                    resize_keyboard=True)