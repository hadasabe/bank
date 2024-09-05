import logging
import asyncio

from bot import TOKEN
from kb import kb

from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.command import Command

logging.basicConfig(filename='logs/bank.log',
                    encoding='utf-8',  level=logging.DEBUG)

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(Command('start'))
async def start(message: Message):
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Что сделать?", reply_markup=keyboard)


@dp.message(F.text or F.text.lower() == "убавить")
async def minus(message: types.Message):
    money = message.text
    print(money)


@dp.message(F.text or F.text.lower() == "прибавить")
async def minus(message: types.Message):
    money = message.text
    print(money)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())