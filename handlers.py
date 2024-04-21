from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

import random


router = Router()


@router.message(Command("start"))
async def start(msg: Message):
    await msg.reply(
        "Привет!Напиши /anekdot чтобы надорвать животик🤣🤣🤣 или /help чтобы получить список команд"
    )


@router.message(Command("help"))
async def help(msg: Message):
    await msg.reply(
        "Список доступных команд:\n"
        "/start - Начало работы с ботом\n"
        "/anekdot - Получить анекдот\n"
        "/help - Получить список команд"
    )


@router.message(Command("anekdot"))
async def anekdot(msg: Message):
    with open("anekdotes.txt", "r", encoding="utf-8") as f:
        anekdotes = f.read().split("*****")
        await msg.answer(random.choice(anekdotes))


@router.message()
async def message_handler(msg: Message):
    await msg.answer(
        "Я не понимаю тебя😥\n\n"
        "Список доступных команд:\n"
        "/start - Начало работы с ботом\n"
        "/anekdot - Получить анекдот\n"
        "/help - Получить список команд"
    )
