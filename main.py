import telebot
import random
from telebot import types
import sqlite3, os


@bot.message_handler(commands=['start'])
def start(message):
    mess=f'Здравствуй, <b>{message.from_user.first_name}</b>.\nДанный бот выполняет две команды:\n\n🔮 <b>Шар предсказаний</b>. Может помочь вам в принятии решений. Для получения ответа сконцентрируйтесь на своем вопросе и нажмите кнопку "Магический шар".\n\n🔮 <b>Карта дня</b>. Хотите вытянуть карту таро и узнать самый вероятный исход дня? Сконцентрируйтесь и нажмите "Вытянуть карту дня".'
    # Клавиатура у пользователя
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    crystallball = types.KeyboardButton("Магический шар")
    taro = types.KeyboardButton("Вытянуть карту дня")
    markup.add(crystallball, taro)
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)

# Реализация команд
@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.chat.type == 'private':
        # Магический шар
        if message.text == 'Магический шар':
            random1=str(random.randint(1,20))
            bot.send_message(message.chat.id, "🔮")
            db = sqlite3.connect('database.db')
            cursor = db.cursor()
            print("Подключен к SQLite")
            sql_fetch_blob_query1 = "SELECT * FROM magicball WHERE id = %s" %(random1)
            cursor.execute(sql_fetch_blob_query1)
            record1 = cursor.fetchall()
            for row1 in record1:
                name1 = row1[1]
            bot.send_message(message.chat.id, name1)
        # Карта дня
        elif message.text == 'Вытянуть карту дня':
            stolbec=str(random.randint(1,78))
            db = sqlite3.connect('database.db')
            cursor = db.cursor()
            print("Подключен к SQLite")
            sql_fetch_blob_query = "SELECT * FROM taroinfo WHERE id = %s" %(stolbec)
            cursor.execute(sql_fetch_blob_query)
            record = cursor.fetchall()
            for row in record:
                name = row[1]
                photo = row[2]
                photo_path = os.path.join(stolbec + ".jpg")
                with open(photo_path, 'wb') as file:
                    file.write(photo)
                print("Данный из blob сохранены в: ", photo_path, "\n")
                photoforbot = open(photo_path, 'rb')
                bot.send_photo(message.chat.id, photoforbot, name)
                del photoforbot

            cursor.close()
            bot.send_message(message.chat.id, '<b>СОВЕТ ОТ astrohelper:</b>\nСтарайтесь не вытягивать больше одной карты в день.', parse_mode='html')
            os.remove(photo_path)
        else:
            bot.send_message(message.chat.id, "Я не понимаю, выберите, пожалуйста, команду 🥺", parse_mode='html')

# Выводит ошибку, направляя пользователя, если он не выбрал команду
@bot.message_handler(content_types=['photo'])
def get_user_text(message):
    bot.send_message(message.chat.id, "Я не понимаю, выберите, пожалуйста, команду 🥺", parse_mode='html')
@bot.message_handler(content_types=['audio'])
def get_user_text(message):
    bot.send_message(message.chat.id, "Я не понимаю, выберите, пожалуйста, команду 🥺", parse_mode='html')
@bot.message_handler(content_types=['voice'])
def get_user_text(message):
    bot.send_message(message.chat.id, "Я не понимаю, выберите, пожалуйста, команду 🥺", parse_mode='html')
@bot.message_handler(content_types=['document'])
def get_user_text(message):
    bot.send_message(message.chat.id, "Я не понимаю, выберите, пожалуйста, команду 🥺", parse_mode='html')
@bot.message_handler(content_types=['sticker'])
def get_user_text(message):
    bot.send_message(message.chat.id, "Я не понимаю, выберите, пожалуйста, команду 🥺", parse_mode='html')
@bot.message_handler(content_types=['video'])
def get_user_text(message):
   bot.send_message(message.chat.id, "Я не понимаю, выберите, пожалуйста, команду 🥺", parse_mode='html')
bot.polling(none_stop=True)