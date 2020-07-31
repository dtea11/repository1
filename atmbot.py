import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("출금준비")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("!출금신청"):
        await message.channel.send("출금신청이 완료되었습니다.")
    if message.content.startswith("!초기화"):
        await message.channel.send("초기화 완료되었습니다.")
    if message.content.startswith("!출금내역확인"):
        await message.channel.send("내역전송완료.")
    if message.content.startswith("!은행원ㅎㅇ"):
        await message.channel.send("이용해주셔서 감사합니다.")

client.run("NzM3NTMwMTI2NDQ2NjI0ODg5.Xx-sdA.i7O56FjTUrKIg7GRYAGvlqcyXc8")