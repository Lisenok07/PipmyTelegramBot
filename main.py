import telebot
bot = telebot.TeleBot('6767944688:AAHrqQ3qq2rTUHnYdPaFzJ13sk7c1cI5TXE')
@bot.message_handler(content_types=['text'])
def get_text_messages(message, chat_id="-1001913381881"):
    if "нахуй" in message.text:
         bot.send_photo(chat_id=chat_id, photo=open('/home/lisa/Downloads/Telegram Desktop/pipmy_agadmtoaaklrseg.png', 'rb'))
         #bot.send_photo(chat_id=chat_id, photo=open('/home/lisa/Downloads/Telegram Desktop/pipmy_agadykqaaudrmes.png', 'rb'))
    if "на хуй" in message.text:
         bot.send_photo(chat_id=chat_id, photo=open('/home/lisa/Downloads/Telegram Desktop/pipmy_agadmtoaaklrseg.png', 'rb'))
         bot.send_photo(chat_id=chat_id, photo=open('/home/lisa/Downloads/Telegram Desktop/pipmy_agadykqaaudrmes.png', 'rb'))
    if "На хуй" in message.text:
         bot.send_photo(chat_id=chat_id, photo=open('/home/lisa/Downloads/Telegram Desktop/pipmy_agadmtoaaklrseg.png', 'rb'))
         bot.send_photo(chat_id=chat_id, photo=open('/home/lisa/Downloads/Telegram Desktop/pipmy_agadykqaaudrmes.png', 'rb'))
    if "лето" in message.text:
        bot.send_photo(chat_id=chat_id, photo=open('/home/lisa/Downloads/Telegram Desktop/pipmy_agadmtoaaklrseg.png', 'rb'))
    if "лета" in message.text:
        bot.send_photo(chat_id=chat_id,photo=open('/home/lisa/Downloads/Telegram Desktop/pipmy_agadmtoaaklrseg.png', 'rb'))
    if "литр" in message.text:
        bot.send_photo(chat_id=chat_id,photo=open('/home/lisa/Downloads/Telegram Desktop/pipmy_agadykqaaudrmes.png', 'rb'))
    if "Нахуй" in message.text:
         bot.send_photo(chat_id=chat_id, photo=open('/home/lisa/Downloads/Telegram Desktop/pipmy_agadmtoaaklrseg.png', 'rb'))
         #bot.send_photo(chat_id=chat_id, photo=open('/home/lisa/Downloads/Telegram Desktop/pipmy_agadykqaaudrmes.png', 'rb'))
    if "Лето" in message.text:
        bot.send_photo(chat_id=chat_id, photo=open('/home/lisa/Downloads/Telegram Desktop/pipmy_agadmtoaaklrseg.png', 'rb'))
    if "Лета" in message.text:
        bot.send_photo(chat_id=chat_id,photo=open('/home/lisa/Downloads/Telegram Desktop/pipmy_agadmtoaaklrseg.png', 'rb'))
    if "Литр" in message.text:
        bot.send_photo(chat_id=chat_id,photo=open('/home/lisa/Downloads/Telegram Desktop/pipmy_agadykqaaudrmes.png', 'rb'))
    if "трамвай" in message.text:
        bot.send_photo(chat_id=chat_id,photo=open('/home/lisa/Downloads/Telegram Desktop/pipmy_agadgi8aaleeges.png', 'rb'))
    if "Трамвай" in message.text:
        bot.send_photo(chat_id=chat_id,photo=open('/home/lisa/Downloads/Telegram Desktop/pipmy_agadgi8aaleeges.png', 'rb'))
    if "рыба" in message.text:
        bot.send_photo(chat_id=chat_id,photo=open('/home/lisa/Downloads/Telegram Desktop/pipmy_agad8zcaaunqces.png', 'rb'))
    if "Рыба" in message.text:
        bot.send_photo(chat_id=chat_id,photo=open('/home/lisa/Downloads/Telegram Desktop/pipmy_agad8zcaaunqces.png', 'rb'))
    if "кофе" in message.text:
        bot.send_photo(chat_id=chat_id,photo=open('/home/lisa/Downloads/Telegram Desktop/pipmy_agadqteaaskxceo.png', 'rb'))
    if "Кофе" in message.text:
        bot.send_photo(chat_id=chat_id,photo=open('/home/lisa/Downloads/Telegram Desktop/pipmy_agadqteaaskxceo.png', 'rb'))
    if "Шикарно" in message.text:
        bot.send_photo(chat_id=chat_id,photo=open('/home/lisa/Downloads/Telegram Desktop/pipmy_agadsdqaahu-oes.png', 'rb'))
    if "шикарно" in message.text:
        bot.send_photo(chat_id=chat_id,photo=open('/home/lisa/Downloads/Telegram Desktop/pipmy_agadsdqaahu-oes.png', 'rb'))
    if "Бан" in message.text:
        bot.send_photo(chat_id=chat_id,photo=open('/home/lisa/Downloads/Telegram Desktop/pipmy_agadodcaaimiees.png', 'rb'))
    if "бан" in message.text:
        bot.send_photo(chat_id=chat_id,photo=open('/home/lisa/Downloads/Telegram Desktop/pipmy_agadodcaaimiees.png', 'rb'))
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши нахуй")
bot.polling(none_stop=True, interval=0)