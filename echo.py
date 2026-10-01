#!/usr/bin/python3
import sys

def main():
    args = sys.argv[1:]

    output = " ".join(args)

    sys.stdout.write(output + "\n")

if __name__ == "__main__":
    main()
