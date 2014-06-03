import csv
import operator

from termcolor import colored

SORT_COL_COLOR = 'green'

class CSVSorter():

    def __init__(self, path_to_csv, delimiter=","):
        self.path_to_csv = path_to_csv
        self.delimiter = delimiter

        self.data = []
        self.sort_col = None

        with open(self.path_to_csv, 'rt') as file:
            reader = csv.reader(file, delimiter=self.delimiter, quotechar='|')
            self.data = [row for row in reader]


    def sort(self, sort_col, reverse=False):
        self.data = sorted(self.data, key=operator.itemgetter(sort_col), reverse=reverse)
        self.sort_col = sort_col

        return self


    def print_all(self, sort_col=0, csv_out=False):
        for row in self.data:
            self.print_row(row, sort_col=self.sort_col, csv_out=csv_out)


    def print_row(self, row, sort_col=None, csv_out=False):
        row_str = ""

        spacer = self.delimiter if csv_out else " "

        for col in range(0, len(row)):
            row[col] = str(row[col]).replace(" ", "")

            if (sort_col >= 0) and (col is sort_col):
                row[col] = colored(row[col], SORT_COL_COLOR)

            row_str += (row[col] + spacer if col < (len(row) - 1) else row[col])

        print(row_str)