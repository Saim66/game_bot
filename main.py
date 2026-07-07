import os
from highrise import BaseBot, __main__
import asyncio

class MyBot(BaseBot):
    async def on_start(self, session_metadata) -> None:
        print("Bot connected!")
        await self.highrise.chat("Hello! I am online.")

    async def on_chat(self, user, message: str) -> None:
        if message == "!help":
            await self.highrise.chat("I am working!")

if __name__ == "__main__":
    # Ensure variables exist
    if not os.getenv("TOKEN") or not os.getenv("ROOM_ID"):
        print("Error: TOKEN or ROOM_ID not found in environment!")
    else:
        # This is the standard, library-approved way to run the bot.
        # It internally reads the TOKEN and ROOM_ID variables.
        asyncio.run(__main__.main([MyBot]))