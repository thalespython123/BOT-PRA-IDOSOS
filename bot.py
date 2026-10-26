import random
import os
import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True
intents.members = True


bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("OLÁ, EU SOU O BOT ASSECÍVEL PARA IDOSOS, EU ENSINO SOBRE O DESMATAMENTO E COMO ELE DEVE SER COMBATIDO")

@bot.command()
async def dicas(ctx):
    await ctx.send("SEMPRE TENTE DESCARTAR QUALQUER TIPO DE LIXO DE FORMA CERTA")
    await ctx.send("VALORIZE O MEIO AMBIENTE, NÃO DESTRUA O QUE PODE SER IMPORTANTE PARA VOCÊ E SUA CONVIVÊNCIA SAUDÁVEL")
@bot.command()
async def economia(ctx):
    await ctx.send("QUER VER ALGUNS SITER PARA ECONOMIA DE ENERGIA?")
    await ctx.send('AQUI: https://www.minhacasasolar.com.br/')
    await ctx.send('https://www.findernet.com/pt/brasil/news/como-otimizar-o-consumo-e-economizar-energia-com-a-finder/')
    await ctx.send('https://fitenergia.com.br/')

# Média aproximada de lixo por pessoa (kg/dia). Ajuste se tiver um dado melhor.
LIXO_KG_POR_PESSOA_DIA = 3.0

@bot.command(name="lixo")
async def lixo(ctx, pessoas: int):
    if pessoas <= 0:
        await ctx.send("INFORME UM NUMERO DE PESSOAS MAIOR QUE ZERO. EX: `4`")
        return

    dia = pessoas * LIXO_KG_POR_PESSOA_DIA
    semana = dia * 7
    mes = dia * 365


    ano = dia * 365

    await ctx.send(
        f"🗑️ **Estimativa de lixo para {pessoas} pessoa(s):**\n"
        f"• Por dia: {dia:.1f} kg\n"
        f"• Por semana: {semana:.1f} kg\n"
        f"• Por mês: {mes:.1f} kg\n"
        f"• Por ano: {ano:.1f} kg"
    )

@bot.command()
async def manual(ctx):
    await ctx.send('https://www.facebook.com/projetoagua.org/posts/iniciamos-a-semana-do-meio-ambientenosso-alerta-%C3%A9-queimadas-diga-n%C3%A3oas-queimadas/866699875484420/')


@lixo.error
async def lixo_error(ctx, error):
    if isinstance(error, (commands.MissingRequiredArgument, commands.BadArgument)):
        await ctx.send("Use assim: `$lixo <número de pessoas>`. Ex.: `/lixo 4`")

bot.run("TOKEN AQUI!")
