
from settings import bot_key
import os
import telebot
from telebot import types


# openai.api_key = os.getenv(Api_key)
bot = telebot.TeleBot(bot_key)

# @bot.message_handler(func = lambda _: True)
# def handle_message(message):
#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=message.text,
#         temperature=0.5,
#         max_tokens=60,
#         top_p=1.0,
#         frequency_penalty=0.5,
#         presence_penalty=0.0,
#     )
#     bot.send_message(chat_id=message.from_user.id, text=response['choices'][0]['text'])

# bot.polling()

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Поехали! можете что написать)', parse_mode='html')


@bot.message_handler(func = lambda message: message.text.lower() == 'привет')
def get_user_answer(message):
     mess = f'Привет, <b>{message.from_user.first_name}</b>, меня зовут <b>Раф</b>'
     bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(func = lambda message: message.text.lower() == 'как дела' or 'как дела?')
def get_user_answer(message):
     mess = f'Привет, <b>{message.from_user.first_name}</b>, меня зовут Раф'
     bot.send_message(message.chat.id, mess, parse_mode='html')



@bot.message_handler()
def get_user_answer(message):
     bot.send_message(message.chat.id, f'Я повторяшка - повторяю :{message.text}', parse_mode='html')
     
    


bot.polling(non_stop=True) #postoyanaya rabota