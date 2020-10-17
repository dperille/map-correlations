import csv
import json

INPUT_FILE_NAME = './data/world-country/world-country-population.csv'
OUTPUT_FILE_NAME = './world-country_population-json.json'
METRIC_NAME = 'population'
COL_START = 4
INDENT = 4

data = {}

with open(INPUT_FILE_NAME) as csv_file:
    reader = csv.reader(csv_file)
    headers = next(reader)
    
    for row in reader:
        entry = {
            METRIC_NAME: {

            }
        }

        for i in range(COL_START, len(row)):
            try:
                entry[METRIC_NAME][headers[i]] = int(row[i])
            except:
                entry[METRIC_NAME][headers[i]] = None

        data[row[0]] = entry

with open(OUTPUT_FILE_NAME, 'w') as outfile:
    json.dump(data, outfile, indent=INDENT)