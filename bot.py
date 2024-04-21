import asyncio
import logging
import sys
from get_token import getToken

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from handlers import router
from parse_anekdotes import parse_anekdotes


async def main() -> None:
    try:
        with open("anekdotes.txt") as f:
            pass
    except:
        print("parsing anekdotes...")
        parse_anekdotes()

    dp = Dispatcher()
    dp.include_router(router=router)
    bot = Bot(token=getToken(), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
