#emitswoh
from discord.ext import commands, tasks
import discord
import string
import sys
import asyncio
import random
import os
import requests
statuses = ['I am *noob*', 'chicken nuggets']

random_messages = ['Why you bully me?', 'Talk RIGHT NOW', 'Who likes Donald Trump here??', "How many chickens would it take to kill an elephant?", "mrbeast", "DM @Ilikeducks", "i AM COOL"]

@tasks.loop(minutes=4.6)
async def test(channel):
    n_random_messages = random.choice(random_messages)
    await channel.send(n_random_messages)



#put your bot-commands channel id here. And a extra channel for noob drops!
comch =  912808735662035035
dropch = 912808837080313856


bot = commands.Bot(command_prefix="!")


noob_emo = '<:noob:908513174972674068>'
aemo = noob_emo
emo = noob_emo
@bot.event
async def on_ready():
    print(f"{bot.user} is ready! Go emitswohs!!")
    channel = bot.get_channel(914190092812320808)
    test.start(channel=channel)
    



bot.load_extension("ping_gateway")

bot.load_extension("snipe")

bot.load_extension("general_help")

bot.load_extension("info_help")

#scripts
noob_script = ["Am I noob?", "Am I pogs?", "Can you be my friend", noob_emo+'Am I cutes?', "Can you give me 1 million dollars??"]

answer_yes = ["pog", "yay", "_noob_", ":smiley:", "you nice nice nice"]

answer_no = ["I am _noob_", "e", ":rage:","*yu mean*"]

answer_hello = ["hi", "hello", "e", ":wave:", ":)"]


@bot.command()
async def noobquestion(ctx):
    r_noob_script = random.choice(noob_script)
    await ctx.channel.send(r_noob_script)

    try:
        message = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=30.0)

    except asyncio.TimeoutError:
        await ctx.channel.send("Ouch you igorned me.")

    else:
        r_noob_yes = random.choice(answer_yes)

        r_noob_no = random.choice(answer_no)
        if message.content.lower() == "yes":
            await ctx.channel.send(r_noob_yes)

        elif message.content.lower() == "no":
            await ctx.channel.send(r_noob_no)

        

@bot.command()
async def rules(ctx: commands.Context):
        info_embed = discord.Embed(title="Ilikeducks's Official Server Rules", description="**Rules Below MUST READ**", colour=0x87CEEB, timestamp=datetime.utcnow())
        embed.set_author(name="Ducky", icon_url="https://cdn.discordapp.com/emojis/720361366900310047.png?size=128")
        await ctx.send(embed=info_embed)




@bot.command()
async def profile_info(ctx, member:discord.Member):
            embed = discord.Embed()
             

            embed.set_image(url=member.avatar_url)

            embed.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.avatar_url)

            await ctx.send(embed=embed)

        
@bot.event
async def on_message(message:discord.Message):
    await bot.process_commands(message)
    if message.content.startswith("hello"):
        random_message = random.randint(1,100)
        if random_message <= 76:
           r_noob_hello = random.choice(answer_hello)
           await message.channel.send(r_noob_hello)
        else:
            return       
    if message.content.startswith("emitswoh"):
        random_message = random.randint(1,100)
        if random_message <= 76:
           
           await message.channel.send("What do you want.")
        else:
            return       



def nitrounchecked(type):
	if type == "nitro classic":
		length = 16
	elif type == "nitro":
		length = 24
	code = list(string.ascii_letters + string.digits)
	random.shuffle(code)
	code = random.choices(code, k=length)
	random.shuffle(code)
	code = "".join(code)
	return code


