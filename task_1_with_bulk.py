import requests
import json
import os
import logging
import click
from datetime import datetime, timedelta

logging.basicConfig(filename='coin_history_app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

@click.command()
@click.option('--iso-date', prompt='Enter date (YYYY-MM-DD)', help='ISO8601 Date in YYYY-MM-DD format')
@click.option('--coin', prompt='Enter coin identifier', help='Coin identifier (e.g. bitcoin)')
@click.option('--bulk-reprocess', is_flag=True, help='Enable bulk data reprocessing')
@click.option('--start-date', help='Start date (YYYY-MM-DD) for bulk reprocessing')
@click.option('--end-date', help='End date (YYYY-MM-DD) for bulk reprocessing')
def download_coin_history(iso_date, coin, bulk_reprocess, start_date, end_date):
    if bulk_reprocess:
        reprocess_data_range(start_date, end_date, coin)
    else:
        fetch_and_store_data(iso_date, coin)

def fetch_and_store_data(iso_date, coin):
    try:
        response = requests.get(f"https://api.coingecko.com/api/v3/coins/{coin}/history?date={iso_date}")
        response.raise_for_status()
        
        data = response.json()
        
        filename = f"{coin}_{iso_date}.json"
        with open(filename, "w") as file:
            json.dump(data, file)
            
        logging.info(f"Data saved to {filename}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error downloading data: {e}")

def reprocess_data_range(start_date, end_date, coin):
    try:
        start_dt = datetime.strptime(start_date, '%Y-%m-%d')
        end_dt = datetime.strptime(end_date, '%Y-%m-%d')
        
        current_dt = start_dt
        while current_dt <= end_dt:
            iso_date = current_dt.strftime('%Y-%m-%d')
            fetch_and_store_data(iso_date, coin)
            current_dt += timedelta(days=1)
    except ValueError as e:
        logging.error(f"Error: {e}")

if __name__ == "__main__":
    download_coin_history()
