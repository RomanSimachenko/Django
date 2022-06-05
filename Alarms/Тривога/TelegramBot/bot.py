import asyncio
import logging
from aiogram import Bot, Dispatcher, executor, types
import os
from parsing import get_alarms, get_chat_id_and_name
import aioschedule
import sys
import sqlite3
import json

KEY_WORDS = ["Рівне", "Сарн", "Дубровиц"]

API_TOKEN = os.getenv('API_TOKEN')

chat_id, chat_name = get_chat_id_and_name(
    url=f"https://api.telegram.org/bot{API_TOKEN}/getUpdates")

try:
    connection = sqlite3.connect('chat_ids.db')
    cursor = connection.cursor()
except Exception as error:
    print(error)

cursor.execute("""CREATE TABLE IF NOT EXISTS chats (
    ID INT,
    name TEXT,  
    key_words TEXT,
    PRIMARY KEY(ID));
""")
connection.commit()

if chat_id and chat_name:
    flag = False
    cursor.execute("""SELECT ID, name, key_words from chats;""")
    rows = cursor.fetchall()
    connection.commit()
    for pk, name, key_words in rows:
        if pk == chat_id:
            flag = True
            break
    if flag:
        cursor.execute(
            f"""UPDATE chats SET name="{chat_name}" WHERE ID={chat_id};""")
        connection.commit()
    else:
        cursor.execute(f"""INSERT INTO chats (ID, name, key_words) 
            VALUES ({chat_id}, "{chat_name}", "{KEY_WORDS}");""")
        connection.commit()
elif chat_id:
    cursor.execute("SELECT ID, name, key_words from chats")
    rows = cursor.fetchall()
    connection.commit()
    for pk, name, key_words in rows:
        if chat_id == pk:
            chat_name = name
            break
elif chat_name:
    cursor.execute("SELECT ID, name, key_words from chats")
    rows = cursor.fetchall()
    connection.commit()
    for pk, name, key_words in rows:
        if name == chat_name:
            chat_id = pk
            break
else:
    print("No chat id and chat name!")
    sys.exit()
# print(chat_id, chat_name)

logging.basicConfig(level=logging.ERROR)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


async def get_active_alarms_by_key_words():
    global active_alarms_by_key_words
    active_alarms_by_key_words = []
    for name, info in json.load(open("alarms.json")).items():
        for rayon, rayon_info in info['districts'].items():
            for word in KEY_WORDS:
                if word.lower() in rayon.lower():
                    if rayon_info['enabled']:
                        active_alarms_by_key_words.append(rayon)
        for word in KEY_WORDS:
            if word.lower() in name.lower():
                if info['enabled']:
                    active_alarms_by_key_words.append(name)


async def send_active_alarms_by_key_words():
    if active_alarms_by_key_words:
        await bot.send_message(chat_id, "@Gardarg @dkn3r @Xotaruu @arekusanda_kegayawa @r0m1mPL")
        for name in active_alarms_by_key_words:
            await bot.send_message(chat_id, f"🔴 Повітряна тривога {name}!!!")


async def scheduler1():
    aioschedule.every(15).seconds.do(get_active_alarms_by_key_words)


async def scheduler2():
    aioschedule.every(300).seconds.do(send_active_alarms_by_key_words)


async def scheduler3():
    aioschedule.every(10).seconds.do(get_alarms)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def main(_):
    asyncio.create_task(scheduler1())
    asyncio.create_task(scheduler2())
    asyncio.create_task(scheduler3())

    @dp.message_handler(commands='alarms')
    async def alarms(message: types.Message):
        active_alarms = []
        for key, value in json.load(open("alarms.json")).items():
            if value['enabled']:
                active_alarms.append(key)
            for k2, v2 in value['districts'].items():
                if v2['enabled']:
                    active_alarms.append(k2)

        if active_alarms:
            await message.answer("Активні повітряні тривоги🚨: ")
            for alarm in active_alarms:
                await message.answer(alarm)
        else:
            await message.answer("Активних повітряних тривог немає.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=main)
