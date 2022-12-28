#!/usr/bin/env python3

def main():
    try:
        a = float(input("Enter number 1: "))
        b = float(input("Enter number 2: "))

        total = a + b

        if total % 1 == 0:
            total = int(total)

        print(total)

    except ValueError:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    main()
