#!/usr/bin/env python3
# Created By: Victor Victor-Calixte
# Date: 11/24/26
# This program prints numbers 1000 - 2000, with every multiple of 5, starting a new line.


def main():

    for counter in range(1000, 2001):
        # Checking if the counter is a multiple of 5. If it is, then start a new line
        # Otherwise, continue that line
        if (counter + 1) % 5 == 0:
            print(counter, " ")
        else:
            print(counter, end=" ")


if __name__ == "__main__":
    main()
