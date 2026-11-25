import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN မထည့်ရသေးပါ")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "မင်္ဂလာပါ။ ကြော်ညာပို့စ် Bot မှ ကြိုဆိုပါတယ်။\n"
        "ကြော်ညာစာပို့ရန် /post ကို အသုံးပြုပါ။"
    )

@bot.message_handler(commands=["post"])
def post(message):
    bot.reply_to(message, "ကြော်ညာစာကို ပို့ပေးပါ။")

bot.infinity_polling()
