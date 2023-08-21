# Exam_data_ML_Mutt
 Practical tasks for Mutt Data
# Coin History Download App

This Python script allows you to download coin history data from the Coingecko API and store it locally. It also includes proper Python logging and the option to bulk-reprocess data for a specified date range.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/coin-history-app.git

2. Navigate to the project directory:
   ```bash
   cd coin-history-app



Install the required libraries using:
   ```bash
    pip install -r requirements.txt

Usage
Fetch and Store Data

To fetch and store data for a specific date and coin, run the script as follows:

   ```bash


python coin_history_app.py

Follow the prompts to input the ISO8601 date (YYYY-MM-DD) and the coin identifier (e.g., bitcoin). The script will download the data and save it in a local JSON file.
Bulk Reprocess Data

To bulk-reprocess data for a specified date range, use the --bulk-reprocess option along with --start-date and --end-date:

   ```bash


python coin_history_app.py --bulk-reprocess --start-date YYYY-MM-DD --end-date YYYY-MM-DD

Replace YYYY-MM-DD with the desired start and end dates in ISO8601 format. This option allows you to download and store data for multiple days within the specified range.
Logging

The script logs its activities to the coin_history_app.log file. This log file includes timestamps, log levels, and messages related to the data download and any errors that may occur.
CRON Job Setup

To automate the script's execution, you can set up a CRON job to run the script daily at 3am. Open your terminal and enter the following command to edit the CRON table:

   ```bash


crontab -e

Add the following lines to schedule the script for bitcoin, ethereum, and cardano:

cron

0 3 * * * /usr/bin/python3 /path/to/coin_history_app.py --iso-date $(date +\%Y-\%m-\%d) bitcoin
0 3 * * * /usr/bin/python3 /path/to/coin_history_app.py --iso-date $(date +\%Y-\%m-\%d) ethereum
0 3 * * * /usr/bin/python3 /path/to/coin_history_app.py --iso-date $(date +\%Y-\%m-\%d) cardano

Replace /usr/bin/python3 with the actual path to your Python 3 interpreter and /path/to/coin_history_app.py with the actual path to your script on your system.
Disclaimer

This script is provided as a sample for educational purposes. It may require further customization and error handling for production use.

Feel free to customize and extend the script to suit your specific needs.

vbnet


Replace placeholders like `your-username`, `/path/to/python3`, and `/path/to/coin_history_app.py` with the actual paths on your system.

This markdown version should be ready for use in your repository's `README.md` file.

