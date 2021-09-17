import logging, datetime, configparser
from functions import ending as ending
from functions import ending2 as ending2
from aiogram import Bot, Dispatcher, executor, types

# Settings
config = configparser.ConfigParser()
config.read("config.ini")
API_TOKEN = config.get('Settings', 'token')
CHAT = config.getint('Settings', 'id_chat')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Global variables
count = 0
sportsmans = dict()
day = 0


@dp.message_handler()
async def plusBot(message: types.Message):
    global count
    global sportsmans
    global day
    # определяем в какой день сообщение отправлено
    message_day = message.date.strftime('%d')
    # механизм скидывания счетчика когда наступает новый день
    if message_day != day:
        count = 0
        sportsmans = dict()

    # если сообщение содержит "+" то происходит магия, а так же проверка чата, чтобы исключить обращения к боту в личку
    if message.text.find("+") != -1 and message.chat.id == CHAT:
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
