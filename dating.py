#!/usr/bin/env python3
# Created by: Samuel Nkongolo
# Created on: Oct 24
# This program checks if a user is eligible to date someone's grandchild.


def main():
    romance = True
    while romance == True:
        # input
        user_age = input("What is the user age?: ")
        # process and output
        try:
            int_user_age = int(user_age)
            # Checks if user is 25-39
            if int_user_age >= 25 and int_user_age < 40:
                print("You can date Grandma Babushka's grandchild")
                romance = False
                # Breaks the sad news to the user.
            else:
                print("You are not in the right demographic.")
        except Exception:
            print("Invalid age")
            romance = False


if __name__ == "__main__":
    main()