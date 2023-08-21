import requests
import json
import os
import logging
import click

logging.basicConfig(filename='coin_history_app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

@click.command()
@click.option('--date', prompt='Enter date (DD-MM-YYYY)', help='Date in DD-MM-YYYY format')
@click.option('--coin', prompt='Enter coin identifier', help='Coin identifier (e.g., bitcoin)')
def download_coin_history(date, coin):
    api_url = f"https://api.coingecko.com/api/v3/coins/{coin}/history?date={date}"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        
        data = response.json()
        
        filename = f"{coin}_{date.replace('-', '')}.json"
        with open(filename, "w") as file:
            json.dump(data, file)
            
        logging.info(f"Data saved to {filename}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error downloading data: {e}")

if __name__ == "__main__":
    download_coin_history()
