import discord, random, asyncio, time, os, json, datetime
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix='.', help_command=None)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Getting Bigger',type=3))
    print('I want to put a mouse in my ass')

@client.command()
async def help(context):
    hpage = discord.Embed(title="**__HELP__**", description="Use `.help <command>` for more info on a command.\nUse `.help <category>` for more info on a category.\n\n**ADMIN ONLY**\n`clear` `kick` `ban` `unban`\n\n**POLLA**\n`piedra_papel_tijera` `text_format_options` `spam` `gameadd` `hearadd` `seeadd`\n\n**OMEEB**\n`_8ball` `token` `ping` `check`\n\n**CHEWICOBOT**\n`gaysay` `check`", colour=discord.Colour.purple())
    text = await context.send(embed=hpage)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ADMIN ONLY~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#####################ELIMINATE A NUMBER OF MESSAGES#####################
@client.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount: int):
    await ctx.message.add_reaction(u"\u2705")
    await ctx.channel.purge(limit=(amount+1))
    if amount == int('1'):
        message = await ctx.send(f'```{amount} messatge has been deleted```')
    else:
        message = await ctx.send(f'````{amount} messatges have been deleted```')
    time.sleep(5)
    await message.delete()
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please specify an amaunt of messatges to delete")
########################################################################

############################TO KICK A MEMBER############################
@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason):
    await ctx.message.add_reaction(u"\u2705")
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member} for {reason}')
########################################################################

############################TO BAN  A MEMBER############################
@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason):
    await ctx.message.add_reaction(u"\u2705")
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member} for {reason}')
########################################################################

#############################UNBAN A MEMBER#############################
@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    await ctx.message.add_reaction(u"\u2705")
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.name}#{user.discriminator} Was unbanned')
            return
########################################################################

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~POLLA~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

