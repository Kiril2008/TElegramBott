import telebot
import config
import random
 
from telebot import types
 
bot = telebot.TeleBot(7792102487:AAF9JmeR3Th9T7_BOwPWP-DN8G91f_72op0s)
 
@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
 
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Рандомне число")
    item2 = types.KeyboardButton("😊 ЯК справи ?")
 
    markup.add(item1, item2)
 
    bot.send_message(message.chat.id, "Привіт, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот створений для тестів.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
 
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '🎲 рандомне число':
            bot.send_message(message.chat.id, str(random.randint(0,100)))
        elif message.text == '😊 як справи?':
 
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("добре", callback_data='good')
            item2 = types.InlineKeyboardButton("Не дуже ", callback_data='bad')
 
            markup.add(item1, item2)
 
            bot.send_message(message.chat.id, 'чудово, сам як?', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'я не знаю що відповісти  😢')
 
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот і чудово 😊')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'буває 😢')
 
            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
                reply_markup=None)
 
            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="ЦЕ ТЕСТОВЕ ПОВІДОМЛЕННЯ!!11")
 
    except Exception as e:
        print(repr(e))
 
# RUN
bot.polling(none_stop=True)