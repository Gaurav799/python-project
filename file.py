from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("5539687232:AAEarBY6sD91E9neF37E3HHixj0g62daypQ",
                use_context=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        """Hello friends, Welcome to the Bot.Digipodium is a platform which reaches out to its audiences to help them enrich their lives in a bigger and better manner through specializations,in the Fields of I.T. Training Digital Marketing Corporate Events coordination.Please write\
        /help
        to see the commands available.""")

def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
    /youtube - To get the youtube URL
    /linkedin - To get the LinkedIn profile URL
    /Connect - To get connect form URL
    /github - To get the Github URL
    /facebook - To get connect link facebook
    /Internship - To apply for Internship """)


def konect_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "find are physical coordinates & fill in detailsto helps us connect you https://digipodium.com/web/contact/)")


def youtube_url(update: Update, context: CallbackContext):
    update.message.reply_text("Youtube Link =>\
    https://www.youtube.com/channel/UCyob7nX8d2i2Ik8vgpI-qvg")


def linkedIn_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "LinkedIn URL => \
        https://www.linkedin.com/company/summertrainingandinternship2022/")


def github_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "github URL => \
            https://github.com/digipodium")


def fb_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "facebook connect URL => \
            https://www.facebook.com/digipodium")


def internship_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "fill in the details to apply for intership => \
            https://docs.google.com/forms/d/e/1FAIpQLSfeIKNSUgx7d702Tt-5R9rFXpDasOHaEcdKNsiVQbKRSVW9vA/viewform")

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url))
updater.dispatcher.add_handler(CommandHandler('connect', konect_url))
updater.dispatcher.add_handler(CommandHandler('github', github_url))
updater.dispatcher.add_handler(CommandHandler('facebook', fb_url))
updater.dispatcher.add_handler(CommandHandler('Internship', internship_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))  # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()