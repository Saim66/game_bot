import os
import asyncio
from highrise import BaseBot, __main__

# Credentials from Railway Variables
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
        # Run the bot using the simplest method possible
        asyncio.run(__main__.main(MyBot, ROOM_ID, TOKEN))