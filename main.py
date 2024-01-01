from pyrogram import filters , Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from dotenv import load_dotenv
import os
import google.generativeai as genai
import PIL.Image
import random

load_dotenv()

API_HASH  = os.getenv('API_HASH')
API_ID  = os.getenv('API_ID')
BOT_TOKEN  = os.getenv('BOT_TOKEN')
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

stickers = ['CAACAgEAAxkBAAEYAqRlkq0-L_85eTtO6GdIFmZQ1--GTQACSwIAAsF-IUTpsXse4dUMzDQE',
            'CAACAgIAAxkBAAEYAqhlkq28KGjH-KawLcVvdLUfqcISWQACzQEAAhZCawrL2Zt7FoIvuDQE',
            'CAACAgIAAxkBAAEYAqllkq28y8fyXKsBf-Pc9AN9-1dIdQAC1BEAA8CgSXknAeKPK_QMNAQ',
            'CAACAgUAAxkBAAEYAqplkq28CIZj0-cZkEhRrtj4KwMHewADAwACKSRJVGYT9GcdigjdNAQ',
            'CAACAgUAAxkBAAEYAqtlkq28rAZzHDw2lQ58NnQIII_m1QACKAQAApv4OFZA66LtASf7izQE',
            'CAACAgEAAxkBAAEYAqxlkq28KegzHLH0-kZ55e_6FfngeAACRwADnjOcH98isYD5RJTwNAQ',
            'CAACAgIAAxkBAAEYAq1lkq28DAo5ep1uoVhLYhm4Hm674gACgBgAAsC2UEmimzNNrlDPPDQE',
            'CAACAgIAAxkBAAEYAq5lkq2811GiH2MxZXjHqhlYJwY_aQACoBcAAt-0IEkggKwiuyDGyTQE',
            'CAACAgIAAxkBAAEYAq9lkq28kgu8D502UUezvqKFO2CaTAACqhYAApmkEUqpUt4Hkn-q5TQE',
            'CAACAgEAAxkBAAEYArhlkq5wWchFDbNKZo0UwWb8fdvnTAACLQIAAqcjIUQ9QDDJ7YO0tjQE',
            'CAACAgEAAxkBAAEYArplkq6FqCyo7JsD8zONqUfvDslwqwACeQEAAsi3GEQBsI4FdYg9jDQE',
            'CAACAgEAAxkBAAEYArxlkq6pXH-2l-3kv271dBPnM7ZCowACXgIAAl3yGUSGa-Q11eKzuTQE',
            'CAACAgEAAxkBAAEYAr5lkq67vFPLasP0sf4oIoIV9HotEAACpwIAAnJoIUQEJZjFh8eLIzQE',
            'CAACAgEAAxkBAAEYAsBlkq7Ju3Fj3h9kTOxNGBP9ZixdAgACVgMAAr-QIUR8-pez2EZI2zQE',
            'CAACAgEAAxkBAAEYAsJlkq77-xcdFMmL983Sfza8mAfIWwACwQEAAm3SUEVB2GFv5BtTzTQE',
            'CAACAgEAAxkBAAEYAsRlkq8vtbtWWqhRNpDE6IESlP_UQwACTAMAAoIzWUTPkzhJAAElokM0BA',
            'AAMCAQADGQEAARgCxmWSrzgh6ovHyPnqi2Gdj7urXhYKAAI7AwACh49ZRKauyeoMCvDeAQAHbQADNAQ',
            'CAACAgEAAxkBAAEYAsZlkq84IeqLx8j56othnY-7q14WCgACOwMAAoePWUSmrsnqDArw3jQE',
            'CAACAgEAAxkBAAEYAshlkq9Xr90XEAVGsRymtQ7I82Ul3QACSQMAAs7EoEafktk_u7gHIzQE',
            'CAACAgEAAxkBAAEYAsplkq-IJjDNCIsad6aneyYasqnzvAACBwIAAknHoUZrTecesaz05zQE'            
            ]

GITHUB_BUTTON = InlineKeyboardMarkup(
            [[InlineKeyboardButton("Follow me on Github Source Code", url='https://github.com/nuhmanpk/')]]
        )

app= Client('VisionScriptBot',
            api_hash=API_HASH,api_id=int(API_ID),
            bot_token=BOT_TOKEN)

genai.configure(api_key=GOOGLE_API_KEY)




@app.on_message(filters.command('start') & filters.private)
async def start(_,message:Message):
    welcome_message = (
        f"👋 Hey @{message.chat.username}!\n\n"
        "I'm here to help. Just send me an image, and I'll do the rest.\n\n"
        "Feel free to explore and use my features. If you have any questions or need assistance, "
        "you can use the /help command.\n\n"
        "🤖 Don't forget to join @BughunterBots for more awesome bots like me!\n"
    )
    await message.reply(welcome_message,quote=True)

@app.on_message(filters.command('help') & filters.private)
async def help_command(_, message: Message):
    help_message = (
        "🤖 **How to use the Transcription Bot**\n\n"
        "1. **Send an Image:** Simply send me an image containing text that you want transcribed.\n"
        "2. **Wait for Transcription:** I'll process the image and provide you with the transcribed text.\n\n"
        "For updates and more bots, join @BughunterBots 🚀\n"
    )
    await message.reply(help_message, quote=True)

@app.on_message(filters.photo & filters.private)
async def vision(bot,message:Message):
    try:
        model_name = 'gemini-pro-vision'
        txt = await message.reply(f'Loading {model_name} ...')
        model = genai.GenerativeModel(model_name)
        await txt.edit("Model Loaded")
        await txt.edit('Downloading Photo ....')
        file_path = await message.download()
        img = PIL.Image.open(file_path)
        sticker_id = random.choice(stickers)
        sticker = await message.reply_sticker(sticker_id)
        await txt.edit('Shhh 🤫 , Gemini Vision Pro is At Work ⚠️. Pls Wait...')
        response = model.generate_content(img)
        os.remove(file_path)
        await sticker.delete()
        await txt.delete()
        if response.text:
            await message.reply(response.text)
        else:
            await message.reply('Couldn\'t figure out what\'s in the Image. Contact @bughunter0 for help.')
        msg =    ("📢 **Exciting Announcement!** 📢\n\n"
        "I'm thrilled to let you know that the source code for this bot will be posted soon on GitHub! 🚀\n\n"
        "Stay tuned and make sure to **Follow Me** here on Telegram for the latest updates. 🌟\n\n"
        "Thank you for your support! 👏\n\n"
        "Happy Coding! 🚀")
        await message.reply(msg,reply_markup=GITHUB_BUTTON)
    except Exception as e:
        await message.reply('Something Bad occured, Contact @bughunter0')
        raise e

@app.on_message(filters.document & filters.private)
async def document(bot,message:Message):
    await message.reply('Documents are not supported, Please the File as Image !!!\n\n @BughunterBots')
    
app.run(print('Bot Started...'))