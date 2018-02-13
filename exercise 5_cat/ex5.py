import argparse

parser = argparse.ArgumentParser()

parser.add_argument("files", nargs='*', type=str, help="first file to print or concatenate")

args = parser.parse_args()

print("Your parsed args:  ", args)

file_one_open = open(args.files[0], "r")
#TODO: make this optional and make it so it can take an arbitrary amount of files and open them
file_two_open = open(args.files[1], "r")
file_three_open = open(args.files[2], "r")


#TODO: again, make this loop through all sequentially without explicitly naming each file to print
for line in file_one_open:
    print(line)
for line in file_two_open:
    print(line)
for line in file_three_open:
    print(line)




file_one_open.close()
file_two_open.close()
file_three_open.close()
