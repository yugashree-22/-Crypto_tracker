from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd
import time
from datetime import datetime

# Chrome Driver Setup
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

# Open CoinMarketCap
driver.get("https://coinmarketcap.com/")

# Wait for page load
time.sleep(5)

crypto_data = []

# Get table rows
rows = driver.find_elements(By.TAG_NAME, "tr")

# Top 10 coins
for row in rows[1:11]:
    try:
        cols = row.find_elements(By.TAG_NAME, "td")

        coin_name = cols[2].text
        price = cols[3].text
        change_24h = cols[4].text
        market_cap = cols[7].text

        crypto_data.append({
            "Timestamp": datetime.now(),
            "Coin": coin_name,
            "Price": price,
            "24h Change": change_24h,
            "Market Cap": market_cap
        })

    except:
        pass

# Close browser
input("Press Enter to close browser...")



# Create DataFrame
df = pd.DataFrame(crypto_data)

# Save CSV
df.to_csv("crypto_data.csv", index=False)

print(df)

print("\nData saved successfully!")