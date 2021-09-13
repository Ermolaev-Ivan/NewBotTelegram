import telegram

# нужно реализовать бота которой в чате будет в сообщениях от пользователей вычленять сообщения с знаком "+" и
# подсчитывать их по команде, так же необходимо реалиазовать сброс каунта каждый день в 00:00 минут по московскому
# времени(+3)

def main():
    TOKEN = open("TOKEN.txt").read()
    bot = telegram.Bot(token=TOKEN)
    # проверяем работу бота
    print(bot.get_me())


    # получаем обновления от бота
    updates = bot.get_updates()

    count = 0
    # переделать список users на словарь, где будет значание username : кол-во плюсов,
    # и переделать с этими условиями весь цикл
    users = []

    for upd in updates:
        print(upd.message.text)
        if "+" in upd.message.text and upd.message.chat.username not in users:
            count += upd.message.text.count("+")
            users.append(upd.message.chat.username)
        else:
            pass

    print(count)



