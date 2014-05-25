import csv

class CSVReader:

    def __init__(self):
        pass


    def as_matrix(self, filename, inc_headers=False):
        data = []
        with open(filename, 'rU') as file:
            reader = csv.reader(file, delimiter=',', quotechar='|')
            data = [row for row in reader]

        return data


    def as_dict(self, filename, inc_headers=False):
        with open(filename, 'rU') as file:
            reader = csv.reader(file, delimiter=',', quotechar='|')
            headers = reader.next()

            records = []
            for row in reader:
                dict = {}
                for i in range(len(headers)):
                    dict[headers[i]] = row[i]

                records.append(dict)


        if inc_headers:
            records = headers.extend(records)

        return records


    def headers(self):
        return self.data()[0]