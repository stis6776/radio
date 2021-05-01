import discord
import time
import openpyxl
from captcha.image import ImageCaptcha
import captcha
import random
import asyncio

client = discord.Client()
role_id = 835647291628322837
come_id = 835474138881327134
exit_id = 835474138881327134
gun_id = 835474138881327134
teauk = 835714663102546030
inj = 835647291628322837
notice_id = 831683438603010129

@client.event
async def on_member_join(member):
    embed = discord.Embed(description=f'{member.mention}님 {message.guild.name}에 오신걸 환영합니다!', colour=0x2F3136)
    embed.set_footer(text=dev)
    await client.get_channel(come_id).send(embed=embed)
    await message.mamber.send(embed=embed)

@client.event
async def on_member_remove(member):
    embed = discord.Embed(description=f'{member.mention}님 {message.guild.name}에 다시 오실때까지 기다릴게요!', colour=0x2F3136)
    embed.set_footer(text=dev)
    await client.get_channel(exit_id).send(embed=embed)
    await message.member.send(embed=embed)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name=f"{len(client.users)} 분들과 FM 봉준 라디오", url='https://www.twitch.tv/bongradio'))
    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='FM 봉준 라디오'))
    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='FM 봉준 라디오'))
    
    print('봇에 연결되었습니다: {}'.format(client.user.name))
    print('봇 아이디: {}'.format(client.user.id))

