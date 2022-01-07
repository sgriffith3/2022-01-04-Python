#!/usr/bin/env python3
## create file object in "r"ead mode

# cfg_file = input("What file do you want to read?\n")
with open(input("What file do you want to read?\n"), "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()

## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)

# Option 1 - 4 lines
count = 0
for item in configlist:
    count += 1
print(f"There are {count} lines in this file")

# Option 2 - 2 lines
num_lines = len(configlist)
print(f"Using the len() function, we see there are: {num_lines} lines")

# Option 3 - 1 line
print(f"On a single line, using len() function, we find there are {len(configlist)} lines")
