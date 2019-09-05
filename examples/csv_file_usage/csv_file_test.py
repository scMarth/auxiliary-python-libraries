import sys, os
sys.path.insert(0, os.path.dirname(__file__) + '/../../')

import csv_file

example_csv_file = csv_file.CsvFile(os.path.dirname(__file__) + "/test_csv.csv", 5)

example_csv_file.validate_records()

example_csv_file.check_for_special_characters()

for i in range(0,6):
    for j in range(0,5):
        print(example_csv_file.csv_array[i][j])
    print("")