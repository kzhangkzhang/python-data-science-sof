# ========================================================
#   File Name   : practice.py
#   Description : Stack Overflow Survey study
#
#   ++++++++++++++++++++++++++++++++++++++++++++++++++++++
#   Date        Who             Description
#   10/18/2019   Kevin Zhang     initial creation
# ========================================================

import csv

with open('survey_results_public.csv', encoding='utf-8') as f:
    # csv_reader is a generator
    csv_reader = csv.DictReader(f)

    yes_count = 0
    no_count = 0

    for line in csv_reader:
        if line['Hobbyist'] == 'Yes':
            yes_count += 1
        elif line['Hobbyist'] == 'No':
            no_count += 1

total = yes_count + no_count
yes_pct = round((yes_count / total) * 100, 2)
no_pct = round((no_count / total) * 100, 2)

print(f'Yes: {yes_pct}%')
print(f'No: {no_pct}%')
