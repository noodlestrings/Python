import csv

with open(r'csv\names.csv', 'r') as csvFile:
    csv_reader = csv.reader(csvFile)  # parameter is the file to be read

    # next(csv_reader)  #skips the field declaration line in the csv

    with open(r'csv\new_names.csv', 'r+') as newFile:
        csv_writer = csv.writer(newFile, delimiter=';')

        for line in csv_reader:
            csv_writer.writerow(line)

        # csv_reader = csv.reader(newFile, delimiter=';')
        # for line in csv_reader:
        #     print(line)
