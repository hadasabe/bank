import logging
import asyncio
import os

from bot import TOKEN
from kb import kb

from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.command import Command, CommandObject

logging.basicConfig(filename='logs/bank.log',
                    encoding='utf-8',  level=logging.DEBUG)

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(Command('start'))
async def start(message: Message):
    print(message.chat.id)
    if message.chat.id == -1002241643562 or message.chat.id == 1276784624:
        await message.answer('''/plus x
/minus x
/balance''')


@dp.message(Command('minus'))
async def minus(message: types.Message, command: CommandObject):
    print(message.chat.id)
    if message.chat.id == -1002241643562 or message.chat.id == 1276784624:
        if command.args is None:
            await message.answer("Ошибка: не переданы аргументы")
            return
        try:
            money = int(command.args.split(" ", maxsplit=1)[0])

        except ValueError:
            await message.answer(
                "Ошибка: неправильный формат команды. Пример:\n"
                "/minus x")
            return

        with open('db.txt', 'r') as f:
            prev = f.readline()
            mon_prev = int(prev)
            mon_prev -= money

        with open("db.txt", "w") as f:
            print(mon_prev, str(money))
            # os.system(r' >db.txt')
            f.write(f'{str(mon_prev)}\n')

        await balance(message)


@dp.message(Command('plus'))
async def plus(message: types.Message, command: CommandObject):
    if message.chat.id == -1002241643562 or message.chat.id == 1276784624:
        if command.args is None:
            await message.answer("Ошибка: не переданы аргументы")
            return
        try:
            money = int(command.args.split(" ", maxsplit=1)[0])

        except ValueError:
            await message.answer(
                "Ошибка: неправильный формат команды. Пример:\n"
                "/plus x")
            return

        with open('db.txt', 'r') as f:
            prev = f.readline()
            mon_prev = int(prev)
            mon_prev += money

        with open("db.txt", "w") as f:
            print(mon_prev, str(money))
            # os.system(r' >db.txt')
            f.write(f'{str(mon_prev)}\n')

        await balance(message)


@dp.message(Command('balance'))
async def balance(message: types.Message):
    with open('db.txt', 'r') as f:
        now = f.readline()

    await message.answer(now)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())