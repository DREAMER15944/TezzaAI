#####################PROJECT MADE BY RAZEX PLEASE DONT FORGET TO LIKE THE VIDEO YOU WATCHED JUST TO SUPPORT ME AND READ "readme.md" FILE #####################

#############ALSO IF YOU WANT ME TO BLOW YOUR MIND WITH AI TOOLS AND BOTS PLEASE SUBSCRIBE AND LIKE MY VIDEOS THAT S ALL WHAT I WANT NOTHING ELSE ################################""

import aiohttp
import discord
import io
import os
import random
import os
from urllib.parse import quote
import aiohttp
import discord
import io
import time
import random
from model_enum import Model as P_model
from discord.ext import commands
from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents, heartbeat_timeout=60)

load_dotenv()


TOKEN = os.getenv("TOKEN") # env option bah t7oti token te3 bot t3k w tconnectih lel code 


@bot.event
async def on_ready():
    await bot.tree.sync()
    num_commands = len(bot.commands)

    invite_link = discord.utils.oauth_url(
        bot.user.id,
        permissions=discord.Permissions(),
        scopes=("bot", "applications.commands")
    )
  

    def print_in_color(text, color):
        return f"\033[{color}m{text}\033[0m"

    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

    ascii_art = """
    \033[1;35m

███████╗██████╗ ███████╗██╗  ██╗████████╗██████╗ ██╗   ██╗███╗   ███╗
██╔════╝██╔══██╗██╔════╝██║ ██╔╝╚══██╔══╝██╔══██╗██║   ██║████╗ ████║
███████╗██████╔╝█████╗  █████╔╝    ██║   ██████╔╝██║   ██║██╔████╔██║
╚════██║██╔═══╝ ██╔══╝  ██╔═██╗    ██║   ██╔══██╗██║   ██║██║╚██╔╝██║
███████║██║     ███████╗██║  ██╗   ██║   ██║  ██║╚██████╔╝██║ ╚═╝ ██║
╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝

\033[0m
    """

    print(ascii_art)
    print(print_in_color(f"{bot.user} aka {bot.user.name} has connected to Discord!", "\033[1;97"))
    print(print_in_color(f"  Loaded {num_commands} commands", "1;35"))
    print(print_in_color(f"      Invite link: {invite_link}", "1;36"))
    print(print_in_color(f"      Invite link: https://discord.gg/t75D68H7NB \n subscribe for more https://www.youtube.com/@Spectrum-Raz/featured", "1;36"))
    


