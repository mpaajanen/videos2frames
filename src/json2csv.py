import json
import csv

# load the JSON data
with open('json/labels_12-4.json', 'r') as f:
    data = json.load(f)

# open a new CSV file for writing
with open('json/output.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    # write the header row
    writer.writerow(['LINK', 'LABELS'])

    # iterate over the JSON data
    for item in data:
        # extract the link and labels
        link = item['link']
        labels = ';'.join(item['labels'])

        # write the row to the CSV file
        writer.writerow([link, labels])
