import argparse

# This script is a simple little addition calculator tool for the command line

parser = argparse.ArgumentParser()

# flags - verbosity, pirate verbosity, friendliness (adds a :) )
parser.add_argument("-v", "--verbose", help="adds more decription to the function",
                    action="store_true")
parser.add_argument("-pv", "--pverbose", help="adds ye scrawlin to ye functioner",
                    action="store_true")
parser.add_argument("-f", "--friendliness", help="brightens your day",
                    action="store_true")


# arguments - numbers to add.
parser.add_argument("number_one", type=int, help="first number to add")
parser.add_argument("number_two", type=int, help="second number to add")
parser.add_argument("number_three", type=int, help="third number to add")

args = parser.parse_args()
answer = args.number_one + args.number_two + args.number_three

if args.verbose:
    print("{} plus {} plus {} equals {}".format(args.number_one, args.number_two, args.number_three, answer))

if args.pverbose:
    print("{} added to ye {} and {} makes ye a total er {}".format(args.number_one, args.number_two, args.number_three, answer))

if args.friendliness:
    print("{}  :)".format(answer))

else:
    print(answer)
