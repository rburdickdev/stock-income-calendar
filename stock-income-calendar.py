import requests

def get_data(api_key, url):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad responses

        # Assuming the response is in JSON format
        json_response = response.json()

        return json_response

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

symbol = input("Enter a Ticker Symbol: ")
api_key = 'SYCORXKZW2OC5QIM'
overview_api_url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol='+symbol+'&apikey='+api_key
quote_api_url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol='+symbol+'&apikey='+api_key

overview_data = get_data(api_key, overview_api_url)
quote_data = get_data(api_key, quote_api_url)

if overview_data:
    print("----- Overview Data -----")
    print(overview_data)

if quote_data:
    print("----- Quote Data -----")
    print(quote_data)
