import discord
from discord.ext import commands, tasks
import random
import asyncio
import traceback

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# ================== SETTINGS ==================
CHANNEL_ID = 1495439811509489814   # ← YOUR NEW CHANNEL
BOT_TOKEN = os.getenv("BOT_TOKEN")

# ================== OG / HIGH TIER (every ~30 min) ==================
OG_BRAINROTS = [
    "Love Love Bear", "Dragon Cannelloni", "Dragon Gingerini", "Hydra Dragon Cannelloni",
    "Griffin", "Secret Lucky Block", "Skibidi Toilet", "Headless Horseman",
    "Meowl", "Strawberry Elephant"
]

# ================== ALL OTHER 10M+ BRAINROTS ==================
ALL_OTHER_BRAINROTS = [
    "Los Mi Gatitos", "Noo my Eggs", "Los Chicleteiras", "67", "Donkeyturbo Express",
    "Los Burritos", "Los 25", "Tacorillo Crocodillo", "Mariachi Corazoni", "Noo my Heart",
    "Swag Soda", "Noo my Gold", "Chimnino", "Bananito", "Chicleteira Noelteira",
    "Los Combinasionas", "Fishino Clownino", "Baskito", "Los Sweethearts",
    "Tacorita Bicicleta", "Spinny Hammy", "Nuclearo Dinossauro", "DJ Panda", "Las Sis",
    "Chicleteira Cupideira", "Chillin Chili", "Money Money Reindeer", "Chipso and Queso",
    "Los Bros", "Money Money Puggy", "Churrito Bunnito", "Los Planitos", "Snailo Clovero",
    "Los Mobilis", "Celularcini Viciosini", "Los 67", "Tuff Toucan", "Mieteteira Bicicleteira",
    "Gobblino Uniciclino", "La Spooky Grande", "Los Jolly Combinasionas", "Cigno Fulgoro",
    "Los Spooky Combinasionas", "Los Hotspotsitos", "Los Candies", "Globa Steppa",
    "Tralaledon", "Los Cupids", "Los Puggies", "W or L", "La Extinct Grande",
    "Esok Sekolah", "La Jolly Grande", "Los Primos", "Bacuru and Egguru", "Eviledon",
    "Los Tacoritas", "Lovin Rose", "Tang Tang Keletang", "Ketupat Kepat", "La Taco Combinasion",
    "Dug Dug Dug", "Tictac Sahur", "Swaggy Bros", "La Romantic Grande", "La Supreme Combinasion",
    "Orcaledon", "Rico Dinero", "Ketchuru And Musturu", "Jolly Jolly Sahur", "Gold Gold Gold",
    "Nacho Spyder", "Rosetti Tualetti", "Garama and Madundung", "Hopilikalika Hopilikalako",
    "Elefanto Frigo", "Cloverat Clapat", "Spaghetti Tualetti", "Ventoliero Pavonero",
    "Quackini Snackini", "Festive 67", "Los Spaghettis", "Sammyni Fattini", "Hokka Horloge",
    "Ginger Gerat", "La Ginger Sekolah", "Boppin Bunny", "Spooky and Pumpky", "Lavadorito Spinito",
    "La Food Combinasion", "Cash or Card", "Fragrama and Chocrama", "La Casa Boo",
    "Signore Carapace", "Los Sekolahs", "Foxini Lanternini", "La Secret Combinasion",
    "Fortunu and Cashuru", "Los Amigos", "Reinito Sleighito", "Ketupat Bros",
    "Burguro And Fryuro", "Pancake and Syrup", "Cooki and Milki", "Capitano Moby",
    "Rosey and Teddy", "Bunny and Eggy", "Popcuru and Fizzuru"
]

def generate_brainrot(tier):
    if tier == "og":
        name = random.choice(OG_BRAINROTS)
        # Headless Horseman = 0.9% chance only
        if name == "Headless Horseman" and random.random() > 0.009:
            name = random.choice([n for n in OG_BRAINROTS if n != "Headless Horseman"])
        return name
    else:
        return random.choice(ALL_OTHER_BRAINROTS)

@bot.event
async def on_ready():
    print(f"✅ Logs Bot is online as {bot.user}")
    low_loop.start()
    mid_loop.start()
    og_loop.start()

# LOW + MID TIER - fast spam (1-3 seconds)
@tasks.loop(seconds=1)
async def low_loop():
    try:
        channel = bot.get_channel(CHANNEL_ID)
        if not channel: return
        name = generate_brainrot("normal")
        embed = discord.Embed(title="🧠 Brainrot Logs", description=f"**{name}**", color=0x2C2F33)
        embed.set_footer(text="Meowl Notifier | Logs v2.4")
        await channel.send(embed=embed)
        await asyncio.sleep(random.randint(1, 3))
    except Exception as e:
        print(f"❌ Fast loop error: {e}")

# MID TIER - 10-30 seconds
@tasks.loop(seconds=10)
async def mid_loop():
    try:
        channel = bot.get_channel(CHANNEL_ID)
        if not channel: return
        name = generate_brainrot("normal")
        embed = discord.Embed(title="🧠 Brainrot Logs", description=f"**{name}**", color=0x2C2F33)
        embed.set_footer(text="Meowl Notifier | Logs v2.4")
        await channel.send(embed=embed)
        await asyncio.sleep(random.randint(10, 30))
    except Exception as e:
        print(f"❌ Mid loop error: {e}")

# OG TIER - every ~30 minutes
@tasks.loop(seconds=1800)
async def og_loop():
    try:
        channel = bot.get_channel(CHANNEL_ID)
        if not channel: return
        name = generate_brainrot("og")
        is_duel = random.random() < 0.3
        icon = "⚔️" if is_duel else "⭐"
        embed = discord.Embed(title="🧠 Brainrot Logs", description=f"**{icon} {name}**", color=0x2C2F33)
        embed.set_footer(text="Meowl Notifier | Logs v2.4")
        await channel.send(embed=embed)
        print(f"✅ OG sent → {name}")
    except Exception as e:
        print(f"❌ OG loop error: {e}")

@bot.command()
async def sendlogs(ctx):
    await low_loop()
    await mid_loop()
    await og_loop()

if __name__ == "__main__":
    print("🚀 Starting Meowl Logs Bot...")
    try:
        bot.run(BOT_TOKEN)
    except Exception as e:
        print(f"❌ Bot crashed: {e}")
        traceback.print_exc()
    finally:
        input("\n\nBot stopped. Press Enter to close the window...")
