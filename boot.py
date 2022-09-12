# This example requires the 'message_content' intent.

import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTAxODcwNzg4ODU2NDMzODcwOA.Gyf2w4.zGgj8jhyUgl2Jsflw6iLskM70_cJwGncp5Az_Q')
