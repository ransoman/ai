import requests
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Ganti ini dengan milik kamu
BOT_TOKEN = '7784432854:AAEjbMIUZpeqbVN8FjcSiLnF7-rq7xNI7bw'
OPENROUTER_API_KEY = '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'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text

    headers = {
        'Authorization': f'Bearer {OPENROUTER_API_KEY}',
        'Content-Type': 'application/json'
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are Raj X AI, a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    }

    try:
        response = requests.post(
            'https://openrouter.ai/api/v1/chat/completions',
            headers=headers,
            json=data
        )

        if response.status_code == 200:
            reply = response.json()['choices'][0]['message']['content']
        else:
            reply = f"⚠️ Error: {response.status_code} - {response.text}"

    except Exception as e:
        reply = f"❌ Exception: {str(e)}"

    await update.message.reply_text(reply)

def main():
    print("Raj X AI is now running... 🤖")
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == '__main__':
    main()
