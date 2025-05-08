from dotenv import load_dotenv
import logging
import os
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ChatMemberUpdated
from telegram.ext import (
    Application,
    ChatMemberHandler,
    CommandHandler,
    CallbackQueryHandler,
    CallbackContext
)

load_dotenv()

# === Logging ===
logging.basicConfig(level=logging.INFO)

# === Bot Token ===
TOKEN = os.getenv("BOT_TOKEN")
app = Application.builder().token(TOKEN).build()

# === File to track welcomed users ===
WELCOMED_USERS_FILE = "welcomed_users.txt"
if not os.path.exists(WELCOMED_USERS_FILE):
    open(WELCOMED_USERS_FILE, "w").close()

# === Time-Based Greeting ===
def get_time_greeting():
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "🌅 Good Morning"
    elif 12 <= hour < 17:
        return "🌞 Good Afternoon"
    elif 17 <= hour < 21:
        return "🌇 Good Evening"
    else:
        return "🌙 Good Night"

# === Menu Buttons ===
def main_menu():
    keyboard = [
        [
            InlineKeyboardButton("🌐 Website", callback_data="website"),
            InlineKeyboardButton("ℹ️ About Me", callback_data="about"),
        ],
        [
            InlineKeyboardButton("💻 Code", callback_data="code"),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

# === Check if user is already welcomed ===
def has_been_welcomed(user_id: int) -> bool:
    with open(WELCOMED_USERS_FILE, "r") as file:
        return str(user_id) in file.read()

def mark_as_welcomed(user_id: int):
    with open(WELCOMED_USERS_FILE, "a") as file:
        file.write(f"{user_id}\n")

# === Intro message on first join ===
def get_intro_message(full_name):
    greeting = get_time_greeting()
    return (
        f"{greeting}, <b>{full_name}</b>! 👋\n\n"
        "🤖 I'm <b>Rajesh</b>, the official bot of <b>Double Negative</b>.\n"
        "I’m here to assist the team with everything tech and teamwork related!\n\n"
        "📌 Ping me for any help anytime by typing <b>/start</b> in the chat.\n\n"
        "How may I assist you today?"
    )

# === Greeting for /start ===
def get_greeting_only(full_name):
    greeting = get_time_greeting()
    return f"{greeting}, <b>{full_name}</b>! 👋\n\nHow may I assist you today?"

# === Handle new member ===
async def welcome_new_member(update: Update, context: CallbackContext):
    result: ChatMemberUpdated = update.chat_member
    user = result.new_chat_member.user
    if result.new_chat_member.status == "member" and not has_been_welcomed(user.id):
        full_name = user.full_name or "there"
        intro_message = get_intro_message(full_name)
        await context.bot.send_message(
            chat_id=update.chat_member.chat.id,
            text=intro_message,
            reply_markup=main_menu(),
            parse_mode="HTML"
        )
        mark_as_welcomed(user.id)

# === /start Command ===
async def start(update: Update, context: CallbackContext):
    user = update.effective_user
    full_name = user.full_name or "there"
    message = get_greeting_only(full_name)

    await update.message.reply_text(
        message,
        reply_markup=main_menu(),
        parse_mode="HTML"
    )

# === Button Click Handler ===
async def handle_buttons(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()

    user_full_name = query.from_user.full_name or "User"

    responses = {
        "website": "🌐 Visit our official website:\nhttps://doublenegative.online/",
        "code": "💻 Explore our GitHub:\nhttps://github.com/dneg-moscow",
        "about": (
            "ℹ️ <b>About Me:</b>\n\n"
            "🤖 I’m <b>Rajesh</b> – a custom Telegram bot built for the Double Negative team.\n"
            "🧠 I’m written entirely in <b>Python</b> and deployed directly from an <b>Android device</b> 📱.\n"
            "⚙️ Lightweight, fast, and always ready to assist the team with useful tools, links, and services.\n"
            "🔄 Continuous updates and improvements are on the way!"
        )
    }

    response_text = responses.get(query.data, "❓ Unknown option.")

    # Send a new message with the response text and the same inline buttons
    await context.bot.send_message(
        chat_id=query.message.chat.id,
        text=f"{response_text}\n\n<b>{user_full_name}</b>, what would you like to do next?",
        parse_mode="HTML",
        reply_markup=main_menu()
    )

# === Register Handlers ===
app.add_handler(ChatMemberHandler(welcome_new_member, ChatMemberHandler.CHAT_MEMBER))
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(handle_buttons))

# === Run Bot ===
print("🤖 Rajesh Bot is running...")
app.run_polling()
