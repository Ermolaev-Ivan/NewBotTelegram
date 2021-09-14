import logging

import aiogram

API_TOKEN = open("TOKEN.txt").read()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = aiogram.Bot(token=API_TOKEN)
dp = aiogram.Dispatcher

@dp.message_handler(commands=['start', 'help'])     # выыдает ошибку, разобратьсязшз
async def send_welcome(message: aiogram.types.Message):
    """
       This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

# Что бы обрабочик перехватывал все сообщения мы просто не передаем ему никаких команж
# @dp.message_handler()
# async def echo(message: aiogram.types.Message):
#     # old style:
#     # await bot.send_message(message.chat.id, message.text)
#
#     await message.answer(message.text)


if __name__ == '__main__':
    aiogram.executor.start_polling(dp, skip_updates=True)
