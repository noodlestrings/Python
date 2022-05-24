import csv

from black import NewLine

with open(r'csv\names.csv', 'r') as csvFile:
    csv_reader = csv.DictReader(csvFile)

    # for line in csv_reader:
    #     print(line['email'])

    # newline="" as third parameter stops \n after each line written
    with open(r'csv\new_names.csv', 'r+', newline="") as newFile:
        #fieldnames = ['first_name', 'last_name', 'email']
        fieldnames = ['first_name', 'last_name']

        csv_writer = csv.DictWriter(
            newFile, fieldnames=fieldnames, delimiter=";")

        csv_writer.writeheader()  # writes the field names at the top

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)
