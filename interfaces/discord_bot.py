import discord
from discord.ext import commands
from core.faq_engine import get_answer

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"[Discord] Conectado como {bot.user} (id: {bot.user.id})")

@bot.command(name="faq")
async def faq_cmd(ctx, *, pergunta: str = None):
    if not pergunta:
        await ctx.send("Use: `!faq <sua pergunta>`")
        return
    resposta = get_answer(pergunta)
    await ctx.send(resposta)

def start_discord(token: str):
    bot.run(token)

#if __name__ == "__main__":
    import os
    token = os.getenv("DISCORD_TOKEN") or "SEU_TOKEN_DISCORD"
    start_discord(token)
