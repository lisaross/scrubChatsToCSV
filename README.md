# Scrub Chats to CSV

`scrubAllToCSV.py` is a Python script that processes Zoom chat transcripts, anonymizing the data by stripping names and compiling the messages into a CSV file. This tool is designed to help you analyze Zoom chat data while respecting the privacy of the participants.

The CSV file output includes columns for the timestamp of the message, the message itself, as well as the company, program, cohort, and session the chat came from.

## Prerequisites

You will need Python 3 installed on your machine. 

## Usage

1. Save your Zoom chat transcripts as `.txt` files. Ensure each file is named using the following format: `company-program-cohort-session.txt`, where:
   - `company` represents the company's name
   - `program` represents the program's code
   - `cohort` represents the cohort number
   - `session` represents the session number

   An example of a valid filename would be `mcdonalds-1on1trial-001-01.txt`.

2. Place the `scrubAllToCSV.py` script in the same directory as your chat transcripts.

3. Run the script from the command line, providing the name of the output CSV file as a command-line argument. For example, if you want the output file to be named `output.csv`, you would run:

   ```bash
   python scrubAllToCSV.py output.csv

The script will process all .txt files in the directory, stripping the names from the chat, and compiling the remaining data into the output CSV file.

### Important Note on Privacy

This script is designed to help respect participant privacy by removing personal identifiers from chat transcripts. However, always be aware of additional steps you may need to take to ensure compliance with privacy laws and regulations, especially when dealing with sensitive information.
