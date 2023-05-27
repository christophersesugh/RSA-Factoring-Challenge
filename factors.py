import sys
import signal
from factorize import factorize

if len(sys.argv) < 2:
    print("USAGE: factors <file>")
    sys.exit(1)

def timeout_handler(signum, frame):
    print("Timeout: Program execution exceeded the time limit")
    sys.exit(1)

file_name = sys.argv[1]

try:
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(5)

    with open(file_name, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.rstrip('\n')
        try:
            number = int(line)
            factorize(number)
            signal.alarm(0)
        except ValueError:
            print("Invalid number: ", line)

except FileNotFoundError:
    print("File not found: ", file_name)
