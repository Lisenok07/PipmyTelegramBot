import telebot
bot = telebot.TeleBot('6973612361:AAFa-LTKrDCuVvKjvMMqf8Z_WJ-gm__FVc8')
@bot.message_handler(content_types=['text'])
def get_text_messages(message, chat_id="-1P001913381881"):
    kolichestvoPosylov = 0
    if "пошел нахуй" in message.text:
        kolichestvoPosylov = kolichestvoPosylov+ 1
        bot.send_message(chat_id=chat_id, text=kolichestvoPosylov)
    if "пошёл нахуй" in message.text:
        kolichestvoPosylov = kolichestvoPosylov+ 1
        bot.send_message(chat_id=chat_id, text=kolichestvoPosylov)
    if "иди нахуй" in message.text:
        kolichestvoPosylov = kolichestvoPosylov+ 1
        bot.send_message(chat_id=chat_id, text=kolichestvoPosylov)
bot.polling(none_stop=True, interval=0)