import requests
import time


coins = ["bitcoin", "ethereum", "solana", "dogecoin", "cardano"]

def get_crypto_price(coin_id):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd&include_24hr_change=true&include_24hr_vol=true"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()[coin_id]
            price = data["usd"]
            change = data["usd_24h_change"]
            volume = data["usd_24h_vol"]

            print(f"\n🪙 {coin_id.upper()}")
            print(f"💰 Price: ${price:,.2f}")
            print(f"📈 24h Change: {change:.2f}%")
            print(f"🔁 24h Volume: ${volume:,.2f}")
        else:
            print(f"❌ Failed to fetch data for {coin_id}")
    except Exception as e:
        print(f"🚫 Error for {coin_id}: {e}")


while True:
    print("===== 📊 LIVE CRYPTO PRICES =====")
    for coin in coins:
        get_crypto_price(coin)
    
    print("\n🔄 Refreshing in 40 seconds...\n")
    time.sleep(40)
