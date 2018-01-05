import telepot
import requests
import time
import configparser


def handle(message):
    chat_id = message['chat']['id']
    command = message['text']

    if command == '/showmyip':
        req = requests.get("http://ipecho.net/plain")
        bot.sendMessage(chat_id, "My ip is " + req.text)


config = configparser.RawConfigParser()
config.read("config.ini")
bot = telepot.Bot(config.get("application", "bot_id"))
bot.message_loop(handle)

print("Running bot")
while True:
    time.sleep(10)