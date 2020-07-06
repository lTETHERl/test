import discord
from discord.ext import commands
from discord.utils import get
import random

bot = commands.Bot(command_prefix='-')

predictions = [
"если вы проявите инициативу, успех не заставит себя ждать.",
"твои надежды и планы сбудутся сверх всяких ожиданий.",
"сегодня ты будешь попадать каждым хуком!",
"тебе пора отдохнуть.",
"тебе предлагается мечта всей жизни. Скажите да!",
"сегодня ты выиграешь мид!",
"тебя ждет приятный сюрприз.",
"время – ваш союзник, лучше отложить принятие важного решения хотя бы на день.",
"сегодня ты сделаешь rampage!",
"готовься к романтическим приключениям."
]

answer_ball = [
"Давно пора!",
"Не сегодня.",
"Не-е-ет!",
"Не-а!",
"Время нарезать!",
"А вот и нет.",
"Будет сделано.",
"А то!",
]

@bot.command()
async def flip(ctx):
	f = random.randint(1, 2)
	if f == 1:
		emb = discord.Embed(title = "Решка!", colour = discord.Color.from_rgb(48, 255, 165))
		emb.set_image(url = "https://castlots.org/img/ru_reshka.png" )
		await ctx.send(embed = emb)
	elif f == 2:
		emb = discord.Embed(title = "Орёл!", colour = discord.Color.from_rgb(48, 255, 165))
		emb.set_image(url = "https://castlots.org/img/ru_orel.png" )
		await ctx.send(embed = emb)

@bot.command()
async def ball(ctx, text = None):
	if text == None:
		await ctx.send("Напишите какое либо действие")
	else:

		b = random.randint(0, 7)
		emb = discord.Embed( title = answer_ball[b], colour = discord.Color.from_rgb(48, 255, 165))
		await ctx.send(embed = emb)

@bot.command()
async def prediction(ctx):
	p = random.randint(0, 9)
	emb = discord.Embed( title = f"{ctx.author}, " +  predictions[p], colour = discord.Color.from_rgb(48, 255, 165))
	await ctx.send(embed = emb)

@bot.command()
async def pudge(ctx):
	await ctx.send(
	"Свежее мясо! Вот команды которые есть: \n"
	"1. -roll 1число 2число(выводит рандомное число из этих двух) \n"
	"2. -duel @пользователь(вызывает на дуэль пользователя) \n"
	"3. -prediction(вызывает случайное предсказание) \n"
	"4. -ball действие(показывает делать это действие или нет) \n"
	"5. -flip(выпадает орёл или решка) \n"
	"6. -pudge(показывает данный список) "
	)

@bot.command()
async def duel( ctx, member: discord.Member = None):
    if member is None:
        await ctx.send('Укажи кого хочешь позвать на дуель!')
    else:
        a = random.randint(1,2)
        if a == 1:
            emb = discord.Embed( title = f"Победитель - {ctx.author}", colour = discord.Color.blue())
            await ctx.send( embed = emb )

            emb = discord.Embed( title = f"Проигравший - {member}", colour = discord.Color.red())
            await ctx.send( embed = emb )
        else:
            emb = discord.Embed( title = f"Победитель - {member}", colour = discord.Color.blue())
            await ctx.send( embed = emb )

            emb = discord.Embed( title = f"Проигравший - {ctx.author}", colour = discord.Color.red())
            await ctx.send( embed = emb )

@bot.command()
async def roll(ctx, arg1 = None, arg2 = None):
	if arg1 == None and arg2 == None:
		otvet = random.randint(1, 100)
	elif arg1 != None and arg2 == None:
		arg1 = int(arg1)
		otvet = random.randint(1, arg1)
	elif arg1 == None and arg2 != None:
		arg2 = int(arg2)
		otvet = random.randint(1, arg2)
	else:
		arg1 = int(arg1)
		arg2 = int(arg2)
		otvet = random.randint(arg1, arg2)
	await ctx.send(str(otvet))


bot.run('NzI5NDYxOTM1OTk2Nzk3MDI5.XwJSrw.vdgFAcFTUjE5Guo-6VdnWtFKL48')