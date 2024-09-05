from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, CallbackQuery
from aiogram.filters.command import Command


kb = [
        [types.KeyboardButton(text="Прибавить"),
        types.KeyboardButton(text="Убавить")]
    ]