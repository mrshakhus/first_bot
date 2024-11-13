import random
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from config import settings

BOT_TOKEN = settings.tg_bot.token

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

users = dict()

@dp.message(CommandStart())
async def register_user(message: Message):
    user_id = message.from_user.id
    if user_id not in users:
        users[user_id] = {"is_playing": False, 
                          "tries": 0,
                          "rand_num": 0}
        await message.answer('Вы зарегистрированы! Можете играть.')
    else:
        await message.answer('Вы уже зарегистрированы! Можете играть.')


@dp.message(Command(commands='play'))
async def start_game(message: Message):
    user_id = message.from_user.id
    users[user_id]['is_playing'] = True
    users[user_id]['tries'] = 5
    users[user_id]['rand_num'] = random.randint(0, 100)
    await message.answer('Начинаем игру! Введите число от 0 до 100.')


@dp.message()
async def process_users_number(message: Message):
    user_id = message.from_user.id
    if users[user_id]['is_playing']:
        input = message.text.strip()
        if input.isdigit():
            users[user_id]['tries'] -= 1
            num = int(input)
            if users[user_id]['rand_num'] > num:
                await message.answer('Мое число больше!')
            elif users[user_id]['rand_num'] < num:
                await message.answer('Мое число меньше!')
            else:
                await message.answer(f'Красава! Ты угадал мое число, это {users[user_id]['rand_num']}!')
                await message.answer('Может, сыграем еще?')
        else:
            await message.answer('Некорректный ввод, введите число от 0 до 100')
        
        if users[user_id]['tries'] == 0:
            await message.answer('К сожалению количество попыток закончилось ;(')
            await message.answer('Может, сыграем еще?')
    

if __name__ == '__main__':
    dp.run_polling(bot)