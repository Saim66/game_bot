import os
import asyncio
from highrise import BaseBot, Highrise

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

async def main():
    bot = MyBot()
    # Direct connection avoids the TypeError from the SDK's main()
    async with Highrise(TOKEN, ROOM_ID) as h:
        await h.run(bot)

if __name__ == "__main__":
    if not TOKEN or not ROOM_ID:
        print("Error: TOKEN or ROOM_ID missing!")
    else:
        asyncio.run(main())