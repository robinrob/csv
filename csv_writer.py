class CSVWriter():

    def __init__(self):
        pass


    def write(self, data, filename, separator=','):
        file = open(filename, 'w')
        for line in data:
            file.write(','.join(line) + '\n')

        file.close()

        return file
