# Made by Flank#1337

import requests
import discord
from discord.ext import tasks
from discord.ext import commands
from libs.check_modules import check_modules
from sys import exit
from os import _exit
from os import path
from libs.utils import print_success
from libs.utils import print_error
from libs.utils import ask_question
from libs.utils import print_status
from libs.utils import parse_proxy_file
from libs.proxy_harvester import find_proxies
from libs.attack import report_profile_attack
from libs.attack import report_video_attack
from multiprocessing import Process
from colorama import Fore, Back, Style

bot = discord.Bot()

token = "put discord bot token and enable all intents lol"

check_modules()

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def profile_attack_process(username, proxy_list):
    if (len(proxy_list) == 0):
        for _ in range(10):
            report_profile_attack(username, None)
        return

    for proxy in proxy_list:
        report_profile_attack(username, proxy)

def video_attack_process(video_url, proxy_list):
    if (len(proxy_list) == 0):
        for _ in range(10):
            report_video_attack(video_url, None)
        return

    for proxy in proxy_list:
        report_video_attack(video_url, proxy)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user} and are serving at {len(bot.guilds)} Guilds!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"Instagram API"))

@bot.slash_command(description="Sends Reports")
async def report(ctx, username):

    for k in range(5):
        p = Process(target=profile_attack_process, args=(username, [],))
        p.start()
        print_status(str(k + 1) + ". Transaction Opened!")

    color = discord.Color.blue()
    bot_embed = discord.Embed(title=f'{username}',color=color)
    bot_embed.add_field(name=":zap: Started sending reports to...",value=f'```@{username}```' )    
        
    await ctx.respond(embeds=[bot_embed])



if __name__ == "__main__":
    try:
        bot.run(token)
        print(Style.RESET_ALL)
    except KeyboardInterrupt:
        print("\n\n" + Fore.RED + "[*] Program is closing!")
        print(Style.RESET_ALL)
        _exit(0)

