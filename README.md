📈 ORB Trading Bot
This is an automated Opening Range Breakout (ORB) trading bot built in Python.
It connects to the OANDA API, subscribes to live LTP (Last Traded Price) for selected symbols, calculates opening ranges, and places orders based on ORB breakout strategy.

📜 Features
Fetch live LTP data for multiple symbols

Calculate 15-minute Opening Range (High and Low)

Place Buy/Sell orders based on breakout strategy

Multi-threaded execution for faster handling of symbols

Logging of all activities to logs/bot.log

Modular code structure with OOP principles

🛠 Setup Instructions
  Clone the repository or download the ZIP.

  Navigate into the project folder:

bash
  cd orb_trading_bot
  Install the required dependencies:

bash
  pip install -r requirements.txt
  Set up your OANDA API Credentials:

In oanda_api.py, add your API access_token and account_id where indicated.
Run the bot:

bash
  python main.py

⚙️ Project Structure

orb_trading_bot/
│
├── main.py            # Entry point to start the bot
├── orb_bot.py         # Core trading logic (ORB strategy, threading)
├── oanda_api.py       # API calls for getting LTP and placing orders
├── utils.py           # Helper functions
├── requirements.txt   # Required Python libraries
├── README.md          # Project documentation
├── logs/
│   └── bot.log        # Logs of the bot's actions
└── data/              # (Optional) Data storage

📋 Requirements
Python 3.8+
Packages: requests, threading, logging, etc. (listed in requirements.txt)

🚀 Notes
This bot is designed for educational purposes.
Ensure your OANDA account is set to practice/demo mode for testing.
Always test thoroughly before deploying live.

🔥 Good Luck and Happy Trading!
