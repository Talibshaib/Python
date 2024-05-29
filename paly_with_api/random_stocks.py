import requests

URL = 'https://api.freeapi.app/api/v1/public/stocks/stock/random'

def get_random_stocks():
    try:
        response = requests.get(URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(e)
        return None
def main():
    stock = get_random_stocks()
    stock_data = stock['data']
    print('\nStock Details\n' + '-'*15 + '\n')
    print(f"Name: {stock_data['Name']}")
    print(f"Symbol: {stock_data['Symbol']}")
    print(f"ISIN: {stock_data['ISIN']}")
    print(f"Price: {stock_data['CurrentPrice']}")
    print(f"Market Cap: {stock_data['MarketCap']}")
    print(f"Book Value: {stock_data['BookValue']}")
    print(f"Dividend: {stock_data['DividendYield']}")
    print("\n" + '-'*15 + "\n")



if __name__ == '__main__':
    main()