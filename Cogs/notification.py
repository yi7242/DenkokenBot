from discord.ext import commands, tasks
import datetime
import locale
import discord

guild = [565176794215481345]


class NotificationCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.zatsudan = self.bot.get_channel(565180051897974784)
        self.botchannel = self.bot.get_channel(568788772444176394)
        self.member = self.bot.get_guild(565176794215481345).get_role(565440592067166208)
        self.timecheck.start()

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong!')

    @commands.command()
    async def stop(self, ctx):
        await self.bot.close()

    @commands.command()
    async def time(self, ctx):
        await ctx.send(datetime.datetime.now())

    @commands.command()
    async def youbi(self, ctx):
        d = datetime.datetime.now()
        await ctx.send(d.strftime("%A"))
        await ctx.send(d.weekday())
        if d.weekday() == 0:
            await ctx.send("今日は会議の日である")
        else:
            await ctx.send("今日は会議の日ではない")


    @tasks.loop(minutes=1)
    async def timecheck(self):
        now = datetime.datetime.now()
        if now.weekday() == 0 and now.hour == 17 and now.minute == 58:
            await self.zatsudan.send(self.member.mention + "会議の時間だよ")


def setup(bot):
    bot.add_cog(NotificationCog(bot))
