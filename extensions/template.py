import aiohttp
import datetime
import discord
from discord import Webhook
from discord import app_commands
from discord.ext import commands
from daug.utils.dpyexcept import excepter
from daug.utils.dpylog import dpylogger
from daug.constants import COLOUR_EMBED_GRAY
from utils.ops_log import emit_component_error

jst = datetime.timezone(datetime.timedelta(hours=9))


def compose_embed(text: str, user: discord.Member):
    return discord.Embed(
         description=text,
         colour=COLOUR_EMBED_GRAY,
         timestamp=datetime.datetime.now(jst),
     ).set_author(
         name=user.display_name,
         icon_url=user.display_avatar.url
     ).set_thumbnail(
         url=user.display_avatar.url,
     )


class TemplateMessageButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    async def on_error(
        self,
        interaction: discord.Interaction,
        error: Exception,
        item: discord.ui.Item,
    ) -> None:
        await emit_component_error(interaction, error, item)

    @discord.ui.button(label='起床', style=discord.ButtonStyle.green, custom_id='template_message:get_up')
    @excepter
    @dpylogger
    async def _send_message_get_up(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)
        text = 'おはよう'
        try:
            async with aiohttp.ClientSession() as session:
                webhooks = await interaction.channel.webhooks()
                webhook = None
                for _webhook in webhooks:
                    if _webhook.user == interaction.client.user:
                        webhook = _webhook
                        break
                if webhook is None:
                    webhook = await interaction.channel.create_webhook(name='テンプレートメッセージ')
                webhook = Webhook.from_url(webhook.url, session=session)
                await webhook.send(embed=compose_embed(text, interaction.user), username=interaction.user.display_name, avatar_url=interaction.user.display_avatar.url)
            await interaction.message.delete()
            await interaction.channel.send('ボタンを押すとテンプレメッセージが投稿されます', view=TemplateMessageButton())
        except discord.errors.NotFound:
            await interaction.followup.send('エラーが発生しました', ephemeral=True)

    @discord.ui.button(label='就寝', style=discord.ButtonStyle.green, custom_id='template_message:sleep')
    @excepter
    @dpylogger
    async def _send_message_sleep(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)
        text = 'おやすみ'
        try:
            async with aiohttp.ClientSession() as session:
                webhooks = await interaction.channel.webhooks()
                webhook = None
                for _webhook in webhooks:
                    if _webhook.user == interaction.client.user:
                        webhook = _webhook
                        break
                if webhook is None:
                    webhook = await interaction.channel.create_webhook(name='テンプレートメッセージ')
                webhook = Webhook.from_url(webhook.url, session=session)
                await webhook.send(embed=compose_embed(text, interaction.user), username=interaction.user.display_name, avatar_url=interaction.user.display_avatar.url)
            await interaction.message.delete()
            await interaction.channel.send('ボタンを押すとテンプレメッセージが投稿されます', view=TemplateMessageButton())
        except discord.errors.NotFound:
            await interaction.followup.send('エラーが発生しました', ephemeral=True)

    @discord.ui.button(label='外出中', style=discord.ButtonStyle.green, custom_id='template_message:go_out')
    @excepter
    @dpylogger
    async def _send_message_go_out(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)
        text = 'お出かけしてるよ'
        try:
            async with aiohttp.ClientSession() as session:
                webhooks = await interaction.channel.webhooks()
                webhook = None
                for _webhook in webhooks:
                    if _webhook.user == interaction.client.user:
                        webhook = _webhook
                        break
                if webhook is None:
                    webhook = await interaction.channel.create_webhook(name='テンプレートメッセージ')
                webhook = Webhook.from_url(webhook.url, session=session)
                await webhook.send(embed=compose_embed(text, interaction.user), username=interaction.user.display_name, avatar_url=interaction.user.display_avatar.url)
            await interaction.message.delete()
            await interaction.channel.send('ボタンを押すとテンプレメッセージが投稿されます', view=TemplateMessageButton())
        except discord.errors.NotFound:
            await interaction.followup.send('エラーが発生しました', ephemeral=True)

    @discord.ui.button(label='帰宅', style=discord.ButtonStyle.green, custom_id='template_message:go_home')
    @excepter
    @dpylogger
    async def _send_message_go_home(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)
        text = 'ただいま'
        try:
            async with aiohttp.ClientSession() as session:
                webhooks = await interaction.channel.webhooks()
                webhook = None
                for _webhook in webhooks:
                    if _webhook.user == interaction.client.user:
                        webhook = _webhook
                        break
                if webhook is None:
                    webhook = await interaction.channel.create_webhook(name='テンプレートメッセージ')
                webhook = Webhook.from_url(webhook.url, session=session)
                await webhook.send(embed=compose_embed(text, interaction.user), username=interaction.user.display_name, avatar_url=interaction.user.display_avatar.url)
            await interaction.message.delete()
            await interaction.channel.send('ボタンを押すとテンプレメッセージが投稿されます', view=TemplateMessageButton())
        except discord.errors.NotFound:
            await interaction.followup.send('エラーが発生しました', ephemeral=True)

    @discord.ui.button(label='食事中', style=discord.ButtonStyle.green, custom_id='template_message:eat')
    @excepter
    @dpylogger
    async def _send_message_eat(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)
        text = 'ご飯食べてるよ'
        try:
            async with aiohttp.ClientSession() as session:
                webhooks = await interaction.channel.webhooks()
                webhook = None
                for _webhook in webhooks:
                    if _webhook.user == interaction.client.user:
                        webhook = _webhook
                        break
                if webhook is None:
                    webhook = await interaction.channel.create_webhook(name='テンプレートメッセージ')
                webhook = Webhook.from_url(webhook.url, session=session)
                await webhook.send(embed=compose_embed(text, interaction.user), username=interaction.user.display_name, avatar_url=interaction.user.display_avatar.url)
            await interaction.message.delete()
            await interaction.channel.send('ボタンを押すとテンプレメッセージが投稿されます', view=TemplateMessageButton())
        except discord.errors.NotFound:
            await interaction.followup.send('エラーが発生しました', ephemeral=True)

    @discord.ui.button(label='暇', style=discord.ButtonStyle.green, custom_id='template_message:talk')
    @excepter
    @dpylogger
    async def _send_message_talk(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)
        text = '暇だよ'
        try:
            async with aiohttp.ClientSession() as session:
                webhooks = await interaction.channel.webhooks()
                webhook = None
                for _webhook in webhooks:
                    if _webhook.user == interaction.client.user:
                        webhook = _webhook
                        break
                if webhook is None:
                    webhook = await interaction.channel.create_webhook(name='テンプレートメッセージ')
                webhook = Webhook.from_url(webhook.url, session=session)
                await webhook.send(embed=compose_embed(text, interaction.user), username=interaction.user.display_name, avatar_url=interaction.user.display_avatar.url)
            await interaction.message.delete()
            await interaction.channel.send('ボタンを押すとテンプレメッセージが投稿されます', view=TemplateMessageButton())
        except discord.errors.NotFound:
            await interaction.followup.send('エラーが発生しました', ephemeral=True)

    @discord.ui.button(label='作業中', style=discord.ButtonStyle.green, custom_id='template_message:work')
    @excepter
    @dpylogger
    async def _send_message_work(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)
        text = '作業してるよ'
        try:
            async with aiohttp.ClientSession() as session:
                webhooks = await interaction.channel.webhooks()
                webhook = None
                for _webhook in webhooks:
                    if _webhook.user == interaction.client.user:
                        webhook = _webhook
                        break
                if webhook is None:
                    webhook = await interaction.channel.create_webhook(name='テンプレートメッセージ')
                webhook = Webhook.from_url(webhook.url, session=session)
                await webhook.send(embed=compose_embed(text, interaction.user), username=interaction.user.display_name, avatar_url=interaction.user.display_avatar.url)
            await interaction.message.delete()
            await interaction.channel.send('ボタンを押すとテンプレメッセージが投稿されます', view=TemplateMessageButton())
        except discord.errors.NotFound:
            await interaction.followup.send('エラーが発生しました', ephemeral=True)

    @discord.ui.button(label='家事中', style=discord.ButtonStyle.green, custom_id='template_message:housework')
    @excepter
    @dpylogger
    async def _send_message_housework(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)
        text = '家事をしてるよ'
        try:
            async with aiohttp.ClientSession() as session:
                webhooks = await interaction.channel.webhooks()
                webhook = None
                for _webhook in webhooks:
                    if _webhook.user == interaction.client.user:
                        webhook = _webhook
                        break
                if webhook is None:
                    webhook = await interaction.channel.create_webhook(name='テンプレートメッセージ')
                webhook = Webhook.from_url(webhook.url, session=session)
                await webhook.send(embed=compose_embed(text, interaction.user), username=interaction.user.display_name, avatar_url=interaction.user.display_avatar.url)
            await interaction.message.delete()
            await interaction.channel.send('ボタンを押すとテンプレメッセージが投稿されます', view=TemplateMessageButton())
        except discord.errors.NotFound:
            await interaction.followup.send('エラーが発生しました', ephemeral=True)

    @discord.ui.button(label='ゲーム中', style=discord.ButtonStyle.green, custom_id='template_message:game')
    @excepter
    @dpylogger
    async def _send_message_game(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)
        text = 'ゲームしてるよ'
        try:
            async with aiohttp.ClientSession() as session:
                webhooks = await interaction.channel.webhooks()
                webhook = None
                for _webhook in webhooks:
                    if _webhook.user == interaction.client.user:
                        webhook = _webhook
                        break
                if webhook is None:
                    webhook = await interaction.channel.create_webhook(name='テンプレートメッセージ')
                webhook = Webhook.from_url(webhook.url, session=session)
                await webhook.send(embed=compose_embed(text, interaction.user), username=interaction.user.display_name, avatar_url=interaction.user.display_avatar.url)
            await interaction.message.delete()
            await interaction.channel.send('ボタンを押すとテンプレメッセージが投稿されます', view=TemplateMessageButton())
        except discord.errors.NotFound:
            await interaction.followup.send('エラーが発生しました', ephemeral=True)

    @discord.ui.button(label='休憩中', style=discord.ButtonStyle.green, custom_id='template_message:rest')
    @excepter
    @dpylogger
    async def _send_message_rest(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)
        text = '休憩してるよ'
        try:
            async with aiohttp.ClientSession() as session:
                webhooks = await interaction.channel.webhooks()
                webhook = None
                for _webhook in webhooks:
                    if _webhook.user == interaction.client.user:
                        webhook = _webhook
                        break
                if webhook is None:
                    webhook = await interaction.channel.create_webhook(name='テンプレートメッセージ')
                webhook = Webhook.from_url(webhook.url, session=session)
                await webhook.send(embed=compose_embed(text, interaction.user), username=interaction.user.display_name, avatar_url=interaction.user.display_avatar.url)
            await interaction.message.delete()
            await interaction.channel.send('ボタンを押すとテンプレメッセージが投稿されます', view=TemplateMessageButton())
        except discord.errors.NotFound:
            await interaction.followup.send('エラーが発生しました', ephemeral=True)

    @discord.ui.button(label='話したい', style=discord.ButtonStyle.green, custom_id='template_message:want_talk')
    @excepter
    @dpylogger
    async def _send_message_want_talk(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)
        text = '話したい'
        try:
            async with aiohttp.ClientSession() as session:
                webhooks = await interaction.channel.webhooks()
                webhook = None
                for _webhook in webhooks:
                    if _webhook.user == interaction.client.user:
                        webhook = _webhook
                        break
                if webhook is None:
                    webhook = await interaction.channel.create_webhook(name='テンプレートメッセージ')
                webhook = Webhook.from_url(webhook.url, session=session)
                await webhook.send(embed=compose_embed(text, interaction.user), username=interaction.user.display_name, avatar_url=interaction.user.display_avatar.url)
            await interaction.message.delete()
            await interaction.channel.send('ボタンを押すとテンプレメッセージが投稿されます', view=TemplateMessageButton())
        except discord.errors.NotFound:
            await interaction.followup.send('エラーが発生しました', ephemeral=True)

    @discord.ui.button(label='声劇したい', style=discord.ButtonStyle.green, custom_id='template_message:want_voice')
    @excepter
    @dpylogger
    async def _send_message_want_voice(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)
        text = '声劇したい'
        try:
            async with aiohttp.ClientSession() as session:
                webhooks = await interaction.channel.webhooks()
                webhook = None
                for _webhook in webhooks:
                    if _webhook.user == interaction.client.user:
                        webhook = _webhook
                        break
                if webhook is None:
                    webhook = await interaction.channel.create_webhook(name='テンプレートメッセージ')
                webhook = Webhook.from_url(webhook.url, session=session)
                await webhook.send(embed=compose_embed(text, interaction.user), username=interaction.user.display_name, avatar_url=interaction.user.display_avatar.url)
            await interaction.message.delete()
            await interaction.channel.send('ボタンを押すとテンプレメッセージが投稿されます', view=TemplateMessageButton())
        except discord.errors.NotFound:
            await interaction.followup.send('エラーが発生しました', ephemeral=True)

    @discord.ui.button(label='マダミスしたい', style=discord.ButtonStyle.green, custom_id='template_message:want_mdms')
    @excepter
    @dpylogger
    async def _send_message_want_mdms(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)
        text = 'マダミスしたい'
        try:
            async with aiohttp.ClientSession() as session:
                webhooks = await interaction.channel.webhooks()
                webhook = None
                for _webhook in webhooks:
                    if _webhook.user == interaction.client.user:
                        webhook = _webhook
                        break
                if webhook is None:
                    webhook = await interaction.channel.create_webhook(name='テンプレートメッセージ')
                webhook = Webhook.from_url(webhook.url, session=session)
                await webhook.send(embed=compose_embed(text, interaction.user), username=interaction.user.display_name, avatar_url=interaction.user.display_avatar.url)
            await interaction.message.delete()
            await interaction.channel.send('ボタンを押すとテンプレメッセージが投稿されます', view=TemplateMessageButton())
        except discord.errors.NotFound:
            await interaction.followup.send('エラーが発生しました', ephemeral=True)

    @discord.ui.button(label='TRPGしたい', style=discord.ButtonStyle.green, custom_id='template_message:want_trpg')
    @excepter
    @dpylogger
    async def _send_message_want_trpg(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)
        text = 'TRPGしたい'
        try:
            async with aiohttp.ClientSession() as session:
                webhooks = await interaction.channel.webhooks()
                webhook = None
                for _webhook in webhooks:
                    if _webhook.user == interaction.client.user:
                        webhook = _webhook
                        break
                if webhook is None:
                    webhook = await interaction.channel.create_webhook(name='テンプレートメッセージ')
                webhook = Webhook.from_url(webhook.url, session=session)
                await webhook.send(embed=compose_embed(text, interaction.user), username=interaction.user.display_name, avatar_url=interaction.user.display_avatar.url)
            await interaction.message.delete()
            await interaction.channel.send('ボタンを押すとテンプレメッセージが投稿されます', view=TemplateMessageButton())
        except discord.errors.NotFound:
            await interaction.followup.send('エラーが発生しました', ephemeral=True)

    @discord.ui.button(label='ゲームしたい', style=discord.ButtonStyle.green, custom_id='template_message:want_game')
    @excepter
    @dpylogger
    async def _send_message_want_game(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)
        text = 'ゲームしたい'
        try:
            async with aiohttp.ClientSession() as session:
                webhooks = await interaction.channel.webhooks()
                webhook = None
                for _webhook in webhooks:
                    if _webhook.user == interaction.client.user:
                        webhook = _webhook
                        break
                if webhook is None:
                    webhook = await interaction.channel.create_webhook(name='テンプレートメッセージ')
                webhook = Webhook.from_url(webhook.url, session=session)
                await webhook.send(embed=compose_embed(text, interaction.user), username=interaction.user.display_name, avatar_url=interaction.user.display_avatar.url)
            await interaction.message.delete()
            await interaction.channel.send('ボタンを押すとテンプレメッセージが投稿されます', view=TemplateMessageButton())
        except discord.errors.NotFound:
            await interaction.followup.send('エラーが発生しました', ephemeral=True)

    @discord.ui.button(label='遊びたい', style=discord.ButtonStyle.green, custom_id='template_message:want_play')
    @excepter
    @dpylogger
    async def _send_message_want_play(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)
        text = '遊びたい'
        try:
            async with aiohttp.ClientSession() as session:
                webhooks = await interaction.channel.webhooks()
                webhook = None
                for _webhook in webhooks:
                    if _webhook.user == interaction.client.user:
                        webhook = _webhook
                        break
                if webhook is None:
                    webhook = await interaction.channel.create_webhook(name='テンプレートメッセージ')
                webhook = Webhook.from_url(webhook.url, session=session)
                await webhook.send(embed=compose_embed(text, interaction.user), username=interaction.user.display_name, avatar_url=interaction.user.display_avatar.url)
            await interaction.message.delete()
            await interaction.channel.send('ボタンを押すとテンプレメッセージが投稿されます', view=TemplateMessageButton())
        except discord.errors.NotFound:
            await interaction.followup.send('エラーが発生しました', ephemeral=True)


class TemplateMessageCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.bot.add_view(TemplateMessageButton())

    @app_commands.command(name='テンプレメッセージボタン', description='テンプレメッセージを投稿できるボタンを設置します')
    @app_commands.guild_only()
    @excepter
    @dpylogger
    async def _template_message_button_app_command(self, interaction: discord.Interaction):
        if not interaction.user.resolved_permissions.manage_channels:
            await interaction.response.send_message('このコマンドを実行するにはチャンネル管理権限が必要です', ephemeral=True)
            return
        await interaction.response.send_message('誰でもテンプレメッセージを投稿できるボタンです。\n投稿が行われるとボタンが一番下に再投稿されます。', ephemeral=True)
        await interaction.channel.send('ボタンを押すとテンプレメッセージが投稿されます', view=TemplateMessageButton())


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(TemplateMessageCog(bot))
