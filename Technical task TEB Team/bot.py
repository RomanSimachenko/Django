import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()


import logging
from aiogram import Bot, Dispatcher, executor, types
from main import models
import json


API_TOKEN = os.getenv("API_TOKEN", "")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def start_help(message: types.Message):
    await message.reply("Put a dictionary of the User pairs `\"username\": user_id` in the chat \
            to register them (e. g. {\"un1\": 8765212452, \"usrname2\": 9345608611, .....})")


@dp.message_handler()
async def echo(message: types.Message):
    try:
        users = json.loads(message.text)
    except json.JSONDecodeError:
        await message.reply("Invalid format")
        return

    msg = await register_users(users)

    await message.reply(msg)


async def register_users(users: dict) -> str:
    """Registers user in Django DB"""
    for key in users.keys():
        try:
            models.CustomUser.objects.create_user(
                username=key.strip(),
                password=str(users[key]).strip(),
                is_staff=True
            )
        except:
            return "Failed to create users"

    return "Users registered successfully"


def main():
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()
