# BY LEGENDX22 🔥❤️👍
from db import mongo, api, hash, token
from telethon import TelegramClient as tg
bot = tg(api, hash).start(bot_token=token)
if __name__ == "__main__":
  bot.run_until_disconnected()
