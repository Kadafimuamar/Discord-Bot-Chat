import os
import asyncio
import discord

os.system('pip install -U discord==1.7.3')
os.system('pip install -U discord.py==1.7.3')

token = "NDMwNTA1OTg5NTk5NTI2OTMx.GfkKv2.wSWto4VPdZISHuUP4p9GmjzRrYLf6BScos4Oos" #TokenIdYour
replyMessage = 'Have A good Day Mate, wait for next announce of Mind Network'
channelId = 1052489674914025522 #channeild
delay = 15

mainMessages = [
    'What is going on?',
    'In November 2022, Mind Network was selected for Binance Incubation Camp Season 5 as the only data project',
    'Mind Network is a Decentralized Zero Trust Data Lake that secures all your data, smart contracts and AI on Web3',
    'It is built on a patented zero trust framework based on Zero Knowledge Proof (ZKP) and Adaptive Fully Homomorphic Encryption (AFHE)',
    'Mind Network seals your data into encrypted data ledgers to make your data truly yours',
    'In addition, Mind Network empowers developers with data intelligence without trade-offs in privacy',
    'Mind Network offers several unique features and capabilities',
    'Full Encryption: Built on patented Adaptive Full Homomorphic Encryption (FHE) framework to empower encrypted computation on encrypted data',
    'Trusted Computation: A tamper-proof computation engine that supports encrypted computation from data query to machine learning',
    'gw mau menyerah aja deh',
    'High-Performance: Scalable to petabyte of data and support high-performance encrypted computation',
    'Mind Network joined Chainlink BUILD to maximize the security and reliability benefits that the Chainlink Oracle infrastructure provides',
]

class Main(discord.Client):
    async def on_ready(self):
        print('Logged in as %s.' % self.user)
        while True:
            channel = self.get_channel(channelId)
            for i, msg in enumerate(mainMessages):
                sent_message = await channel.send(msg)
                print(f'Sent message {i+1} in #{channel.name}.')
                await asyncio.sleep(delay)
                await sent_message.delete()  # Delete the sent message

    async def on_message(self, message):
        if isinstance(message.channel, discord.DMChannel):
            if message.author.id != self.user.id:
                with open('blacklist.txt', 'r', encoding='UTF-8') as file:
                    if str(message.author.id) not in file.read():
                        sent_message = await message.reply(replyMessage)
                        print('Replied to %s.' % message.author.name)
                        await asyncio.sleep(delay)
                        await sent_message.delete()  # Delete the sent message
                        with open('blacklist.txt', 'a', encoding='UTF-8') as file:
                            file.write('%s\n' % message.author.id)

if __name__ == '__main__':
    Main().run(token, bot=False)
