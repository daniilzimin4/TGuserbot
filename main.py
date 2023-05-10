from pyrogram import Client, filters
from pyrogram.errors import FloodWait

import time
from datetime import datetime
from random import randint
from time import sleep
import random

from config import *
from db_work import Database
from messages import *

app = Client("my_account", api_id=configID, api_hash=configHASH)
db = Database()


# отправить 1000-7 -14 -21 и картинку в начале
@app.on_message(filters.command("ded_inside", prefixes=".") & filters.me)
def ded_inside(_, msg):
    msg.delete()
    app.send_photo(msg.chat.id, "gul.jpg")
    x = 1000
    while x > 0:
        app.send_message(msg.chat.id, str(x) + "-7")
        x -= 7


# список всех возможных команд
@app.on_message(filters.command("help", prefixes=".") & filters.me)
def help(_, msg):
    msg.edit(ALLCOMMANDS)


# Отправить спокойной ночи 100 раз
@app.on_message(filters.command("spoki", prefixes=".") & filters.me)
def spoki(_, msg):
    msg.delete()
    for i in range(100):
        app.send_message(msg.chat.id, "𝚜𝚙𝚘𝚔𝚘𝚒𝚗𝚘𝚒 𝚗𝚘𝚌𝚑𝚒")


# Отправить текст песни по строчкам (делит одно сообщение на несколько)
@app.on_message(filters.command("song", prefixes=".") & filters.me)
def spoki(_, msg):
    msg.delete()
    s = msg.text[6:].split("\n")
    for i in s:
        app.send_message(msg.chat.id, i)
        sleep(0.1)


# Отправить споки 1 раз
@app.on_message(filters.command("spoki_one", prefixes=".") & filters.me)
def spoki_one(_, msg):
    msg.delete()
    app.send_message(msg.chat.id, "𝚜𝚙𝚘𝚔𝚘𝚒𝚗𝚘𝚒 𝚗𝚘𝚌𝚑𝚒")


# auto game for the theorem 3x + 1 ---> 1
@app.on_message(filters.command("3x1game", prefixes=".") & filters.me)
def fuckingGAME(_, msg):
    x = int(msg.text[12:])
    msg.delete()
    while x != 1:
        if x % 2 == 0:
            x //= 2
        else:
            x = x * 3 + 1
        app.send_message(msg.chat.id, x)
        sleep(0.1)


# Отправить несколько раз одно сообщение -- ".spam 10 some words"
@app.on_message(filters.command("spam", prefixes=".") & filters.me)
def spam(_, msg):
    msg.delete()
    s = msg.text[6:].split(" ", maxsplit=1)
    for i in range(int(s[0])):
        sleep(0.5)
        app.send_message(msg.chat.id, s[1])


# Отправить RIP
@app.on_message(filters.command("rip", prefixes=".") & filters.me)
def rip(_, msg):
    msg.edit(RIP)


# Отправить сердчеко
@app.on_message(filters.command("love2", prefixes=".") & filters.me)
def rip(_, msg):
    msg.edit(LOVE2)


# Отправить LOVE
@app.on_message(filters.command("love", prefixes=".") & filters.me)
def love(_, msg):
    for i in LOVE:
        sleep(0.5)
        msg.edit(i)


# Отправить PRESS_F
@app.on_message(filters.command("pressF", prefixes=".") & filters.me)
def pressF(_, msg):
    msg.edit(PRESSF)

# Отправить PRESSF2
@app.on_message(filters.command("pressF2", prefixes=".") & filters.me)
def pressf2(_, msg):
    msg.edit(PRESSF2)


# Отправить LOL
@app.on_message(filters.command("lol", prefixes=".") & filters.me)
def lol(_, msg):
    msg.edit(LOL)


# Отправить bruh
@app.on_message(filters.command("bruh", prefixes=".") & filters.me)
def bruh(_, msg):
    msg.edit(BRUH)


