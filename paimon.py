import logging
from aiogram import Bot, Dispatcher, executor, md, types
from bs4 import BeautifulSoup as BS 
import requests
from datetime import datetime, time, timedelta
import time
import schedule
import asyncio


u_id = #urtoken
token = #urkey
bot = Bot(token= token, parse_mode=types.ParseMode.MARKDOWN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

print("Ehe te nandoyo!")

def paimon_got_some_news():
    u_id = #urtoken
    token = #urkey
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
            print("1")
            send_message = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + u_id + '&parse_mode=Markdown&text=' + text
            send_response = requests.get(send_message)
            return send_response.json()


schedule.every(5).hours.do(paimon_got_some_news)

while True:
    schedule.run_pending()
    time.sleep(1)


if __name__ == '__main__':
        executor.start_polling(dp, skip_updates=True)