@client.event
async def on_message(message):
    if message.content.startswith("!유저인증"):
        if message.author.guild_permissions.ban_members:
            target = message.mentions[0]
            embed=discord.Embed(title='인증되었습니다', description=f'{target.mention} 님이 {message.guild.name} 서버 에서 인증되었습니다')
            await message.channel.send(embed=embed)
            await message.mentions[0].send(embed=embed)
            role = discord.utils.get(message.guild.roles, id=role_id)
            await message.mentions[0].add_roles(role)

    if message.content.startswith("!권한지급"):
        if message.author.guild_permissions.ban_members:
            target = message.mentions[0]
            embed=discord.Embed(title='권한추가', description=f'{target.mention} 님에게 권한이 추가되었습니다')
            embed1=discord.Embed(title='확인하십시오', description=f'{target.mention} 님에게 주신 권한이 제대로 된 권한인지 한번더 확인해주십시오')
            await message.author.send(embed=embed1)
            await message.channel.send(embed=embed)
            await message.mentions[0].send(embed=embed)
            role = message.role_mentions[0]
            await message.mentions[0].add_roles(role)

    if message.content.startswith("!도움말"):
        await message.channel.send(f'{message.author.mention} 님 디엠을 확인해주세요')
        embed=discord.Embed(title='봇 도움말', description='봇을 많이 사용 해주세요')
        embed.add_field(name='사연 보내기', value='<#836241957435998239> 방에서 !사연 <할말> 로 사연을 보내보세요!')
        embed.add_field(name='건의사항 전송하기', value='봇의 DM 채널에서 !건의 <건의사항> 으로 건의사항을 보내주세요!')
        EMBED.set_footer(text='<@837876715983994901><<각종 문의')
        await message.author.send(embed=embed)

    if message.content.startswith('!전송'):
        await message.delete()
        if message.author.guild_permissions.manage_messages:
            msg = message.content[26:]
            await message.mentions[0].send(embed=discord.Embed(title=f"**{message.author.name}** 님이 전송하신 메시지: {msg}", colour=discord.Colour.blurple()))
            await message.channel.send(embed=discord.Embed(title=f'`{message.mentions[0]}`에게 DM을 보냈습니다', colour=discord.Colour.blue()))
            
        else:
            await message.channel.send(f'{member.mention}')
            message = await message.channel.send(embed=discord.Embed(title='⚠️ `명령어 사용권한이 없습니다` ⚠️', colour=discord.Colour.red()))
            return

    if message.content.startswith("!건의"):
        if message.channel.type is discord.ChannelType.private:
            await message.channel.send("제대로 건의가 전송되었습니다")
            ss = message.content[4:]
            embed1=discord.Embed(title='사연이 전송됨', description='관리자님 내용을 검토해주세요')
            embed1.add_field(name='전송자', value=f'{message.author.mention}')
            embed1.add_field(name='전송된 건의사항 : ', value=ss, inline=False)
            embed1.add_field(name=f'전송자 아이디 : {message.author.id}', value='내용이 부적절할시 이에따른 처벌을 내려주세요')
            embed1.set_footer(text='!전송 <@아이디> 로 답변 부탁드릴게요!')
            await client.get_channel(836031569230561321).send(embed=embed1)
        else:
            await message.channel.send("건의사항은 DM으로 부탁드릴게요")

    if message.content.startswith('!폭파') or message.content.startswith('!채널삭제'):
        try:
            if message.author.guild_permissions.ban_members:
                await message.channel.delete()
            else:
                await message.channel.send(f'{message.author.mention}')
                await message.delete()
                message = await message.channel.send(embed=discord.Embed(title='⚠️ `명령어 사용권한이 없습니다` ⚠️', colour=discord.Colour.red()))
        except:
            pass

    if message.content == ("!인증"):
        await message.channel.send("디엠을 확인해주세요")
        Image_captcha = ImageCaptcha()
        msg = ""
        a = ""
        for i in range(6):
            a += str(random.randint(0, 9))

        name = str(message.author.id) + ".png"
        Image_captcha.write(a, name)

        embed=discord.Embed(title='위 사진에 보이는 숫자를 작성하셔야 인증이 완료됩니다.', colour=0x2F3136)
        embed.set_footer(text='제한시간 10초')
        await message.author.send(embed=embed, file=discord.File(name))
        def check(msg):
            return msg.author == message.author and message.channel == message.channel

        try:
            msg = await client.wait_for("message", timeout=10, check=check)
        except:
            await message.author.send(embed=discord.Embed(title='시간이 초과되었습니다', colour=0x2F3136))
            return

        if msg.content == a:
            await message.author.send(embed=discord.Embed(title='인증되었습니다', ccolour=0x2F3136))
            role = discord.utils.get(message.guild.roles, id=inj)
            await message.author.add_roles(role)
        else:
            await message.author.send(embed=discord.Embed(title='재시도 해주세요', colour=0x2F3136))

    if message.content.startswith('!밴'):
        if message.author.guild_permissions.ban_members:
            try:
                target = message.mentions[0]
            except:
                await message.channel.send('유저가 지정되지 않았습니다')
                return
            
            j = message.content.split(" ")
            try:
                reason = j[2]
            except IndexError:
                reason = 'None'

            

            embed = discord.Embed(title='차단', description=f'🚫**{message.guild.name}**에서 차단되었습니다.\n사유: {reason}🚫', colour=0x2F3136)
            try:
                await target.send(embed=embed)
            except:
                pass
            await target.ban(reason=reason)

            embed = discord.Embed(title='✅  차단 성공', description=f'🚫**{target}**이 차단되었습니다.\n사유: {reason}🚫', colour=0x2F3136)
            await client.get_channel(835474138881327134).send(embed=embed)
        else:
            embed = discord.Embed(description=f'{message.author.mention}님 ⚠️ 명령어 사용권한이 없습니다 관리자만 사용이 가능합니다 ⚠️', colour=0x2F3136)
            await message.channel.send(embed=embed)

    if message.content.startswith('!킥'):
        if message.author.guild_permissions.ban_members:
            await message.delete()
            try:
                target = message.mentions[0]
            except:
                await message.channel.send('유저가 지정되지 않았습니다')
                return
            
            j = message.content.split(" ")
            try:
                reason = j[2]
            except IndexError:
                reason = 'None'

            

            embed = discord.Embed(title='추방', description=f'🚫**{message.guild.name}**에서 추방되었습니다.\n사유: {reason}🚫', colour=0x2F3136)
            try:
                await target.send(embed=embed)
            except:
                pass
            await target.kick(reason=reason)

            embed = discord.Embed(title='✅  추방 성공', description=f'🚫**{target}**이 추방되었습니다.\n사유: {reason}🚫', colour=0x2F3136)
            await client.get_channel(835474138881327134).send(embed=embed)
        else:
            embed = discord.Embed(description=f'{message.author.mention}님 ⚠️ 명령어 사용권한이 없습니다 관리자만 사용이 가능합니다 ⚠️', colour=0x2F3136)
            await message.channel.send(embed=embed)

    if message.content.startswith('!청소'):
        try:
            
            if message.author.guild_permissions.manage_messages:
                amount = message.content[4:]
                await message.delete()
                await message.channel.purge(limit=int(amount))
                embed = discord.Embed(description='🧹 메시지 ' + str(amount) + '개가 삭제되었습니다! 쓰레기 청소 전문은 고냥이~!', colour=0x2F3136)
                embed.set_footer(text=dev)
                await message.channel.send(embed=embed)
                await asyncio.sleep(2)
                await message.delete()
            else:
                embed = discord.Embed(description=f'{message.author.mention}님 ⚠️ 명령어 사용권한이 없습니다 관리자만 사용이 가능합니다 ⚠️', colour=0x2F3136)
                await message.channel.send(embed=embed)
        except:
            pass

    if message.channel.id == 836241957435998239:
        if message.author.bot:
            return
        await message.delete()
        embed2=discord.Embed(title='다음 아래중 골라주세요', description='선택해주세요')
        embed2.add_field(name='비공개 익명 전송', value='1️⃣ 를 선택해주세요')
        embed2.add_field(name='공개 전송', value='2️⃣ 를 선택해주세요')
        embed2.add_field(name='공개 전송', value='3️⃣ 를 선택해주세요')
        msg = await message.channel.send(embed=embed2)
        ss = message.content[4:]

        embed = discord.Embed(colour=discord.Colour.blue(), timestamp=message.created_at)
        embed.add_field(name='전송자', value='익명으로 전송된 사연 입니다', inline=False)
        embed.add_field(name='사연 메시지', value=ss, inline=False)
        embed.set_footer(text='봇에게 사연을 보내 저희 서버를 높이 올라가도록 해주세요!')

        embed1=discord.Embed(title='사연이 전송됨', description='관리자님 내용을 검토해주세요')
        embed1.add_field(name='전송자', value=f'{message.author.mention}')
        embed1.add_field(name='전송된 사연 메시지', value=ss, inline=False)
        embed1.set_footer(text=f'전송자 아이디 : {message.author.id} / 내용이 부적절할시 이에따른 처벌을 내려주세요')

        embed3 = discord.Embed(colour=discord.Colour.blue(), timestamp=message.created_at)
        embed3.add_field(name='전송자', value=f'{message.author.mention} 님께서 전송하신 사연입니다', inline=False)
        embed3.add_field(name='사연 메시지', value=ss, inline=False)
        embed3.set_footer(text='봇에게 사연을 보내 저희 서버를 높이 올라가도록 해주세요!')
        await msg.add_reaction("1️⃣")
        await msg.add_reaction("2️⃣")
        await msg.add_reaction("3️⃣")

        while True:
            def check(reaction, user):
                return str(reaction.emoji) in ['1️⃣' , '2️⃣' , '3️⃣'] and user == message.author

            try:
                reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)

            except asyncio.TimeoutError:
                await client.get_channel(837879770644480030).send(f"{message.guild.name} 에서 시간이 초과됨")

            if (str(reaction.emoji) == '1️⃣'):
                await msg.delete()
                await client.get_channel(836242030954414150).send(embed=embed)
                await client.get_channel(836242313733996596).send(embed=embed1)
                await message.author.send("공개로 메시지가 전송되었습니다")
                break
            
            elif (str(reaction.emoji) == '2️⃣'):
                await msg.delete()
                await client.get_channel(836242030954414150).send(embed=embed3)
                await message.author.send("익명으로 메시지가 전송되었습니다")
                break

            elif (str(reaction.emoji) == '3️⃣'):
                await message.author.send("성공적으로 취소되었습니다")
                await msg.delete()

    if message.content.startswith('!공지'):
        try:
            if message.author.guild_permissions.manage_messages:
                msg = message.content[4:]
                await message.delete()
                message = await message.channel.send(embed=discord.Embed(title='✔️ `공지가 제대로 등록되었습니다` ✔️', colour=discord.Colour.blue())) 
                embed = discord.Embed(colour=discord.Colour.blue(), timestamp=message.created_at)
                embed.add_field(name="공지사항 안내 ", value=msg , inline=False)
                embed.set_footer(text=message.author.name)
                await client.get_channel(notice_id).send('@everyone', embed=embed)
            else:
                await message.channel.send(f'{message.author.mention}')
                await message.delete()
                message = await message.channel.send(embed=discord.Embed(title='⚠️ `명령어 사용권한이 없습니다` ⚠️', colour=discord.Colour.red())) 
        except:
            pass


client.run('ODM3ODc4MTAxNTY4MTI2OTg2.YIy8yg.9GrIHBdGuelKKjrvIiWuw0mXD8Q')
