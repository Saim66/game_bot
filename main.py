import os
import random
from highrise import BaseBot, __main__

# Credentials are loaded at runtime from Railway's 'Variables' tab
TOKEN = os.getenv("TOKEN")
ROOM_ID = os.getenv("ROOM_ID")

class MyBot(BaseBot):
    async def on_start(self, session_metadata) -> None:
        print("Bot is running!")

    async def on_user_join(self, user, position) -> None:
        await self.highrise.chat(f"Welcome {user.username}! Type !help to see what I can do.")

    async def on_chat(self, user, message: str) -> None:
        cmd = message.lower().strip()

        if cmd == "!help":
            await self.highrise.chat("Games: !trivia, !riddle, !guess")
        
        elif cmd == "!trivia":
            await self.highrise.chat("Trivia: What is the largest planet in our solar system?")
            
        elif cmd == "!riddle":
            await self.highrise.chat("Riddle: The more of this there is, the less you see. What is it?")
            
        elif cmd == "!guess":
            number = random.randint(1, 10)
            await self.highrise.chat(f"I'm thinking of a number 1-10. Guess it!")

# This tells the SDK how to run the bot
if __name__ == "__main__":
    from highrise import __main__
    # This keeps the bot alive using your environment variables
    # You will use the terminal command: python main.py