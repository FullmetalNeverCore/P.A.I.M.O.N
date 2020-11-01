import logging
import telebot
from bs4 import BeautifulSoup as BS 
import requests
from datetime import datetime, time, timedelta
import time
import schedule

u_id = "497185921"
token = "1425708349:AAHHzf5dwC1M7L6tlV1ecs_aYriHb1yAuP4"
bot = telebot.TeleBot(token)
logging.basicConfig(level=logging.INFO)


def paimon_got_some_news():
    r = requests.get(f"https://www.bing.com/news/search?q=genshin+impact&qpvt=genshin+impact&FORM=EWRE")
    html = BS(r.content, 'html.parser')

    t = open("file.txt", "r", encoding='utf-8')
    c_l = t.readlines()
    print(c_l)


    for el in html.select('#news.news.search.verx'):
        text = el.select('a.title')[0].text
        print(text)
        if text in c_l:
            print("Its already in the list.")
        else:
            t = open("file.txt", "w", encoding='utf-8')
            tr = t.write(str(text))
            bot.send_message(u_id, text) 



@bot.message_handler(commands=['start'])
def start(message):
    u_id = message.chat.id
    bot.send_message(u_id, "Heyy!Now Paimon will send u some news,once a day!")



while True:
    now = datetime.now().time()
    if now.hour == 12 and now.minute == 00:
        paimon_got_some_news()
        time.sleep(60)
    else:
        time.sleep(60)
