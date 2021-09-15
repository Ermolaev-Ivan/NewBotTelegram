import logging

from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = open("TOKEN.txt").read()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# @dp.message_handler(commands=['start', 'help'])
# async def send_welcome(message: types.Message):
#     """
#     This handler will be called when user sends `/start` or `/help` command
#     """
#     await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")
# Что бы обрабочик перехватывал все сообщения мы просто не передаем ему никаких команж


@dp.message_handler()
async def echo(message: types.Message, count=0, list_sportsmans = []):
   if "+" in message.text:
       count = count + message.text.count("+")
       print(count)
       print(message.from_user.username)
   else:
       print("-")

   await message.answer(message.text)





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
