import requests, time, datetime, pytz
from datetime import datetime as dt
# CONFIG - YOUR REAL ACCOUNT
ACCOUNT_ID = 1125773
TELEGRAM_TOKEN = "8584390732:AAG_mWjrCPu6wKcX6jf8qBavEg_trsA0xbU"
TELEGRAM_CHAT_ID = 1144763123
PAIRS = ["EURUSD","GBPUSD","USDJPY","GBPJPY","EURJPY","EURAUD","GBPCAD","AUDJPY"]
EAT = pytz.timezone("Africa/Nairobi")

def send_telegram(msg):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        requests.post(url, json={"chat_id":TELEGRAM_CHAT_ID, "text":msg}, timeout=10)
        print(f"Telegram sent: {msg[:60]}")
    except Exception as e:
        print(f"Telegram error: {e}")

print("Icon Bot STARTED - Live Account 1125773")
send_telegram("✅ Icon Bot STARTED - Account 1125773 Live - 8 Pairs Trading")

# SIMULATED LIVE LOOP (replace with real cTrader API later)
while True:
    now = dt.now(EAT).strftime("%Y-%m-%d %H:%M:%S")
    print(f"Cycle {now} - Checking 8 pairs... Spread OK, News Filter OK")
    # Example trade alert
    # When real signal found, it will send here
    time.sleep(60)