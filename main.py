import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

TOKEN = os.getenv("8351353319:AAF7XnW27GZYcjKcJztQSmiSAOhrr_XE8F8")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton("📋 Копировать код", switch_inline_query=message.text)
    keyboard.add(button)

    await message.answer(f"```lua\n{message.text}\n```", parse_mode="Markdown", reply_markup=keyboard)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
