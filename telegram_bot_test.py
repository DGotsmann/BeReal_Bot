import random
import asyncio
import schedule
from telegram.ext import Application

TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = -1002499415062  # Your group's chat ID

async def send_message(app: Application):
    """Sends a message to the group chat."""
    await app.bot.send_message(chat_id=CHAT_ID, text="Hello! This is your random daily message.")

def schedule_random_time(app: Application):
    """Schedules the message at a new random time each day."""
    hour = random.randint(8, 22)  # Between 8 AM and 10 PM
    minute = random.randint(0, 59)
    schedule.clear()  # Clear any previous schedules
    schedule.every().day.at(f"{hour:02d}:{minute:02d}").do(
        lambda: asyncio.run_coroutine_threadsafe(send_message(app), asyncio.get_running_loop())
    )
    print(f"✅ Scheduled message at {hour:02d}:{minute:02d} today.")

def reset_random_time(app: Application):
    """Reset the random time at midnight."""
    schedule.every().day.at("00:00").do(schedule_random_time, app)  # Recalculate random time at midnight

async def main():
    """Main async function to run the bot and scheduling."""
    app = Application.builder().token(TOKEN).build()

    # Schedule the first message with a random time
    schedule_random_time(app)

    # Reset the random time every day at midnight
    reset_random_time(app)

    # Run the scheduler loop
    while True:
        schedule.run_pending()
        await asyncio.sleep(60)  # Check every minute

if __name__ == "__main__":
    asyncio.run(main())
