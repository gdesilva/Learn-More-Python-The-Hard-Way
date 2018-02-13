# Recreating Grep
# Grep searches an input file, and selects lines that match one or more given
# patterns.
#
# By default, a pattern matches an input line
# if the regular expression (RE) in the pattern matches the input line
# without its trailing newline.
#
# It is used for simple patterns and basic regular expressions.


# e.g. if you want to search for the word "help" in a file...
#       grep help *.rst



import argparse
import re
from pathlib import Path

parser = argparse.ArgumentParser()

parser.add_argument('pattern', type=str)
parser.add_argument('path', type=str)

args = parser.parse_args()

def find_line(filename, pattern):
    target_file = open(args.path)
    try:
        lines = target_file.readlines()
    except UnicodeDecodeError:
        print(f"Binary file {name} matches.")
        return

    pattern_obj = re.compile(pattern) # this takes a regex pattern and compiles
                                           # it to an object for reuse
                                           # the responsibility is on the user to
                                           # use regex for their pattern search, rather
                                           # than using plain string plus a flag and
                                           # converting this into the appropriate regex
                                           # (this is more user friendly, and would
                                           # be suitable for a future improvement however)
    for line in lines:
        if pattern_obj.search(line):
            print("The pattern '%s' is identified in: %s" % (args.pattern, lines))
        else:
            print("The pattern '%s' was not identified." % args.pattern)

    target_file.close()


if args.path:
    search_path = Path(args.path[0])
    open_files = search_path.rglob("*") # produces a list of files

    find_line(args.path[0], args.pattern[0])


