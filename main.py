import os
import random
import asyncio
from highrise import BaseBot, __main__

# Credentials are pulled from your Railway Variables tab
TOKEN = os.getenv("TOKEN")
ROOM_ID = os.getenv("ROOM_ID")

class MyBot(BaseBot):
    async def on_start(self, session_metadata) -> None:
        print("Bot has successfully connected!")
        await self.highrise.chat("Hello! I am online and ready to play.")

    async def on_user_join(self, user, position) -> None:
        await self.highrise.chat(f"Welcome {user.username}! Type !help to see my games.")

    async def on_chat(self, user, message: str) -> None:
        cmd = message.lower().strip()

        if cmd == "!help":
            await self.highrise.chat("Games available: !trivia, !riddle, !guess")
        
        elif cmd == "!trivia":
            await self.highrise.chat("Trivia: What is the largest planet in our solar system?")
            
        elif cmd == "!riddle":
            await self.highrise.chat("Riddle: I speak without a mouth and hear without ears. What am I?")
            
        elif cmd == "!guess":
            await self.highrise.chat("Guessing Game: I'm thinking of a number 1-10. Type your guess!")

if __name__ == "__main__":
    # DEBUG: This print will show up in your Railway 'Logs' tab
    print(f"DEBUG Check - Token found: {bool(TOKEN)}")
    print(f"DEBUG Check - Room ID found: {bool(ROOM_ID)}")

    if not TOKEN or not ROOM_ID:
        print("CRITICAL ERROR: TOKEN or ROOM_ID not detected in environment variables.")
    else:
        asyncio.run(__main__.main(MyBot))