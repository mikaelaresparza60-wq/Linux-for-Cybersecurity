#!/usr/bin/python3
import sys

def grep_stream(pattern, stream):
    for line in stream:
        if pattern in line:
            sys.stdout.write(line)

def grep_file(pattern, file_name):
    try:
        with open(file_name, "r") as f:
            grep_stream(pattern, f)
    except FileNotFoundError:
        sys.stderr.write(f"grep.py: {file_name}: No such file or directory\n")


def main():
    args = sys.argv[1:]

    if not args:
        sys.stderr.write("Usage: grep.py PATTERN [FILE . . .]\n")
        return

    pattern = args[0]
    files = args[1:]
    
    if files:
        for file_name in files:
            grep_file(pattern, file_name)
    else:
        grep_stream(pattern, sys.stdin)

if __name__ == "__main__":
    main()
