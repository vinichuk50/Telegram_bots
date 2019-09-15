import pyowm
import telebot

owm = pyowm.OWM('8c3b544846d8565aac55c1a95065ca86', language = 'UA')
bot = telebot.TeleBot("933030682:AAGm3jklrWiFUw4G0q5K3YkSxBxTTRlCX-s")
@bot.message_handler(commands=['start'])
def send_welcome(message):
 bot.send_message(message.chat.id, "Привіт Вікуся ♥\n\n🤖Я маленький ботик створений для тебе!\n✍Напиши мені своє місто і я тобі покажу погоду!")
#@bot.message_handler(commands=['help'])
#def send_welcome(message):
  #bot.reply_to(message, "Давай для начала я тебе расскажу несколько правил!\nНазвание города писать только на языке на котором люди говорят там!")

@bot.message_handler(content_types=['text'])
def send_echo(message):
  observation = owm.weather_at_place( message.text )
  w = observation.get_weather()
  temp = w.get_temperature('celsius')["temp"]
  wind = w.get_wind()["speed"]
  hum = w.get_humidity()
  time = w.get_reference_time(timeformat='iso')



  answer = "В місті " + message.text + " зараз: " + w.get_detailed_status() + "\n---------------------"
  answer += "\nТемпература: " + str(temp) + "°C" + "\n---------------------" + "\nШвидкість вітру: " + str(wind) + "м/с." +  "\n---------------------" 
  if temp < 10:
    answer += "\nЗараз дуже холодно, приб'ю якщо погано одягнеся!"
  if temp < 20:
    answer += "\nЗараз прохладно, тепло одягайся!"
  elif temp < 40:
    answer += "\nЗараз тепло, одягайся як хочеш!"
  else:
    answer += "\nТемпература нормальная!"

  bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True )
input()