###########################PIEDRA PAPEL TIJERA##########################
@client.command(aliases=['ppt'])
async def piedra_papel_tijera(wlh):
    page_wlh = discord.Embed(title="PIEDRA PAPEL TIJERA",description="Chose one reaction",colour=discord.Colour.purple())
    message = await wlh.send(embed=page_wlh)
    first_run = True
    while True:
        if first_run:
            first_run = False
            reactmoji = ["✌️", "✋", "✊"]
            random_choice = ["✌️", "✋", "✊"][random.randint(0,2)]
            print(random_choice)
            for react in reactmoji:
                await message.add_reaction(react)

        def check_react(reaction, user):
            if reaction.message.id != message.id:
                return False
            if user != wlh.message.author:
                return False
            if str(reaction.emoji) not in reactmoji:
                return False
            return True

        try:
            res, user = await client.wait_for('reaction_add', check=check_react)
        except asyncio.TimeoutError:
            return await message.clear_reactions()


        if random_choice == "✋":
            if user != wlh.message.author:
                pass
            elif "✋" in str(res.emoji):
                empat1_wlh = discord.Embed(title='TIE', description='Sorry, we have tied. Try luck next time.',colour=discord.Colour.orange())
                empat1_wlh.set_image(url="https://images-ext-2.discordapp.net/external/HPvVY1ymPUj9FdDUoNkbG7vKQdfnTrvl9Nc_TxFYoZY/https/i.redd.it/gy053gdfdzf21.jpg")
                await message.clear_reactions()
                await message.edit(embed=empat1_wlh)
            elif "✊" in str(res.emoji):
                lose1_wlh = discord.Embed(title='YOU LOSE', description='Sorry, I win. Try luck next time.',colour=discord.Colour.red())
                lose1_wlh.set_image(url="https://images-ext-1.discordapp.net/external/OBRXUG9_R2L2s94H-8m_5T4iylkcIgIZzjROdEvmZdI/https/i.pinimg.com/originals/75/da/d0/75dad06113b84276fd4fbfd9c024afe7.jpg?width=426&height=585")
                await message.clear_reactions()
                await message.edit(embed=lose1_wlh)
            elif "✌️" in str(res.emoji):
                win1_wlh = discord.Embed(title='YOU WIN', description='You win',colour=discord.Colour.green())
                win1_wlh.set_image(url="https://images-ext-2.discordapp.net/external/FNx63GRVAqZSpAD56rAB0urAaB0dRNrDYg6h4WAOYrQ/https/data.whicdn.com/images/347860021/original.jpg?width=596&height=585")
                await message.clear_reactions()
                await message.edit(embed=win1_wlh)
        elif random_choice == "✊":
            if user != wlh.message.author:
                pass
            elif "✊" in str(res.emoji):
                empat2_wlh = discord.Embed(title='TIE', description='Sorry, we have tied. Try luck next time.',colour=discord.Colour.orange())
                empat2_wlh.set_image(url="https://images-ext-2.discordapp.net/external/HPvVY1ymPUj9FdDUoNkbG7vKQdfnTrvl9Nc_TxFYoZY/https/i.redd.it/gy053gdfdzf21.jpg")
                await message.clear_reactions()
                await message.edit(embed=empat2_wlh)
            elif "✌️" in str(res.emoji):
                lose2_wlh = discord.Embed(title='YOU LOSE', description='Sorry, I win. Try luck next time.',colour=discord.Colour.red())
                lose2_wlh.set_image(url="https://images-ext-1.discordapp.net/external/OBRXUG9_R2L2s94H-8m_5T4iylkcIgIZzjROdEvmZdI/https/i.pinimg.com/originals/75/da/d0/75dad06113b84276fd4fbfd9c024afe7.jpg?width=426&height=585")
                await message.clear_reactions()
                await message.edit(embed=lose2_wlh)
            elif "✋" in str(res.emoji):
                win2_wlh = discord.Embed(title='YOU WIN', description='You win',colour=discord.Colour.green())
                win2_wlh.set_image(url="https://images-ext-2.discordapp.net/external/FNx63GRVAqZSpAD56rAB0urAaB0dRNrDYg6h4WAOYrQ/https/data.whicdn.com/images/347860021/original.jpg?width=596&height=585")
                await message.clear_reactions()
                await message.edit(embed=win2_wlh)
        elif random_choice == "✌️":
            if user != wlh.message.author:
                pass
            elif "✌️" in str(res.emoji):
                empat3_wlh = discord.Embed(title='TIE', description='Sorry, we have tied. Try luck next time.',colour=discord.Colour.orange())
                empat3_wlh.set_image(url="https://images-ext-2.discordapp.net/external/HPvVY1ymPUj9FdDUoNkbG7vKQdfnTrvl9Nc_TxFYoZY/https/i.redd.it/gy053gdfdzf21.jpg")
                await message.clear_reactions()
                await message.edit(embed=empat3_wlh)
            elif "✋" in str(res.emoji):
                lose3_wlh = discord.Embed(title='YOU LOSE', description='Sorry, I win. Try luck next time.',colour=discord.Colour.red())
                lose3_wlh.set_image(url="https://images-ext-1.discordapp.net/external/OBRXUG9_R2L2s94H-8m_5T4iylkcIgIZzjROdEvmZdI/https/i.pinimg.com/originals/75/da/d0/75dad06113b84276fd4fbfd9c024afe7.jpg?width=426&height=585")
                await message.clear_reactions()
                await message.edit(embed=lose3_wlh)
            elif "✊" in str(res.emoji):
                win3_wlh = discord.Embed(title='YOU WIN', description='You win',colour=discord.Colour.green())
                win3_wlh.set_image(url="https://images-ext-2.discordapp.net/external/FNx63GRVAqZSpAD56rAB0urAaB0dRNrDYg6h4WAOYrQ/https/data.whicdn.com/images/347860021/original.jpg?width=596&height=585")
                await message.clear_reactions()
                await message.edit(embed=win3_wlh)
########################################################################

###############################TEXT TRICKS##############################
@client.command(aliases=['tfo','text_tricks'])
async def text_format_options(text_tricks):
    tfo = discord.Embed(title="TEXT FORMATTING", description="Here is some ways to format text\n\n*ITALICS(cursiva)*\nSurround your text in asterisks(*)\n\n**BOLD(negrita)**\nSurround your text in double asterisks(**)\n\n__UNDERLINE(subrallado)__\nSurround your text in double underscores(__)\n\n~~STRIKETHROUGH(tachado)~~\nSurround your text in double tildes(~\~)\n\n`CODE CHUNKS`\nSurround your text in backticks(`) \n\nBLOCKQUOTES\n> Start your text with a greater than symbol(>)\n\nSECRETS(spoiler)\n||Surround your text in double pipes(|\|)||", colour=discord.Colour.purple())
    text = await text_tricks.send(embed=tfo)

########################################################################

