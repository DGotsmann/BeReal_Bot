import asyncio
from telegram import Bot

TOKEN = "7897872563:AAG6h-O8_Ewwcn_fluAEFl9iLaDElZIpuoI"
CHAT_ID = -1002499415062  # Your group chat ID

async def send_message():
    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text="Test message from bot!")

# Run the async function
asyncio.run(send_message())
