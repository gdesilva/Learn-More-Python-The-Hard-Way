import argparse
from pathlib import Path


parser = argparse.ArgumentParser()

parser.add_argument('-d', nargs='?')
parser.add_argument('-f', nargs='?', type=int)
parser.add_argument('path', nargs='*') #TODO: default to standard input

args = parser.parse_args()

# Thiss bring in an input file
# TODO: handle more than one path/file at a time
target_file = open(args.path[0])
lines = target_file.readlines() #list of lines in lines

# This cuts a line by the delimiter
def print_lines():
    try:
        for line in lines:
            split_lines = line.split(args.d)
            #print the lines according to the field numbers
            #just handle a single field, then do comma separated fields, then ranges - these
            #when input raw are not integers - we need to convert them to integers
            print(split_lines[args.f])
    except IndexError:
        pass

print_lines()
