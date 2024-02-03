import requests
import matplotlib.pyplot as plt
from key import AlphaVantageKEY

def main():
    url = "https://www.alphavantage.co/query"
    # symbol = input("Enter a stock symbol: ")
    # response = requests.get(url, params={
    #     "function": "TIME_SERIES_DAILY",
    #     "symbol": "IBM",
    #     "outputsize": "full",
    #     "apikey": AlphaVantageKEY
    # })
    response = requests.get(url, params={
        "function": "TIME_SERIES_DAILY",
        "symbol": "IBM",
        "outputsize": "full",
        "apikey": "demo"
    })
    data = response.json()
    closing_prices = [float(data["Time Series (Daily)"][date]["4. close"]) for date in data["Time Series (Daily)"]]
    dates = list(data["Time Series (Daily)"].keys())
    plt.plot(dates, closing_prices)
    # plt.title(f"{symbol} Stock Price")
    plt.title("IBM Stock Price")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.xticks(rotation=45)
    plt.show()
    
    

if __name__ == "__main__":
    main()
