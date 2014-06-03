#!/usr/bin/python3

import sys
import argparse

from csv_sorter import CSVSorter

parser = argparse.ArgumentParser(description='Sort a CSV file.')

parser.add_argument('file', metavar='file', type=str,
                    help='CSV file')

parser.add_argument('column', metavar='column', type=int,
                    help='sorting column')

parser.add_argument("--delimiter", "-d", type=str, default=",",
                    help="field delimiter")

parser.add_argument("--reverse", "-r", action="store_true", default=False,
                    help="reverse sort")

parser.add_argument("--csv", action="store_true", default=None,
                    help="format output as CSV")

args = parser.parse_args()

CSVSorter(args.file, args.delimiter).sort(sort_col=args.column, reverse=args.reverse).print_all(csv_out=args.csv)