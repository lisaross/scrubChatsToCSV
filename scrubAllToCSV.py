import os
import csv
import sys
import re
import glob

def parse_line(line):
    timestamp, rest = line.split('From', 1)
    message = re.search(r".*:(.*)", rest)

    if message:
        message = message.group(1).strip()
    else:
        message = ''
    
    return timestamp.strip(), message.strip()

def convert_file_to_csv(input_file_name, output_file_name):
    filename = os.path.splitext(os.path.basename(input_file_name))[0]
    company, program, cohort, session = filename.split('-')

    with open(input_file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(output_file_name, 'a', newline='', encoding='utf-8') as f:
        fieldnames = ['timestamp', 'message', 'company', 'program', 'cohort', 'session']
        writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        if f.tell() == 0:
            writer.writeheader()

        timestamp = message = ''
        messages = []
        for line in lines:
            if 'From' in line:
                if messages:
                    writer.writerow({'timestamp': timestamp, 'message': ' '.join(messages).strip(), 'company': company, 'program': program, 'cohort': cohort, 'session': session})
                    messages = []
                
                timestamp, message = parse_line(line)
                messages.append(message)
            elif line.strip():
                messages.append(line.strip())

        if messages:
            writer.writerow({'timestamp': timestamp, 'message': ' '.join(messages).strip(), 'company': company, 'program': program, 'cohort': cohort, 'session': session})

def main():
    if len(sys.argv) != 2:
        print("Usage: python scrubAllToCSV.py <outputfile.csv>")
        sys.exit(1)

    output_file = sys.argv[1]

    if os.path.isfile(output_file):
        os.remove(output_file)

    for file_name in glob.glob('*.txt'):
        convert_file_to_csv(file_name, output_file)

if __name__ == "__main__":
    main()
