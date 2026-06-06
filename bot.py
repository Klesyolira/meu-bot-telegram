import os
import logging
from telegram.ext import ApplicationBuilder, CommandHandler

# Configuração de logs para ajudar a ver o erro no Render
logging.basicConfig(level=logging.INFO)

TOKEN = os.environ.get("TOKEN_BOT")

async def start(update, context):
    await update.message.reply_text('O bot está online!')

if __name__ == '__main__':
    if not TOKEN:
        print("ERRO: O TOKEN_BOT não foi encontrado nas variáveis de ambiente!")
    else:
        print("Iniciando o bot...")
        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.run_polling()
