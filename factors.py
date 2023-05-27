import sys

from factorize import factorize

if len(sys.argv) < 2:
    print("USAGE: factors <file>")
    sys.exit(1)

file_name = sys.argv[1]

try:
    with open(file_name, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.rstrip('\n')
        try:
            number = int(line)
            factorize(number)
        except ValueError:
            print("Invalid number: ", line)

except FileNotFoundError:
    print("File not found: ", file_name)
