from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButtonPollType, WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from config import settings

BOT_TOKEN = settings.tg_bot.token

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# button1 = KeyboardButton(text="Да🙏")
# button2 = KeyboardButton(text="Нет😡")

# keyboard_buttons = ReplyKeyboardMarkup(keyboard=[[button1, button2]], 
#                                        one_time_keyboard=True, 
#                                        resize_keyboard=True)

# buttons3: list[KeyboardButton] = [ KeyboardButton(text=f'{i}') for i in range(1, 101) ]
# keyboard_example: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[buttons3],
#                                                             resize_keyboard=True)

kb_builder = ReplyKeyboardBuilder()
# kb_builder.row(*buttons3)

# contacts_btn = KeyboardButton(
#     text='Поделиться контактами',
#     request_contact=True
# )

# geo_btn = KeyboardButton(
#     text='Поделиться геолокацией',
#     request_location=True
# )

# poll_btn = KeyboardButton(
#     text='Создать голосовалку',
#     request_poll=KeyboardButtonPollType(type='poll')
# )

# kb_builder.row(contacts_btn, geo_btn, poll_btn, width=1)

# https://stepik.org/
web_app = KeyboardButton(
    text='Открыть Stepik',
    web_app=WebAppInfo(url='https://bb.kai.ru/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_1_1')
)
kb_builder.row(web_app, width=1)



@dp.message(CommandStart())
async def send_keyboard_buttons(message: Message):
    await message.answer(
        text='Да или нет?',
        reply_markup=kb_builder.as_markup()      
    )


@dp.message(F.text == '1')
async def handle_yes_answer(message: Message):
    await message.answer(text="Нормас",
                         reply_markup=ReplyKeyboardRemove(remove_keyboard=True))

# @dp.message(F.text == 'Да🙏')
# async def handle_yes_answer(message: Message):
#     await message.answer(text="Нормас")


# @dp.message(F.text == 'Нет😡')
# async def handle_no_answer(message: Message):
#     await message.answer(text="Плохо")


if __name__ == "__main__":
    dp.run_polling(bot)

