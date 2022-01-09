Pycord.Wavelink
===============

.. image:: https://img.shields.io/badge/Python-3.7%20%7C%203.8%20%7C%203.9-blue.svg
    :target: https://www.python.org
    :align: center
.. image:: https://img.shields.io/pypi/v/pycord.wavelink.svg
    :target: https://pypi.org/project/pycord.wavelink/
    :align: center

Wavelink is robust and powerful Lavalink wrapper for `Pycord <https://github.com/Pycord-Development/pycord>`_!
Wavelink features a fully asynchronous API that's intuitive and easy to use.

Support
---------------------------
For support using Pycord.WaveLink, please join the official `support server
<https://discord.gg/pycord>`_ on `Discord <https://discord.com/>`_.

|Discord|

.. |Discord| image:: https://discord.com/api/guilds/881207955029110855/embed.png?style=banner2
   :target: https://discord.gg/pycord

Documentation
---------------------------

The documention can be found `here <https://wavelink-docs.pycord.dev/en/latest/>`_!

Installation
---------------------------
The following commands are currently the valid ways of installing WaveLink.

**WaveLink requires Python 3.8+**

**Windows**

.. code:: sh

    py -3.9 -m pip install pycord.wavelink --pre

**Linux**

.. code:: sh

    python3.9 -m pip install pycord.wavelink --pre

Getting Started
----------------------------

A quick and easy bot example:

.. code:: py
    
    import pycord.wavelink as wavelink
    from discord.ext import commands

    class Bot(commands.Bot):
        def __init__(self):
            super().__init__(command_prefix='>?')

        async def on_ready(self):
            print('Bot is ready!')

    class Music(commands.Cog):
        """Music cog to hold Wavelink related commands and listeners."""
        def __init__(self, bot: commands.Bot):
            self.bot = bot
            bot.loop.create_task(self.connect_nodes())

        async def connect_nodes(self):
            """Connect to our Lavalink nodes."""
            await self.bot.wait_until_ready()
            await wavelink.NodePool.create_node(
                bot=bot,
                host='0.0.0.0',
                port=2333,
                password='YOUR_LAVALINK_PASSWORD',
            )

        @commands.Cog.listener()
        async def on_wavelink_node_ready(self, node: wavelink.Node):
            """Event fired when a node has finished connecting."""
            print(f'Node: <{node.identifier}> is ready!')

        @commands.command()
        async def play(self, ctx: commands.Context, *, search: wavelink.YouTubeTrack):
            """Play a song with the given search query.
            If not connected, connect to our voice channel.
            """
            if not ctx.voice_client:
                vc: wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
            else:
                vc: wavelink.Player = ctx.voice_client
            await vc.play(search)

    bot = Bot()
    bot.add_cog(Music(bot))
    bot.run('YOUR_BOT_TOKEN')
