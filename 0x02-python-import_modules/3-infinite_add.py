#!/usr/bin/python3
from sys import argv

def main():
    num_args = len(argv) - 1
    result = 0

    for i in range(num_args):
        result += int(argv[i + 1])

    print(result)

if __name__ == "__main__":
    main()
