from highrise import BaseBot

class MyBot(BaseBot):
    async def on_start(self, session_metadata) -> None:
        print("Bot has successfully connected to the room!")

    # Add 'position' as the second argument here
    async def on_user_join(self, user, position) -> None:
        await self.highrise.chat(f"Welcome to the room, {user.username}!")
        
    async def on_chat(self, user, message: str) -> None:
        if message.lower() == "!hello":
            await self.highrise.chat(f"Hello {user.username}!")