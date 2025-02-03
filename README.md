# Pi Zero Live Tweet Display

A compact, real-time Twitter feed display using a **Raspberry Pi Zero** and an **SPI OLED/LCD screen**. This project helps you stay updated with live tweets while working, without needing to check your phone.

---

## ✨ Features
- **Live Twitter Feed** – Displays tweets as soon as they arrive.
- **Compact & Always-On** – Sits on your desk for quick updates.
- **Easy Setup** – Simple Python script with minimal dependencies.
- **Customizable** – Filter tweets by hashtags, mentions, or specific accounts.

---

## 🛠️ Hardware Requirements
- **Raspberry Pi Zero (or any Raspberry Pi)**
- **SPI Display** (e.g., SSD1306 OLED, ST7789 LCD)
- **MicroSD Card (with Raspberry Pi OS)**
- **Wi-Fi Connection**
- **Power Supply**

---

## 🖥️ Software Requirements
- **Raspberry Pi OS (Lite recommended)**
- **Python 3**
- **Tweepy** (Twitter API library)
- **Adafruit CircuitPython Libraries** (for SPI display)

Install dependencies:
```bash
sudo apt update && sudo apt upgrade -y
pip3 install tweepy adafruit-circuitpython-ssd1306
```

---

## 🔑 Twitter API Setup
1. Sign up at [Twitter Developer Portal](https://developer.twitter.com/).
2. Create a new app and get API keys.
3. Enable **Read-Only Access**.
4. Store the API keys in your script.

---

## 🚀 Installation & Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/pi-tweet-display.git
   cd pi-tweet-display
   ```
2. Add your Twitter API keys in `config.py`:
   ```python
   API_KEY = "your-api-key"
   API_SECRET = "your-api-secret"
   ACCESS_TOKEN = "your-access-token"
   ACCESS_SECRET = "your-access-secret"
   ```
3. Run the script:
   ```bash
   python3 twitter_display.py
   ```
4. To run on startup:
   ```bash
   crontab -e
   ```
   Add this line:
   ```
   @reboot python3 /home/pi/pi-tweet-display/twitter_display.py &
   ```

---

## 🛠️ Customization
- Change the tweet source (timeline, hashtags, or user mentions).
- Adjust the display settings (font size, scroll speed, etc.).
- Use a different SPI display (modify display driver accordingly).

---

## 📷 Example Setup
*Coming soon: Photos of the setup and working display!*

---

## 📜 License
This project is open-source under the **MIT License**.

---

## 🤝 Contributions
Pull requests are welcome! Feel free to fork and improve the project.

---

### 🚀 Enjoy your live tweet display! 🎉

