from data.data_fetcher import fetch_historical_data

symbol = "GOOG"
start_date = "2023-01-01"
end_date = "2023-12-31"

data = fetch_historical_data(symbol, start_date, end_date)

print("Fetched Data:")
print(data.head())
print("Columns:", data.columns)