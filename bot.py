import telegram.ext
import validators
import main
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

def start(update, context):
    update.message.reply_text("Hello! Welcome to 英國經濟圈 News Summary Bot!")

def help(update, context):
    update.message.reply_text("""
    Pass me a news url and I will summarise it for you! The following commands are also available:

    /start -> Welcome Message
    /help -> This Message
    /contact -> Information About Contact
    """)

def content(update, context):
    update.message.reply_text("Trial")

def contact(update, context):
    update.message.reply_text("You can contact me @applechan123")

def handle_message(update, context):
    if validators.url(update.message.text) == True:
        titlestring, news_summary, hashtags = main.main(update.message.text)
        # update.message.reply_photo(photo=open(filename, 'rb'))
        update.message.reply_text(f"{titlestring}\n\n{news_summary}\n\n{hashtags}\n\nNews source: {update.message.text}.replace('https://','')")

updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start",start))
disp.add_handler(telegram.ext.CommandHandler("help",help))
disp.add_handler(telegram.ext.CommandHandler("content",content))
disp.add_handler(telegram.ext.CommandHandler("contact",contact))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

updater.start_polling()
updater.idle()