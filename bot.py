import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Bot token
TOKEN = "7980421671:AAFhM7QQtrEj45X36tqxOpyptZ0Pr0Jg708"

# Botu başlat
bot = telebot.TeleBot(TOKEN)

# /start komutu
@bot.message_handler(commands=['start'])
def start(message):
    user = message.from_user
    welcome_message = (
        f"👋 Hello @{user.username}!\n"
        "🌟 Welcome to TokenCreatorBot! 🌟\n\n"
        "This bot allows you to easily create your own token on the Solana network. 🚀\n\n"
        "✨ No coding skills required!\n"
        "💰 Launch your project effortlessly!\n\n"
        "To get started, click the button below or use the /help command for more information."
    )

    # Inline buton oluşturma
    markup = InlineKeyboardMarkup()
    # WebAppInfo ile Mini App olarak URL'yi ekliyoruz
    web_app = WebAppInfo(url="https://glittering-cranachan-d4f688.netlify.app")
    markup.add(InlineKeyboardButton("🚀 Create Token", web_app=web_app))

    bot.reply_to(message, welcome_message, reply_markup=markup)

# /help komutu
@bot.message_handler(commands=['help'])
def help_command(message):
    help_message = (
        "📝 *Commands:*\n"
        "/start - Start the bot and display the welcome message.\n"
        "/help - Show available commands and usage information.\n"
        "/info - Learn more about the Solana network and token creation."
    )
    bot.reply_to(message, help_message, parse_mode="Markdown")

# /info komutu
@bot.message_handler(commands=['info'])
def info_command(message):
    info_message = (
        "💡 *About Solana Network:*\n"
        "Solana is a high-performance blockchain supporting fast transactions and low fees.\n"
        "With this bot, you can easily create your own Solana token."
    )
    bot.reply_to(message, info_message, parse_mode="Markdown")

# Botu çalıştır
def main():
    print("Bot is running...")
    bot.polling()

if __name__ == "__main__":
    main()
