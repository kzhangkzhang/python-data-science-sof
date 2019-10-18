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

    # counts = {
    #     'Yes': 0,
    #     'No': 0
    # }

    # Kevin's own
    counts = dict.fromkeys(['Yes', 'No'], 0)

    for line in csv_reader:
        counts[line['Hobbyist']] += 1

total = counts['Yes'] + counts['No']
yes_pct = round((counts['Yes'] / total) * 100, 2)
no_pct = round((counts['No'] / total) * 100, 2)

print(f'Yes: {yes_pct}%')
print(f'No: {no_pct}%')
