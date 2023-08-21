import requests
import json
import os

def download_coin_history(date, coin_id):
    api_url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/history?date={date}"

    
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        
        filename = f"{coin_id}_{date}.json"
        with open(filename, "w") as file:
            json.dump(data, file)
            
        print(f"Data saved to {filename}")
    else:
        print("Error downloading data.")

if __name__ == "__main__":
    input_date = input("Enter date (YYYY-MM-DD): ")
    coin_id = input("Enter coin identifier: ")
    
    download_coin_history(input_date, coin_id)
