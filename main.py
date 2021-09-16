import logging

from aiogram import Bot, Dispatcher, executor, types


def ending(el):
    num_list = [12, 13, 14, 15, 16, 17, 18, 19]
    a = el % 10
    if el in num_list:
        return ""
    elif a == 2 or a == 3 or a == 4:
        return "а"
    else:
        return ""


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
    global count
    global sportsmans
    print(message)
    # стоит подумать над логикой работы через словари {username : количесво плюсов}
    if message.text.find("+") != -1:
        count = count + message.text.count("+")
        sportsmans.append(message.from_user.last_name + " " + message.from_user.first_name)
    else:
        pass
    if message.text == "/get":
        sport = set(sportsmans)

        await message.answer(f"На тренировку собирается {count} человек{ending(count)}:")
        for a in sport:
            await message.answer(a)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
