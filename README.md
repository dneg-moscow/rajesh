# 🤖 Rajesh – Double Negative Telegram Bot

Rajesh is the official Telegram bot for the **Double Negative** team. Built with Python, it lives inside our team’s Telegram group, offering helpful interactions, updates, and automation to make internal collaboration smoother.

This bot automatically welcomes new members with a time-based greeting and introduces itself. Team members can also interact with Rajesh using the `/start` command and inline buttons.

---

## 🚀 Features

- ✅ Greets new members based on the time of day (Good Morning, Afternoon, etc.)
- ✅ First-time welcome message with a personal touch
- ✅ `/start` command to quickly re-engage the bot
- ✅ Interactive buttons for:
  - 🌐 Website
  - 💻 Code (GitHub)
  - ℹ️ About Me
- ✅ Simple spam handling (can be expanded)

---

## 🔧 Setup Instructions

### 1. Clone the Repository

To clone the repository to your local machine, run:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
````

### 2. Install Required Packages

Use `pip` to install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` File

In the root of the project directory, create a file named `.env`:

```
BOT_TOKEN=your-telegram-bot-token-here
```

You can get this token from [@BotFather](https://t.me/botfather) on Telegram.

### 4. Run the Bot

```bash
python rajesh_bot.py
```

---

## ℹ️ About Me (The Bot)

Rajesh is written in **Python** and hosted on an **Android device** using a lightweight deployment setup. It uses the `python-telegram-bot` library for handling updates, user events, and inline buttons.

---

## 🌐 Useful Links

* Website: [https://doublenegative.online](https://doublenegative.online)
* GitHub: [https://github.com/dneg-moscow](https://github.com/dneg-moscow)

---

## 🛡️ Security Note

⚠️ **NEVER** hardcode your token in code. Always use `.env` to store sensitive information, and ensure `.env` is in your `.gitignore`.

---

## 🧑‍💻 Author

Maintained by the Double Negative Team. For issues or contributions, feel free to fork and create a pull request.

```
```
