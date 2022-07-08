from discord.ext import commands
import traceback
from key import token
INITIAL_EXTENSIONS = [
    'Cogs.notification'
]


class MyBot(commands.Bot):

    def __init__(self, command_prefix):

        super().__init__(command_prefix)

        for cog in INITIAL_EXTENSIONS:
            try:
                self.load_extension(cog)
            except Exception:
                traceback.print_exc()

    async def on_ready(self):
        print('-----')
        print("Logged in as",self.user.name)
        print(self.user.id)
        print('-----')


if __name__ == '__main__':
    bot = MyBot(command_prefix='d!')
    bot.run(token)
