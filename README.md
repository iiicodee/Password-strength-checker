import ccxt
import pandas as pd
from ollama import Client
import time

# --- CONFIGURATION ---
# This is your Mac's address (The Brain)
MAC_IP = "http://10.166.66.25:11434"

# Connect to the Brain
client = Client(host=MAC_IP)

# Connect to Binance (The Market)
exchange = ccxt.binance()

def get_btc_data():
    print(">> Igris is watching the market...")
    # Fetch last 5 hours of Bitcoin data
    ohlcv = exchange.fetch_ohlcv('BTC/USDT', '1h', limit=5)
    
    # Organize the numbers
    df = pd.DataFrame(ohlcv, columns=['time', 'open', 'high', 'low', 'close', 'volume'])
    df['time'] = pd.to_datetime(df['time'], unit='ms')
    
    # Return the clean data as text
    return df.to_string()

def ask_brain(data):
    print(">> Sending data to Mac Mini for analysis...")
    
    prompt = f"""
    You are Project Igris, a ruthless crypto trader.
    Here is the last 5 hours of Bitcoin price action:
    {data}
    
    Analyze the 'close' prices.
    Is the trend BULLISH (going up) or BEARISH (going down)?
    Give me a single signal: BUY or SELL.
    """
    
    try:
        response = client.chat(model='deepseek-r1', messages=[
            {'role': 'user', 'content': prompt}
        ])
        return response['message']['content']
    except Exception as e:
        return f"Error: {e}"

# --- START THE BOT ---
print("⚔️ PROJECT IGRIS: ONLINE ⚔️")

while True:
    # 1. Get Data
    market_data = get_btc_data()
    
    # 2. Analyze
    decision = ask_brain(market_data)
    
    # 3. Print Result
    print("\n" + "="*40)
    print("IGRIS REPORT:")
    print(decision)
    print("="*40 + "\n")
    
    # 4. Wait 30 seconds
    time.sleep(30)