# Изменять сообщение рандомными словами и удалять
@app.on_message(filters.command("randwords", prefixes=".") & filters.me)
def randwords(_, msg):
    cnt = int(msg.text.split(".randwords ", maxsplit=1)[1])
    last = -1
    for i in range(cnt):
        now = randint(0, CNTRANDOMWORDS - 1)
        while now == last:
            now = randint(0, CNTRANDOMWORDS - 1)
        last = now

        try:
            msg.edit(RANDOWWORDS[now])
            sleep(0.1)
        except FloodWait as e:
            sleep(e.x)

    msg.delete()


# Стикер, который выбивает шесть на кубике
@app.on_message(filters.command("cube", prefixes=".") & filters.me)
def cube(_, msg):
    try:
        emoj = msg.text.split(".cube ", maxsplit=1)[1]
        msg.delete()
    except Exception as error:
        msg.edit("neeeeeed emoji")
        sleep(5)
        msg.delete()
        return

    need = 6

    if emoj == "🏀":
        need = 5
    elif emoj == "⚽️":
        need = 5

    test = app.send_dice(msg.chat.id, emoj)
    while test.dice.value != need:
        test.delete()
        test = app.send_dice(msg.chat.id, emoj)


# Команда type
@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = ""  # to be printed
    typing_symbol = "-"

    while (tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05)  # 50 ms

            tbp = tbp + text[0]
            text = text[1:]

            msg.edit(tbp)
            sleep(0.05)

        except FloodWait as e:
            sleep(e.x)


# Команда взлома пентагона
@app.on_message(filters.command("hack", prefixes=".") & filters.me)
def hack(_, msg):
    perc = 0

    while (perc < 100):
        try:
            text = "👮‍ Взлом пентагона в процессе ..." + str(perc) + "%"
            msg.edit(text)

            perc += random.randint(1, 3)
            sleep(0.1)

        except FloodWait as e:
            sleep(e.x)

    msg.edit("🟢 Пентагон успешно взломан!")
    sleep(3)

    msg.edit("👽 Поиск секретных данных об НЛО ...")
    perc = 0

    while (perc < 100):
        try:
            text = "👽 Поиск секретных данных об НЛО ..." + str(perc) + "%"
            msg.edit(text)

            perc += random.randint(1, 5)
            sleep(0.15)

        except FloodWait as e:
            sleep(e.x)

    msg.edit("🦖 Найдены данные о существовании динозавров на земле!")


# Переход в АФК режим
@app.on_message(filters.command("afk", prefixes=".") & filters.me)
def afk(_, msg):
    db.set_my_afk(1)
    if msg.text == ".afk":
        orig_text = "null"
    else:
        orig_text = msg.text.split(".afk ", maxsplit=1)[1]
    db.set_reason(orig_text)
    db.set_time_afk(time.time())
    text = f'''<b>Я теперь в AFK.</b>'''
    msg.edit(text)


# Выход из АФК режима
@app.on_message(filters.command("unafk", prefixes=".") & filters.me)
def unafk(_, msg):
    db.set_my_afk(0)
    text = f"<b>Я больше не в AFK.</b>"
    msg.edit(text)


# Команда ответа на входящие сообщения
@app.on_message(filters.private)
async def hello(client, message):
    # print(message)
    if str(message.chat.type) == "ChatType.PRIVATE":
        if my != message.from_user.id and db.get_my_afk() == 1:
            current_time = datetime.fromtimestamp(int(time.time()) - db.get_time_afk())
            if db.get_reason() == "null":
                text = f'''<b>Я сейчас в AFK(Уже {current_time.hour - 3}:{current_time.minute}:{current_time.second}).</b>'''
            else:
                text = f'''<b>Я сейчас в AFK(Уже {current_time.hour - 3}:{current_time.minute}:{current_time.second}).
Причина: </b>''' + db.get_reason()
            await message.reply_text(text)


app.run()
