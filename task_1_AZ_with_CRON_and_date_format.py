import requests
import json
import os
import logging
import click
from datetime import datetime

logging.basicConfig(filename='coin_history_app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

@click.command()
@click.option('--iso-date', prompt='Enter date (YYYY-MM-DD)', help='ISO8601 Date in YYYY-MM-DD format')
@click.option('--coin', prompt='Enter coin identifier', help='Coin identifier (e.g., bitcoin)')
def download_coin_history(iso_date, coin):
    try:
        date_obj = datetime.strptime(iso_date, '%Y-%m-%d')
        formatted_date = date_obj.strftime('%d-%m-%Y')
        
        api_url = f"https://api.coingecko.com/api/v3/coins/{coin}/history?date={formatted_date}"
        
        response = requests.get(api_url)
        response.raise_for_status()
        
        data = response.json()
        
        filename = f"{coin}_{formatted_date}.json"
        with open(filename, "w") as file:
            json.dump(data, file)
            print(f"Data saved to {filename}")

        logging.info(f"Data saved to {filename}")
    except (ValueError, requests.exceptions.RequestException) as e:
        logging.error(f"Error: {e}")
        print("Error downloading data.")

if __name__ == "__main__":
    download_coin_history()
