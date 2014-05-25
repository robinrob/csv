#!/usr/bin/env python

from csv_generator import CSVGenerator
from csv_writer import CSVWriter
from csv_reader import CSVReader

data = CSVReader().as_dict(CSVWriter().write(CSVGenerator().generate(10, 10), 'file.txt').name)

print(str(data))