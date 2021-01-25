import csv
import collections

occurrence = collections.Counter()
with open("alcohol-available-for-consumption-year-ended-december-2019-csv.csv", newline="") as f:
    file_reader = csv.DictReader(f, delimiter=",")
    count = 0
    for line in file_reader:
        if line["MAGNITUDE"] == '0':
            count += 1
    print(count)
