import discord
from discord import app_commands
from discord.ext import commands
from daug.utils.dpyexcept import excepter
from daug.utils.dpylog import dpylogger
from utils.ops_log import emit_component_error
from utils.ops_log import emit_modal_error


class SecretPostModal(discord.ui.Modal, title='匿名でメッセージを投稿する'):
    def __init__(self):
        super().__init__()

    name = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label='ペンネーム',
        required=False,
    )

    content = discord.ui.TextInput(
        style=discord.TextStyle.long,
        label='投稿するメッセージ',
        required=True,
    )

    @excepter
    @dpylogger
    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        content = self.content.value
        if self.name.value:
            content = f'【ペンネーム】{self.name.value}\n\n{content}'

        await interaction.channel.send(content)
        try:
            await interaction.message.delete()
            await interaction.channel.send(view=SecretPostButton())
        except discord.errors.NotFound:
            pass

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await emit_modal_error(
            interaction,
            error,
            title='Anonymous post modal failed',
        )


class SecretPostButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    async def on_error(
        self,
        interaction: discord.Interaction,
        error: Exception,
        item: discord.ui.Item,
    ) -> None:
        await emit_component_error(interaction, error, item)

    @excepter
    @dpylogger
    @discord.ui.button(label='匿名でメッセージを投稿する', style=discord.ButtonStyle.blurple, custom_id='secret_post:post')
    async def _send_secret_post(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(SecretPostModal())


class SecretPostCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.bot.add_view(SecretPostButton())

    @app_commands.command(name='匿名投稿ボタン', description='匿名でメッセージを投稿できるボタンを設置します')
    @app_commands.guild_only()
    @excepter
    @dpylogger
    async def _secret_post_button_app_command(self, interaction: discord.Interaction):
        if not interaction.user.resolved_permissions.manage_channels:
            await interaction.response.send_message('このコマンドを実行するにはチャンネル管理権限が必要です', ephemeral=True)
            return
        await interaction.response.send_message('誰でも匿名でメッセージを投稿できるボタンです。\n投稿が行われるとボタンが一番下に再投稿されます。', ephemeral=True)
        await interaction.channel.send(view=SecretPostButton())


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(SecretPostCog(bot))
