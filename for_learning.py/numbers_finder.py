from aiogram import F, Bot, Dispatcher
from aiogram.filters import BaseFilter
from aiogram.types import Message, PhotoSize
from config import settings

bot = Bot(settings.tg_bot.token)
dp = Dispatcher()

class MyFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool | dict[str, list[int]]:
        numbers: list[int] = []
        for word in message.text.lower().strip(' .,').split(" "):
            if word.isdigit():
                numbers.append(word)
        
        if numbers:
            return {"numbers": numbers}
        return False
    
@dp.message(F.text.lower().startswith('найди числа'), MyFilter())
async def find_numbers_in_message(message: Message, numbers: list[int]):
    await message.answer(f"Нашел числа! Вот они: {" ".join(numbers)}")


@dp.message(F.text.lower().startswith('найди числа'))
async def notify_when_no_numbers(message: Message):
    await message.answer(f"Не нашел числа ;(")

@dp.message(F.photo[-1].as_('max_photo'))
async def send_back_photo(message: Message, max_photo: PhotoSize):
    await message.answer_photo(max_photo.file_id, 
                               'Осторожно!', 
                               has_spoiler=True, 
                               disable_notification=True)


if __name__ == '__main__':
    dp.run_polling(bot)