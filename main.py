import telegram

# нужно реализовать бота которой в чате будет в сообщениях от пользователей вычленять сообщения с знаком "+" и
# подсчитывать их по команде, так же необходимо реалиазовать сброс каунта каждый день в 00:00 минут по московскому
# времени(+3)


TOKEN = open("TOKEN.txt").read()
bot = telegram.Bot(token=TOKEN)
# проверяем работу бота
print(bot.get_me())


# получаем обновления от бота,,,,
updates = bot.get_updates()


for upd in updates:
   print(upd.message.text)
   if upd.message.text == "+":
       print("True")
   else:
       print("False")

