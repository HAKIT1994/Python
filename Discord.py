#導入 Discord.py
import discord
#client 是我們與 Discord 連結的橋樑
from discord.ext.commands import bot

client = discord.Client()

#調用 event 函式庫
@client.event
#當機器人完成啟動時
async def on_ready():
    print('目前登入身份：', client.user)
    game = discord.Game('努力學習py中')
    # discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await client.change_presence(status=discord.Status.invisible, activity=game)

@client.event
#當有訊息時
async def on_message(message):
    #排除自己的訊息，避免陷入無限循環
    if message.author == client.user:
        return
    #如果包含 ping，機器人回傳 pong
    if message.content == 'hello':
        msg = await message.channel.send('pong')
        await msg.delete()

    if message.content == 'Password':
        import random
        import string

        def gen(word, num, mark):
            word = ''.join(random.choice(string.ascii_letters) for i in range(word))
            num = ''.join(random.choice(string.digits) for i in range(num))
            mark = ''.join(random.choice(string.punctuation) for i in range(mark))

            samplelist = list(word + num + mark)
            random.shuffle(samplelist)
            return ''.join(samplelist)

        await message.channel.send(gen(6,2,3))





client.run('ODY3MzI1Njk1OTE4NjA0MzA4.YPfeAA.8H4kLLAniNaOlqwxkOn7bCoCo64') #TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面
