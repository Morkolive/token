const { Telegraf, Markup } = require('telegraf');
const express = require('express');

const TOKEN = "7980421671:AAFhM7QQtrEj45X36tqxOpyptZ0Pr0Jg708";
const bot = new Telegraf(TOKEN);

const app = express();
app.use(bot.webhookCallback('/bot'));
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Bot sunucusu çalışıyor: http://localhost:${PORT}`);
});

// Webhook ayarlama
bot.telegram.setWebhook(`https://<vercel-proje-adın>.vercel.app/bot`);

// /start komutu
bot.start((ctx) => {
  const user = ctx.from;
  const welcomeMessage = `
👋 Hello @${user.username}!
🌟 Welcome to TokenCreatorBot! 🌟

This bot allows you to easily create your own token on the Solana network. 🚀

✨ No coding skills required!
💰 Launch your project effortlessly!

To get started, click the button below or use the /help command for more information.
  `;

  ctx.replyWithMarkdown(welcomeMessage, Markup.inlineKeyboard([
    Markup.button.webApp("🚀 Create Token", "https://glittering-cranachan-d4f688.netlify.app")
  ]));
});

// /help komutu
bot.command('help', (ctx) => {
  const helpMessage = `
📝 *Commands:*
/start - Start the bot and display the welcome message.
/help - Show available commands and usage information.
/info - Learn more about the Solana network and token creation.
  `;
  ctx.replyWithMarkdown(helpMessage);
});

// /info komutu
bot.command('info', (ctx) => {
  const infoMessage = `
💡 *About Solana Network:*
Solana is a high-performance blockchain supporting fast transactions and low fees.
With this bot, you can easily create your own Solana token.
  `;
  ctx.replyWithMarkdown(infoMessage);
});

bot.launch();
console.log("Bot çalışıyor...");