####################CHANGE THE SPAM TIME OF DRAREG04####################
@client.command()
async def spam(mcetm):
    page_wlh = discord.Embed(title="SPAM",description="Write the time",colour=discord.Colour.purple())
    text = await mcetm.send(embed=page_wlh)
    def check(msg):
        return msg.author == mcetm.author and msg.channel == mcetm.channel

    msg = await client.wait_for("message", check=check)
    if msg.author.id == 511535555381559311 and int(msg.content) >= 0:
        f = open("time.txt", "w")
        f.write(str(msg.content))
        f.close
        puta = ("The time has change to "+ str(msg.content) + " seconds")
        pag = discord.Embed(title="OK", description=puta, colour=discord.Colour.purple())
        toxt = await mcetm.send(embed=pag)
    else:
        await mcetm.send("https://cdn.memegenerator.es/imagenes/memes/full/2/71/2710193.jpg")
########################################################################

############################CHANGE THE TXTS#############################
@client.command()
async def gameadd(mcetm):
    already=""
    with open ("game.txt") as g:
        for h in g:
            already = already+("- "+str(h))
        g.close
    page_wlh = discord.Embed(title="GAME",description=("**Write the new game:**\n"+str(already)),colour=discord.Colour.purple())
    text = await mcetm.send(embed=page_wlh)
    def check(msg):
        return msg.author == mcetm.author and msg.channel == mcetm.channel

    msg = await client.wait_for("message", check=check)
    if msg.author.id == 511535555381559311:
        f = open("game.txt", "a")
        f.write("\n")
        f.write(str(msg.content))
        f.close
        puta = ("The game "+ str(msg.content) + " has been added to the game.txt")
        pag = discord.Embed(title="OK", description=puta, colour=discord.Colour.purple())
        toxt = await mcetm.send(embed=pag)
    else:
        await mcetm.send("https://cdn.memegenerator.es/imagenes/memes/full/2/71/2710193.jpg")
@client.command()
async def hearadd(mcetm):
    already=""
    with open ("hear.txt") as g:
        for h in g:
            already = already+("- "+str(h))
        g.close
    page_wlh = discord.Embed(title="HEAR",description=("**Write the new stuff:**\n"+str(already)),colour=discord.Colour.purple())
    text = await mcetm.send(embed=page_wlh)
    def check(msg):
        return msg.author == mcetm.author and msg.channel == mcetm.channel

    msg = await client.wait_for("message", check=check)
    if msg.author.id == 511535555381559311:
        f = open("hear.txt", "a")
        f.write("\n")
        f.write(str(msg.content))
        f.close
        puta = (str(msg.content) + " has been added to the hear.txt")
        pag = discord.Embed(title="OK", description=puta, colour=discord.Colour.purple())
        toxt = await mcetm.send(embed=pag)
    else:
        await mcetm.send("https://cdn.memegenerator.es/imagenes/memes/full/2/71/2710193.jpg")
@client.command()
async def seeadd(mcetm):
    already=""
    with open ("see.txt") as g:
        for h in g:
            already = already+("- "+str(h))
        g.close
    page_wlh = discord.Embed(title="SEE",description=("**Write the new stuff:**\n"+str(already)),colour=discord.Colour.purple())
    text = await mcetm.send(embed=page_wlh)
    def check(msg):
        return msg.author == mcetm.author and msg.channel == mcetm.channel

    msg = await client.wait_for("message", check=check)
    if msg.author.id == 511535555381559311:
        f = open("see.txt", "a")
        f.write("\n")
        f.write(str(msg.content))
        f.close
        puta = (str(msg.content) + " has been added to the see.txt")
        pag = discord.Embed(title="OK", description=puta, colour=discord.Colour.purple())
        toxt = await mcetm.send(embed=pag)
    else:
        await mcetm.send("https://cdn.memegenerator.es/imagenes/memes/full/2/71/2710193.jpg")
########################################################################
###############################SPAWN POKEMON############################
@client.command()
async def pspawn(ctx, *,  num):	    
	def read_time():
		with open("time.txt", "r") as f:
			lines = f.readlines()
			return lines[0].strip()
			f.close()
	temps = read_time()
	for n in range(int(num)):
		spam.pspawn()
########################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~OMEEB~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

