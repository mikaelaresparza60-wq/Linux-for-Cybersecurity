#!/usr/bin/python3
import sys

def std_in():
    for line in sys.stdin:
        sys.stdout.write(line)

def infile(file):
        try:
           with open(file, "r") as f:
               for line in f:
                   sys.stdout.write(line)
        except FileNotFoundError:
            sys.stderr.write(f"cat,py: {file}: No such file or directory\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        infile(sys.argv[1])
    else:
        std_in()
