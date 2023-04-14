# Домашнее задание  №5

import json
import csv
import re

debtors_data = []
with open("traders.txt") as file:
    for line in file:
        debtors_data.append([x for x in line.split()])

for i in range(len(debtors_data)):
    debtors_data[i] = debtors_data[i][0]

with open("efrsb_1000.json") as f:
    data_json = json.load(f)

listCSV = []
for j in range(len(debtors_data)):
    INN = debtors_data[j]
    for i in range(len(data_json)):

        if "debtor_inn" in data_json[i] and "debtor_ogrn" in data_json[i]: #and INN == data_json[i]['debtor_inn']
            listCSV.append({'INN': data_json [i] ['debtor_inn'], 'OGRN': data_json[i]["debtor_ogrn"]})

with open('traders.csv', 'w', newline='') as csvFile:
    wr = csv.DictWriter(csvFile, delimiter = ';', fieldnames = ['INN', 'OGRN'])
    wr.writeheader()
    for i in listCSV:
        wr.writerow(i)

def find_emails(text):
    lst = re.findall('\S+@\S+', text)
    return lst

with open('efrsb.json') as file:
    emails_list = json.load(file)

dictionary_emails = {}

for i in range(len(emails_list)):
    emails_set = set(find_emails(emails_list[i]['msg_text']))
    if emails_set != set():
        dictionary_emails[str(emails_list[i]['publisher_inn'])] = emails_set

with open('emails.json', 'w') as outfile:
    json.dump(dictionary_emails, outfile, default=list)