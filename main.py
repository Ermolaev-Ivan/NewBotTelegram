import logging, datetime
from aiogram import Bot, Dispatcher, executor, types


# две функции окончаний не абсолютные, но для наших нужд подходящие
def ending(el):
    num_list = [12, 13, 14, 15, 16, 17, 18, 19]
    a = el % 10
    if el in num_list:
        return ""
    elif a == 2 or a == 3 or a == 4:
        return "а"
    else:
        return ""


def ending2(el):
    if el == 1:
        return "-го человека"
    else:
        return "-х человек"


# вынести это в конфиг
API_TOKEN = open("TOKEN.txt").read()
chat = -1001516445146

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

count = 0
sportsmans = dict()
day = 0


@dp.message_handler()
async def plusBot(message: types.Message):
    global count
    global sportsmans
    global day

    message_day = message.date.strftime('%d')
    # механизм скидывания счетчика когда наступает новый день
    if message_day != day:
        count = 0
        sportsmans = dict()

    # если сообщение содержит "+" то происходит магия
    if message.text.find("+") != -1:
        count = count + message.text.count("+")
        name_sportsman = message.from_user.last_name + " " + message.from_user.first_name
        # Проверка,содержится ли плюсанувший челоек уже в словаре
        if name_sportsman in sportsmans.keys():
            sportsmans[name_sportsman] = sportsmans[name_sportsman] + message.text.count("+")
        else:
            sportsmans[name_sportsman] = message.text.count("+")

    # Команда выводящая инфу в чат
    if message.text == "/get":
        await message.answer(f"На тренировку собирается {count} человек{ending(count)}:")
        # вывод имен людей и кол-во приходящих с ними людей
        for key in sportsmans.keys():
            if sportsmans[key] > 1:
                await message.answer(f"{key} приведет с собой еще {sportsmans[key] - 1}{ending2(sportsmans[key] - 1)}")
            else:
                await message.answer(key)

    # перезаписываем глобальную переменную для работы логики сбрасыванию счетчиков
    day = datetime.datetime.now().strftime('%d')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
