# !/usr/bin/env python3
# -*- coding: utf-8 -*-


def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


if __name__ == "__main__":
    test_number = 5
    result = even_or_odd(test_number)
    print(f"The number {test_number} is {result}.")
