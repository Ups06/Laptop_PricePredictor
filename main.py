#App ID: 1299750679375642654
#Public Key: 6c2c2e8ac0046894a7780e477e7dd804ea58eaf8612242f9776a9f888a7e3cd1

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
client.run('')                          #token from discord web

secret_key="MTI5OTc1MDY3OTM3NTY0MjY1NA.GWaWSs.uX-1-l4wSc5HSqSzyPrc_CcDTVpWCtaSD7lcuE";