@bot.event
async def on_message(message):

	if message.content.startswith("!nitro_help"):
		he = discord.Embed(title="Help", color=0xf47fff)
		he.add_field(name="!g (nitro/nitro classic)",
		             value="Generate 1 unchecked nitro/nitro classic code")
		he.add_field(name="!gc (nitro/nitro classic)",
		             value="Generate and check 1 nitro/nitro classic code")
		he.add_field(name="!c (nitro code/nitro classic code)",
		             value="Check a nitro/nitro classic code")
		he.add_field(name="More commands soon",
		             value="Specials commands for VIP!!")
		he.add_field(name="!h", value="Help")

		await message.channel.send(embed=he)

	
	if (message.content.startswith("!untilTrue")):
		ntype = message.content[4:]
		ntype.strip()
		ntype = ntype.lower()
		await message.channel.send("Searching for: " + ntype.split(" ")[1])
		if ntype == "nitro" or ntype == "nitro classic":
			code = nitrounchecked(ntype)

			url = "https://discordapp.com/api/v8/entitlements/gift-codes/" + code
			response = requests.get(url)

			while response.status_code != 200:
				code = nitrounchecked(ntype)

				url = "https://discordapp.com/api/v8/entitlements/gift-codes/" + code
				response = requests.get(url)
			x = "Valid"
			channel = bot.get_channel(dropch)
			await channel.send("https://discord.gift/" + code)

			if len(code) == 16:
				t = "Nitro Classic"
			elif len(code) == 24:
				t = "Nitro"

			emb = discord.Embed(title=aemo + " Discord Nitro " + aemo,
			                    color=0xf47fff)

			emb.add_field(name="Code", value=code, inline=False)
			emb.add_field(name="Type", value=t, inline=True)
			emb.add_field(name="Status", value=x, inline=True)

			await message.channel.send(message.author.mention +
			                           " Check your DMs for " + ntype + "!")
			await message.author.send(embed=emb)
			await message.author.send("https://discord.gift/" + code)
	if message.content.startswith("!g") and message.channel.id == comch:
		ntype = message.content[3:]
		ntype.strip()
		ntype = ntype.lower()
		if ntype == "nitro" or ntype == "nitro classic":
			code = nitrounchecked(ntype)
			await message.author.send("https://discord.gift/" + code)
			await message.channel.send(message.author.mention +
			                           " Check your DMs for " + ntype + "!")

	if message.content.startswith("!c") and message.channel.id == comch:
		code = message.content[3:]
		code.strip()
		if len(code) == 16 or len(code) == 24:

			url = "https://discordapp.com/api/v8/entitlements/gift-codes/" + code
			response = requests.get(url)

			if response.status_code == 200:
				x = "Valid"
				channel = bot.get_channel(dropch)
				await channel.send("https://discord.gift/" + code)

			elif response.status_code == 429:
				x = "Ratelimited"
			elif response.status_code == 404:
				x = "Expired"
			else:
				x = "Invalid"

			if len(code) == 16:
				t = "Nitro Classic"
			elif len(code) == 24:
				t = "Nitro"
			else:
				t = "Invalid"

			emb1 = discord.Embed(title=emo + " Discord Nitro " + emo,
			                     color=0xf47fff)

			emb1.add_field(name="Code", value=code, inline=False)
			emb1.add_field(name="Type", value=t, inline=True)
			emb1.add_field(name="Status", value=x, inline=True)

			await message.channel.send(embed=emb1)

	if message.content.startswith("!gc") and message.channel.id == comch:

		ntype = message.content[4:]
		ntype.strip()
		ntype = ntype.lower()
		if ntype == "nitro" or ntype == "nitro classic":
			code = nitrounchecked(ntype)

			url = "https://discordapp.com/api/v8/entitlements/gift-codes/" + code
			response = requests.get(url)

			if response.status_code == 200:
				x = "Valid"
				channel = bot.get_channel(dropch)
				await channel.send("https://discord.gift/" + code)

			elif response.status_code == 429:
				x = "Ratelimited"
			elif response.status_code == 404:
				x = "Expired"
			else:
				x = "Invalid"

			if len(code) == 16:
				t = "Nitro Classic"
			elif len(code) == 24:
				t = "Nitro"

			emb = discord.Embed(title=aemo + " Discord Nitro " + aemo,
			                    color=0xf47fff)

			emb.add_field(name="Code", value=code, inline=False)
			emb.add_field(name="Type", value=t, inline=True)
			emb.add_field(name="Status", value=x, inline=True)

			await message.channel.send(message.author.mention +
			                           " Check your DMs for " + ntype + "!")
			await message.author.send(embed=emb)
			await message.author.send("https://discord.gift/" + code)

my_secret = os.environ['TOKEN']
bot.run(my_secret)