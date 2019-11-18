#!/usr/bin/env python3

# Created by: Evano Fotia
# Created on: oct 2019
# this program guesses the number


import constants


def main():
    # Its guessing the number

    # input
    guessed_number = int(input("Enter your guess (0 to 9): "))
    print("")

    # Process
    if guessed_number == constants.CORRECT_NUMBER:
        # Output
        print("Correct")


if __name__ == "__main__":
    main()
