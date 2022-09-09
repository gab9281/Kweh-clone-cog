from typing import Literal

import discord
from redbot.core import commands
from redbot.core.bot import Red
from redbot.core.config import Config

RequestType = Literal["discord_deleted_user", "owner", "user", "user_strict"]


class Kweh(commands.Cog):
    """
    A short description of the cog.
    """

    def __init__(self, bot: Red) -> None:
        self.bot = bot
        self.config = Config.get_conf(
            self,
            identifier=152870986323066880,
            force_registration=True,
        )


    async def red_delete_data_for_user(self, *, requester: RequestType, user_id: int) -> None:
        # TODO: Replace this with the proper end user data removal handling.
        super().red_delete_data_for_user(requester=requester, user_id=user_id)


    # Entrypoint
    @commands.group()
    async def ffxiv(self, ctx: commands.Context):
        """Entrypoint to use ffxiv related commands."""
        pass

    @ffxiv.command(name="kweh")
    async def ffxiv_kweh(self, ctx):
        """Kweh"""
        await ctx.send("Kweh !")

    # User
    @ffxiv.group(name="user")
    async def user(self, ctx: commands.Context):
        """User informations"""
        pass

    @user.command(name="kweh")
    async def user_kweh(self, ctx):
        """Kweh"""
        await ctx.send("Kweh! Dear user! Kweh!")