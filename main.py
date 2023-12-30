from pyrogram import filters , Client
from pyrogram.types import Message
from dotenv import load_dotenv
import os
import google.generativeai as genai
import PIL.Image

load_dotenv()

API_HASH  = os.getenv('API_HASH')
API_ID  = os.getenv('API_ID')
BOT_TOKEN  = os.getenv('BOT_TOKEN')
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

app= Client('VisionScriptBot',
            api_hash=API_HASH,api_id=int(API_ID),
            bot_token=BOT_TOKEN)

genai.configure(api_key=GOOGLE_API_KEY)




@app.on_message(filters.command('start') & filters.private)
async def start(_,message:Message):
    welcome_message = (
        f"👋 Hey @{message.chat.username}!\n\n"
        "I'm here to help you transcribe text from images. Just send me an image, and I'll do the rest.\n\n"
        "Feel free to explore and use my features. If you have any questions or need assistance, "
        "you can use the /help command.\n\n"
        "🤖 Don't forget to join @bughunterbots for more awesome bots like me!\n"
    )
    await message.reply(welcome_message,quote=True)

@app.on_message(filters.command('help') & filters.private)
async def help_command(_, message: Message):
    help_message = (
        "🤖 **How to use the Transcription Bot**\n\n"
        "1. **Send an Image:** Simply send me an image containing text that you want transcribed.\n"
        "2. **Wait for Transcription:** I'll process the image and provide you with the transcribed text.\n\n"
        "For updates and more bots, join @bughunterbots 🚀\n"
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
        await txt.edit('Shhh 🤫 , Gemini Vision Pro is At Work ⚠️')
        response = model.generate_content(img)
        os.remove(file_path)
        await txt.delete()
        await message.reply(response.text)
    except Exception as e:
        await message.reply('Something Bad occured, Contact @bughunter0')
        raise e

    
app.run(print('Bot Started...'))