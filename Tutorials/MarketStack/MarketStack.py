import requests
import os
import json

# https://marketstack.com/documentation#python
# https://www.w3schools.com/python/ref_requests_get.asp
def get_data():
    params = {
        'access_key': '0f4688be0bd61dd00a7007682c6cdbe7',
        'symbols': 'aapl'
    }

    # api_result = requests.get('https://api.marketstack.com/v1/tickers/aapl/eod', params)
    api_result = requests.get('api.marketstack.com/v1/eod', params)

    api_response = api_result.json()

    # with open("output.json", "w") as outfile:
    #     json_object = json.dumps(dictionary, indent=4)
    #     outfile.write(api_response)

    for stock_data in api_response['data']:
        print('Ticker {} has a day high of {} on {}'.format(
            stock_data['symbol'],
            stock_data['high'],
            stock_data['low']))


if __name__ == "__main__":
    get_data()