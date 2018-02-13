# this script replicates some basic core functionality of the 'find' command line
# function.
# What it should do:
    # 1. specify the directory to start searching in: . or /usr/local/.
    # 2. A filter argument like -name or -type d (files of type directory)
    # 3. An action to do with each found file: -print, and -exec are essential
        # exec
    # ex: find . −name ”*.txt” −print

import argparse
import glob
import subprocess

parser = argparse.ArgumentParser()

# parser.add_argument('start', type=str)
# NOTE: This doesn't really do anything at the moment. Could refactor so that it uses Zed's
# format but there doesn't seem to be much advantage to it
parser.add_argument('-file', type=str, nargs='*', required=False,
                    help="""
                    This will take in a file, a directory and file,
                    or just a directory, and either print or pass to the exec function.
                    Wildcards are supported in the file function.
                    """)
# parser.add_argument('-print', action='store_true')
parser.add_argument('-exec', nargs='*', required=False)
#TODO: Add to help what exec does


args = parser.parse_args()

file_list = []

if args.file:
    for f in args.file:
        file_list.append(f)
else:
    file_list.append(args.start)


if args.exec:
    exec_args = ' '.join(args.exec)

print("\n")
print("Your args are: %s" % args)
print("Your file(s) is/are: %s" % args.file)
print("Your path is: %s" % args.start)


# TODO: Not needed...? Currently print does nothing. Can use cat in exec instead.
# if args.print == True:
#     print("Your path and file is: %s" % find)


if args.exec:
    print("You are running the following subprocess on this path: %s" % exec_args)
    print("---- OUTPUT ----")
    for a in file_list:
        print(">> Running %s on %s" % (exec_args, a))
        subprocess.run([exec_args, a])
        print("\n")
