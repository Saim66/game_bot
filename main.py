import os
import asyncio
from highrise import BaseBot, __main__

# Credentials
TOKEN = os.getenv("TOKEN")
ROOM_ID = os.getenv("ROOM_ID")

class MyBot(BaseBot):
    async def on_start(self, session_metadata) -> None:
        print("Bot connected successfully!")
        await self.highrise.chat("Hello! I am online.")

    async def on_chat(self, user, message: str) -> None:
        if message == "!help":
            await self.highrise.chat("I am working!")

if __name__ == "__main__":
    if not TOKEN or not ROOM_ID:
        print("CRITICAL: TOKEN or ROOM_ID missing.")
    else:
        # Use a list of dictionaries. This is compatible with all SDK versions.
        bot_list = [{"bot": MyBot(), "room_id": ROOM_ID, "api_token": TOKEN}]
        asyncio.run(__main__.main(bot_list))