# imports #

import discord

# vars #
prefix = '!'
status = 0  # 0 - off, 1 - online, 2 - afk, 3 - ocupado #


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        status = 'ONLINE'
        print(f'> Status: {status}')

    async def on_message(self, message):
        print(f'Mensagem de {message.author}: {message.content}')
        if message.content.startswith(prefix) is False and message.author.name != self.user:
            await message.channel.send(f'Você não inseriu o prefixo({prefix}), tente novamente.')
            
        else:
            return
        # comandos #
        '''if message.content == f'{prefix}speak':
            await message.channel.send(message.content[6::])'''
        ##
        if message.content == f'{prefix}status':
            if status == 0:
                status == 'OFFLINE'
            elif status == 1:
                status == 'ONLINE'
            elif status == 2:
                status == 'AUSENTE'
            elif status == 3:
                status == 'OCUPADO'
            await message.channel.send(f':minidisc: | Status: {status}')


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(
    'MTA1NzY4NTQ5NjA0Nzg3NDA5OA.GFQZqc.gbiROuMxqF-D0MDEm_N8wlZO7-BqHeM20KDi7o'
)
