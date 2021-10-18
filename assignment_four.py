#By Caleb Beswick, last edited 10/15/21, part of unit four
#Program to give an equation for two random numbers between 5-20

import random


def generating_numbers(maximum, minimum):
    """

    :param maximum: is the maximum number up to 20
    :param minimum: is the minimum number at minimum 1
    :return: returns the number
    """
    if maximum >= 20:
        maximum = 20
    elif minimum <= 5:
        minimum = 5


def num_check():
    """

    :return:
    """
    x = int(input("Please enter a number above 5, but below 20 "))

    if x >= 20:
        return 20
    elif x <= 5:
        return 5
    else:
        return x


def get_sign():
    """

    :return: returns the sign of the equation
    """
    x = input("Please enter the sign ")

    if x == "*":
        return "*"
    elif x == "-":
        return "-"
    else:
        return "+"


def random_number(num1, num2):
    """

    :param num1: The first number used to generate a random number
    :param num2: The second number used to generate a random number
    :return: returns the random number
    """
    if num1 < num2:
        x = random.randint(num1, num2)
    else:
        x = random.randint(num2, num1)
    return x



def getting_sign(sign, ran1, ran2):
    """

    :param sign: the sign of the equation
    :param num1: The first number of the equation
    :param num2: The second number of the equation
    """
    if sign == "*":
        question = ran1 * ran2
        print(ran1, "*", ran2)
    elif sign == "-":
        question = ran1 - ran2
        print(ran1, "-", ran2)

    else:
        question = ran1 + ran2
        print(ran1, "+", ran2)

    answer = int(input("What is the answer? "))
    if answer == question:
        print("You got it right!")
    else:
        print("You are incorrect")


def main():
    sign = get_sign()
    num1 = num_check()
    num2 = num_check()
    ran1 = random_number(num1, num2)
    ran2 = random_number(num1, num2)
    getting_sign(sign, ran1, ran2)


main()
