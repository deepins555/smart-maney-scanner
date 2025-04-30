import asyncio
from telegram import Bot
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

bot = Bot(token=TELEGRAM_BOT_TOKEN)

async def main():
    text = "✅ Бот запущено і працює. Smart Money Scanner активний!"
    await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=text)
    print("Працює сканер...")

if __name__ == "__main__":
    asyncio.run(main())
