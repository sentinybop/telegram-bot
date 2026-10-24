import os
import asyncio
from dotenv import load_dotenv
from aiogram import Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Bot
from aiogram import F
def main():
    #load bot token from env
    load_dotenv()
    token = os.getenv('BOT_TOKEN')
    if token == None:
        raise SystemExit('bot token not found. check .env')
    dp=Dispatcher()
    @dp.message(Command('start')) #answer for /start
    async def cmd_start(message: Message):
        await message.answer('Helloo')
    @dp.message(F.text) # echo message
    async def echo(message: Message):
        user_text= message.text
        await message.answer(f'{user_text}. length of message is {len(user_text)}')   
    async def main(): # start bot
        bot = Bot(token=token)
        await dp.start_polling(bot)
    asyncio.run(main())

if __name__ == '__main__':
    main()