async def generate_image_prodia(prompt, model, sampler, seed, neg):
    print("\033[1;32m(Prodia) Creating image for :\033[0m", prompt)
    start_time = time.time()

    async def create_job(prompt, model, sampler, seed, neg):
        if neg is None:
            negative = "(nsfw:1.5),verybadimagenegative_v1.3, ng_deepnegative_v1_75t, (ugly face:0.8),cross-eyed,sketches, (worst quality:2), (low quality:2), (normal quality:2), lowres, normal quality, ((monochrome)), ((grayscale)), skin spots, acnes, skin blemishes, bad anatomy, DeepNegative, facing away, tilted head, {Multiple people}, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worstquality, low quality, normal quality, jpegartifacts, signature, watermark, username, blurry, bad feet, cropped, poorly drawn hands, poorly drawn face, mutation, deformed, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, extra fingers, fewer digits, extra limbs, extra arms,extra legs, malformed limbs, fused fingers, too many fingers, long neck, cross-eyed,mutated hands, polar lowres, bad body, bad proportions, gross proportions, text, error, missing fingers, missing arms, missing legs, extra digit, extra arms, extra leg, extra foot, repeating hair, nsfw, [[[[[bad-artist-anime, sketch by bad-artist]]]]], [[[mutation, lowres, bad hands, [text, signature, watermark, username], blurry, monochrome, grayscale, realistic, simple background, limited palette]]], close-up, (swimsuit, cleavage, armpits, ass, navel, cleavage cutout), (forehead jewel:1.2), (forehead mark:1.5), (bad and mutated hands:1.3), (worst quality:2.0), (low quality:2.0), (blurry:2.0), multiple limbs, bad anatomy, (interlocked fingers:1.2),(interlocked leg:1.2), Ugly Fingers, (extra digit and hands and fingers and legs and arms:1.4), crown braid, (deformed fingers:1.2), (long fingers:1.2)"
        else:
            negative = neg
        url = 'https://api.prodia.com/generate'
        params = {
            'new': 'true',
            'prompt': f'{quote(prompt)}',
            'model': model,
            'negative_prompt': f"{negative}",
            'steps': '100',
            'cfg': '9.5',
            'seed': f'{seed}',
            'sampler': sampler,
            'upscale': 'True',
            'aspect_ratio': 'square'
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                data = await response.json()
                return data['job']

    job_id = await create_job(prompt, model, sampler, seed, neg)
    url = f'https://api.prodia.com/job/{job_id}'
    headers = {
        'authority': 'api.prodia.com',
        'accept': '*/*',
    }

    async with aiohttp.ClientSession() as session:
        while True:
            async with session.get(url, headers=headers) as response:
                json = await response.json()
                if json['status'] == 'succeeded':
                    async with session.get(f'https://images.prodia.xyz/{job_id}.png?download=1',
                                           headers=headers) as response:
                        content = await response.content.read()
                        img_file_obj = io.BytesIO(content)
                        duration = time.time() - start_time
                        print(f"\033[1;34m(Prodia) Finished image creation\n\033[0mJob id : {job_id}  Prompt : ",
                              prompt, "in", duration, "seconds.")
                        return img_file_obj


@bot.hybrid_command(name="imagine", description="Command to imagine an image")
@app_commands.choices(sampler=[
    app_commands.Choice(name='📏 Euler (Recommended)', value='Euler'),
    app_commands.Choice(name='📏 Euler a', value='Euler a'),
    app_commands.Choice(name='📐 Heun', value='Heun'),
    app_commands.Choice(name='💥 DPM++ 2M Karras', value='DPM++ 2M Karras'),
    app_commands.Choice(name='🔍 DDIM', value='DDIM')
])
@app_commands.choices(model=[
    app_commands.Choice(name='🌈 Elldreth vivid mix (Landscapes, Stylized characters, nsfw)', value='ELLDRETHVIVIDMIX'),
    app_commands.Choice(name='💪 Deliberate v2 (Anything you want, nsfw)', value='DELIBERATE'),
    app_commands.Choice(name='🔮 Dreamshaper (HOLYSHIT this so good)', value='DREAMSHAPER_6'),
    app_commands.Choice(name='🎼 Lyriel', value='LYRIEL_V16'),
    app_commands.Choice(name='💥 Anything diffusion (Good for anime)', value='ANYTHING_V4'),
    app_commands.Choice(name='🌅 Openjourney (Midjourney alternative)', value='OPENJOURNEY'),
    app_commands.Choice(name='🏞️ Realistic (Lifelike pictures)', value='REALISTICVS_V20'),
    app_commands.Choice(name='👨‍🎨 Portrait (For headshots I guess)', value='PORTRAIT'),
    app_commands.Choice(name='🌟 Rev animated (Illustration, Anime)', value='REV_ANIMATED'),
    app_commands.Choice(name='🤖 Analog', value='ANALOG'),
    app_commands.Choice(name='🌌 AbyssOrangeMix', value='ABYSSORANGEMIX'),
    app_commands.Choice(name='🌌 Dreamlike v1', value='DREAMLIKE_V1'),
    app_commands.Choice(name='🌌 Dreamlike v2', value='DREAMLIKE_V2'),
    app_commands.Choice(name='🌌 Dreamshaper 5', value='DREAMSHAPER_5'),
    app_commands.Choice(name='🌌 MechaMix', value='MECHAMIX'),
    app_commands.Choice(name='🌌 MeinaMix', value='MEINAMIX'),
    app_commands.Choice(name='🌌 Stable Diffusion v14', value='SD_V14'),
    app_commands.Choice(name='🌌 Stable Diffusion v15', value='SD_V15'),
    app_commands.Choice(name="🌌 Shonin's Beautiful People", value='SBP'),
    app_commands.Choice(name="🌌 TheAlly's Mix II", value='THEALLYSMIX'),
    app_commands.Choice(name='🌌 Timeless', value='TIMELESS')
])

@app_commands.describe(
    prompt="Write a amazing prompt for a image",
    model="Model to generate image",
    sampler="Sampler for denosing",
    negative="Prompt that specifies what you do not want the model to generate"

)
@commands.guild_only()

async def imagine_prodia(ctx, prompt: str, model: app_commands.Choice[str], sampler: app_commands.Choice[str],
                         negative: str = None, seed: int = None):
    if seed is None:
        seed = random.randint(10000, 99999)
    await ctx.defer()

    model_uid = P_model[model.value].value[0]




    imagefileobj = await generate_image_prodia(prompt, model_uid, sampler.value, seed, negative)


    img_file = discord.File(imagefileobj, filename="image.png", description=prompt)


    embed = discord.Embed(color=discord.Color.random())
    embed.title = f"🎨Generated Image by {ctx.author.display_name}"
    embed.add_field(name='📝 Prompt', value=f'- {prompt}', inline=False)
    if negative is not None:
        embed.add_field(name='📝 Negative Prompt', value=f'- {negative}', inline=False)
    embed.add_field(name='🤖 Model', value=f'- {model.value}', inline=True)
    embed.add_field(name='🧬 Sampler', value=f'- {sampler.value}', inline=True)
    embed.add_field(name='🌱 Seed', value=f'- {str(seed)}', inline=True)



    await ctx.send(embed=embed, file=img_file)

  



#---------------------------------------------Run Bot-------------------------------------------------
bot.run(TOKEN)
