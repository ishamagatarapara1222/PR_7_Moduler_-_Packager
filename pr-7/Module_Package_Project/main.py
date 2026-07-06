"""
Multi-Utility Toolkit
PR.7 - Moduler & Packager
"""

import sys
import os

# Make sure project root is in path
sys.path.insert(0, os.path.dirname(__file__))

import modules.datetime_utils as dt_utils
import modules.math_utils as math_utils
import modules.random_utils as rand_utils
import modules.uuid_utils as uuid_utils
import modules.file_utils as file_utils
from package.module import explore_module


SEP = "-" * 26


def print_sep():
    print(SEP)


# ─── Sub-menus ───────────────────────────────────────────────────────────────

def datetime_menu():
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ").strip()
        print_sep()

        if choice == "1":
            dt_utils.display_current_datetime()
        elif choice == "2":
            d1 = input("Enter the first date (YYYY-MM-DD): ").strip()
            d2 = input("Enter the second date (YYYY-MM-DD): ").strip()
            dt_utils.calculate_difference(d1, d2)
        elif choice == "3":
            d = input("Enter date (YYYY-MM-DD): ").strip()
            fmt = input("Enter custom format (e.g. %d/%m/%Y): ").strip()
            dt_utils.format_date(d, fmt)
        elif choice == "4":
            dt_utils.stopwatch()
        elif choice == "5":
            secs = int(input("Enter countdown seconds: ").strip())
            dt_utils.countdown_timer(secs)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Try again.")
        print_sep()


def math_menu():
    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ").strip()
        print_sep()

        if choice == "1":
            n = int(input("Enter a number: ").strip())
            math_utils.calculate_factorial(n)
        elif choice == "2":
            p = float(input("Enter principal amount: ").strip())
            r = float(input("Enter rate of interest (in %): ").strip())
            t = float(input("Enter time (in years): ").strip())
            math_utils.compound_interest(p, r, t)
        elif choice == "3":
            angle = float(input("Enter angle in degrees: ").strip())
            math_utils.trigonometric_calculations(angle)
        elif choice == "4":
            shape = input("Enter shape (circle/rectangle/triangle): ").strip()
            if shape.lower() == "circle":
                r = float(input("Enter radius: ").strip())
                math_utils.area_of_shapes(shape, r)
            elif shape.lower() == "rectangle":
                l = float(input("Enter length: ").strip())
                w = float(input("Enter width: ").strip())
                math_utils.area_of_shapes(shape, l, w)
            elif shape.lower() == "triangle":
                b = float(input("Enter base: ").strip())
                h = float(input("Enter height: ").strip())
                math_utils.area_of_shapes(shape, b, h)
            else:
                print("Unknown shape.")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")
        print_sep()


def random_menu():
    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ").strip()
        print_sep()

        if choice == "1":
            s = int(input("Enter start range: ").strip())
            e = int(input("Enter end range: ").strip())
            rand_utils.generate_random_number(s, e)
        elif choice == "2":
            count = int(input("Enter how many numbers: ").strip())
            s = int(input("Enter start range: ").strip())
            e = int(input("Enter end range: ").strip())
            rand_utils.generate_random_list(count, s, e)
        elif choice == "3":
            length = int(input("Enter password length: ").strip())
            rand_utils.create_random_password(length)
        elif choice == "4":
            digits = int(input("Enter OTP digits (default 6): ").strip() or "6")
            rand_utils.generate_otp(digits)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")
        print_sep()


def uuid_menu():
    while True:
        print("\nGenerate Unique Identifiers (UUID):")
        print("1. Generate Single UUID")
        print("2. Generate Multiple UUIDs")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ").strip()
        print_sep()

        if choice == "1":
            uuid_utils.generate_uuid()
        elif choice == "2":
            count = int(input("Enter how many UUIDs to generate: ").strip())
            uuid_utils.generate_multiple_uuids(count)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")
        print_sep()


def file_menu():
    while True:
        print("\nFile Operations (Custom Module):")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ").strip()
        print_sep()

        if choice == "1":
            fname = input("Enter file name: ").strip()
            file_utils.create_file(fname)
        elif choice == "2":
            fname = input("Enter file name: ").strip()
            data = input("Enter data to write: ").strip()
            file_utils.write_to_file(fname, data)
        elif choice == "3":
            fname = input("Enter file name: ").strip()
            file_utils.read_from_file(fname)
        elif choice == "4":
            fname = input("Enter file name: ").strip()
            data = input("Enter data to append: ").strip()
            file_utils.append_to_file(fname, data)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")
        print_sep()


def explore_dir_menu():
    while True:
        print("\nExplore Module Attributes (dir()):")
        mod_name = input("Enter module name to explore (math/random/datetime/uuid): ").strip()
        print_sep()
        explore_module(mod_name)
        print_sep()
        again = input("Explore another module? (y/n): ").strip().lower()
        if again != "y":
            break


# ─── Main Menu ───────────────────────────────────────────────────────────────

def main():
    while True:
        print("\nMenu:")
        print("=" * 26)
        print("Welcome to Multi-Utility Toolkit")
        print(SEP)
        print("Choose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")
        print(SEP)
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            datetime_menu()
        elif choice == "2":
            math_menu()
        elif choice == "3":
            random_menu()
        elif choice == "4":
            uuid_menu()
        elif choice == "5":
            file_menu()
        elif choice == "6":
            explore_dir_menu()
        elif choice == "7":
            print("\nExit:")
            print('\n"Quality is our Motto."')
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
