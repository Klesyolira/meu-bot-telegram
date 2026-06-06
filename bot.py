import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# Pega o token das variáveis de ambiente do Render
TOKEN = os.environ.get("TOKEN_BOT")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Painel Yoru Shield conectado com sucesso!')

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot rodando...")
    app.run_polling()
