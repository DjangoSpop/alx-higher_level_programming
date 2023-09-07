#!/usr/bin/python3
from sys import argv

def main():
    num_args = len(argv) - 1
    print(f"{num_args} {'argument' if num_args == 1 else 'arguments'}:")

    for i in range(num_args):
        print(f"{i + 1}: {argv[i + 1]}")

if __name__ == "__main__":
    main()