##############################RESPNDS YOU###############################
# .8ball(QUESTION) TELS YOU AN ANSWER TO YOUR QUESTION
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    await ctx.message.add_reaction(u"\u2705")
    responses = ['It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes – definitely.', 'You may rely on it.', 'As I see it, yes.', 'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.', 'Dont count on it.', 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.', 'No.']
    messages =(f"**QUESTION:** {question}\n**ANSWER:** {random.choice(responses)}")
    eitball = discord.Embed(title="**__8BALL__**",description=messages,colour=discord.Colour.purple())
    eitball.set_author(name="OMEEB",icon_url="https://media.discordapp.net/attachments/889464004613906473/904028920163221514/fda13b9d6d88f25a9d968901d319216a.jpg")
    message = await ctx.send(embed=eitball)
########################################################################

#######################DOSNT TELL YOU THE TOKEN#########################
@client.command()
async def token(ctx):
    await ctx.message.add_reaction(u"\u2705")
    await ctx.send(f"TOKEN:||           I'm not going to tell you that            ||")
########################################################################

############################TELLS YOUR PING#############################
@client.command()
async def ping(ctx):
    await ctx.message.add_reaction(u"\u2705")
    await ctx.send(f'{round(client.latency * 1000)}ms')
########################################################################

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~CHEWICOBOT~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#############################ANONYM MESSAGE#############################
@client.command()
async def gaysay(ctx, *, say):
    messages =("Un gay ha dicho: " + say)
    eitball = discord.Embed(title="**GAY SAY**",description=messages,colour=discord.Colour.purple())
    eitball.set_image(url="https://media.discordapp.net/attachments/895556702190043156/904104565350211605/unknown.png")
    eitball.set_author(name="CHEWICOBOT",icon_url="https://media.discordapp.net/attachments/895556702190043156/904104565350211605/unknown.png")
    message = await ctx.send(embed=eitball)
########################################################################

#######################REACT TO 1000 CHANEL IMAGES#######################
@client.command()
async def check(ctx):
    async for imessage in ctx.history(limit=1000):
        if len(imessage.attachments) > 0:
            await imessage.add_reaction("<:KEKW:889820322323369985>")
            await imessage.add_reaction("<:bruh:897742300971679794>")
            await imessage.add_reaction("<:emoji_upvote_startup:741629294127874109>")
            await imessage.add_reaction("<:emoji_downvote_startup:741630229218328597>")

        elif "https://" in imessage.content:
            await imessage.add_reaction("<:KEKW:889820322323369985>")
            await imessage.add_reaction("<:bruh:897742300971679794>")
            await imessage.add_reaction("<:emoji_upvote_startup:741629294127874109>")
            await imessage.add_reaction("<:emoji_downvote_startup:741630229218328597>")
########################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~EVENT~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#######################REACT TO SPECYFIC MESSAGES#######################
@client.event
async def on_message(message):
    if "bot" in message.content:
        react = await message.channel.send("Me has llamado uwu :point_right::point_left:")
        await message.add_reaction(u"\u2705")

    if message.channel.id == 898488969082310668:
        await message.add_reaction(":pepeyessign:")
        await message.add_reaction(":3113peepohypers:")
        await message.add_reaction(":pepenosign:")
      
    channelss = [741652556194906164, 888366853251031090, 907243446727737354]  # 1st= OMEEB SERVER 2nd= SALESIANS SERVER
    if message.channel.id in channelss:
        if len(message.attachments) > 0:
            await message.add_reaction("<:KEKW:889820322323369985>")
            await message.add_reaction("<:bruh:897742300971679794>")
            await message.add_reaction("<:emoji_upvote_startup:741629294127874109>")
            await message.add_reaction("<:emoji_downvote_startup:741630229218328597>")

        elif "https://www.tiktok.com" in message.content:
            await message.channel.send("https://cdn.discordapp.com/attachments/616222062595538947/755097123451830323/Snapchat-1848621029.jpg")
            await message.add_reaction("<:KEKW:889820322323369985>")
            await message.add_reaction("<:bruh:897742300971679794>")
            await message.add_reaction("<:emoji_upvote_startup:741629294127874109>")
            await message.add_reaction("<:emoji_downvote_startup:741630229218328597>")

        elif "https://" in message.content:
            await message.add_reaction("<:KEKW:889820322323369985>")
            await message.add_reaction("<:bruh:897742300971679794>")
            await message.add_reaction("<:emoji_upvote_startup:741629294127874109>")
            await message.add_reaction("<:emoji_downvote_startup:741630229218328597>")

    await client.process_commands(message)

    if ".gaysay" in message.content:
        await message.delete()
########################################################################
  
client.run(TOKEN)
