import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = open("TOKEN.txt").read()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

count = 0
sportsmans = []


@dp.message_handler()
async def echo(message: types.Message):

    # объявляем глобальными переменные
    global count
    global sportsmans
    # стоит подумать над логикой работы через словари {username : количесво плюсов}
    if message.text.find("+") != -1:
        count = count + message.text.count("+")
        sportsmans.append(message.from_user.username)

    # над реализацией данного функционала стоит подумать.. - может быть и дефисом
    # elif "-" in message.text:
    #     if message.from_user.username not in list_sportsmans:
    #         print("проходит 2")
    #         pass
    #     else:
    #         list_sportsmans.remove(message.from_user.username)
    #         count = count - message.text.count("-")

    else:
        pass
    if message.text == "/get":
        await message.answer(f"На тренировку собирается {count} человек(а)")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
