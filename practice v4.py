# ========================================================
#   File Name   : practice.py
#   Description : Stack Overflow Survey study
#
#   ++++++++++++++++++++++++++++++++++++++++++++++++++++++
#   Date        Who             Description
#   10/18/2019   Kevin Zhang     initial creation
# ========================================================

# LanguageWorkedWith

import csv
from collections import defaultdict, Counter

with open('survey_results_public.csv', encoding='utf-8') as f:
    # csv_reader is a generator
    csv_reader = csv.DictReader(f)

    language_counter = Counter()

    total = 0

    for line in csv_reader:
        languages = line['LanguageWorkedWith'].split(';')
        language_counter.update(languages)
        total += 1


print(total)
print(language_counter.most_common(5))

# language_counter.most_common(5) returns list of tuple
# the tuple likes ('JavaScript', 59219)
for language, value in language_counter.most_common(5):
    language_pct = round((value / total) * 100, 2)
    print(f'{language}: {language_pct}%')
