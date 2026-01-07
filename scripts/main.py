# !/usr/bin/env python3
# -*- coding: utf-8 -*-


def main_2(value):
    return value * 2


def main_1(name="World"):
    return f"Hello, {name}!"


if __name__ == "__main__":
    data_1_1 = main_1()
    print(data_1_1)
    data_1_2 = main_1("Alice")
    print(data_1_2)
    data_2_1 = main_2()
    print(data_2_1)
    data_2_2 = main_2(10)
    print(data_2_2)
