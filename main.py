import telebot

TOKEN = "YOUR_BOT_TOKEN"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "မင်္ဂလာပါ။ Bot အလုပ်လုပ်နေပါပြီ။")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "Bot အသုံးပြုရန် /start ကိုနှိပ်ပါ။")

bot.infinity_polling()
