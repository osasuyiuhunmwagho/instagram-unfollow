## 🌟 Instagram Unfollow Bot

## 🚀 Overview

Welcome to the **Instagram Unfollow Bot**! 🎉 This Python-based bot uses Selenium to help you automate the process of unfollowing users on Instagram. Whether you're cleaning up your followers list or just experimenting with automation, this bot is here to make things easier.

> **Note:** The bot is a work in progress! It currently navigates to the followers path but doesn't yet store the followers or unfollowers lists.

---

## ✨ Features

- 🔐 **Automates Login**: Securely log in to Instagram using your credentials.
- 📂 **Path Navigation**: Automatically navigate to followers and following paths.
- 📫 **Inbox Navigation**: Quickly navigate to the Instagram inbox.
- ⚡ **Performance Optimizations**: Headless mode, eager page load strategy, disabled images, and explicit waits for faster and more reliable runs.
- 🛠️ **Built with Selenium**: Enjoy seamless browser automation.

---

## 📋 Requirements

- **Python**: Version 3.8 or higher.
- **Google Chrome** (or any Chromium variant compatible with ChromeDriver).

---

## 🛠️ Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/instagram-unfollow-bot.git
   cd instagram-unfollow-bot
   ```

2. **Install dependencies**:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. (Optional) **Use a local ChromeDriver**:
   - Set `CHROMEDRIVER_PATH` in your environment to use an existing driver and avoid downloads.
   - Otherwise, the script will use `webdriver-manager` (cached) to provision the correct driver.

---

## ⚙️ Configuration

Create a `.env` file (or set environment variables) using the template below:

```env
USERNAME=your_instagram_username
PASSWORD=your_instagram_password
HEADLESS=true
DISABLE_IMAGES=true
PAGE_LOAD_STRATEGY=eager
EXPLICIT_WAIT_SECONDS=20
# Optional: CHROMEDRIVER_PATH=/usr/local/bin/chromedriver
```

> Tip: Keep `.env` out of version control. This repo includes a `.gitignore` entry for it.

---

## ▶️ Usage

Run the bot:

```bash
python navigateToinbox.py
```

---

## ⚠️ Current Limitations
- 🛑 The bot does not yet store or process the lists of followers and unfollowers.
- 📉 Error handling and rate-limiting protections need enhancement.

---

## 🌟 Planned Features
- 💾 Store followers and unfollowers lists.
- 📊 Track changes in followers over time.
- 🔍 Add criteria-based unfollow logic.
- 🧰 Enhance error handling and logging.
- 🕶️ Support for advanced headless evasion techniques.

---

## 🤝 Contributing
We love contributions!
If you have ideas, suggestions, or want to report bugs, feel free to:

- Open an issue 📢
- Submit a pull request 🚀

Let’s build something amazing together! 💪

