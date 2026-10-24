import os
import asyncio
from dotenv import load_dotenv
from aiogram import Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Bot
from aiogram import F
from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
def main():
    #load bot token from env
    load_dotenv()
    token = os.getenv('BOT_TOKEN')
    if token is None:
        raise SystemExit('bot token not found. check .env')
    dp=Dispatcher()
    @dp.message(Command('start')) #answer for /start
    async def cmd_start(message: Message):
        await message.answer('Helloo') 
    @dp.message(Command('menu')) # builder menu on message
    async def menu(message: Message):
        builder = InlineKeyboardBuilder()
        builder.button(text='button 1', callback_data='1')
        builder.button(text='button 2', callback_data='2')
        await message.answer('choose: ', reply_markup=builder.as_markup())
    @dp.message(F.text) # echo message
    async def echo(message: Message):
        user_text= message.text
        await message.answer(f'{user_text}. length of your message is {len(user_text)}')     
    @dp.callback_query(F.data=='1') # answer button1 
    async def button1(callback: CallbackQuery):
        await callback.message.edit_text('you tapped 1')
    @dp.callback_query(F.data == '2') #answer button 2
    async def button2(callback: CallbackQuery):
        await callback.message.edit_text('you tapped 2')    
    async def main(): # start bot
        bot = Bot(token=token)
        await dp.start_polling(bot)
    asyncio.run(main())

if __name__ == '__main__':
    main()