import os
import asyncio
from highrise import BaseBot, __main__
from highrise.models import BotDefinition

# Credentials are pulled from your Railway Variables
TOKEN = os.getenv("TOKEN")
ROOM_ID = os.getenv("ROOM_ID")

class MyBot(BaseBot):
    async def on_start(self, session_metadata) -> None:
        print("Bot connected!")
        await self.highrise.chat("Hello! I am online.")

    async def on_chat(self, user, message: str) -> None:
        if message == "!help":
            await self.highrise.chat("I am working!")

# This structure packages the bot correctly for the SDK
definitions = [BotDefinition(MyBot, ROOM_ID, TOKEN)]

if __name__ == "__main__":
    if not TOKEN or not ROOM_ID:
        print("CRITICAL ERROR: TOKEN or ROOM_ID not detected.")
    else:
        # Pass the defined list to the main function
        asyncio.run(__main__.main(definitions))