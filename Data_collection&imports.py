import os;os.system('cls')
"""
testing time 
"""
import requests
import pandas as pd
url ="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&outputsize=full&apikey=demo"
all_data=[]# used to save all the value gain access from API
response = requests.get(url)
data = response.json()
if "Time Series (Daily)" in data:
    time_series = data["Time Series (Daily)"]

    for date, values in time_series.items():
            stock_data = {
                "Symbol": "IBM",
                "Date": date,
                "Open": float(values["1. open"]),
                "High": float(values["2. high"]),
                "Low": float(values["3. low"]),
                "Close": float(values["4. close"]),
                "adjusted close": float(values["5. adjusted close"]),
                "Volume": int(values["6. volume"]),
                "dividend amount": float(values["7. dividend amount"]),
                "split coefficient": float(values["8. split coefficient"])
            }

            all_data.append(stock_data)

    print(f" Collected {len(all_data)} days of data for IBM")

else:
        print(f"Failed : {data.get('Note', 'Invalid response')}")

# Conversion
df = pd.DataFrame(all_data)
# Save to CSV file
df.to_excel("Stocks_after_every_5min.xlsx", index=False)
print("\n Successfully collection")
print(df.head())