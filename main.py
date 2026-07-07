import os
import asyncio
from highrise import BaseBot, __main__

class MyBot(BaseBot):
    async def on_start(self, session_metadata) -> None:
        print("Bot connected successfully!")

if __name__ == "__main__":
    # The modern SDK handles credentials automatically from environment variables
    # We pass the class directly as a list
    asyncio.run(__main__.main([MyBot]))