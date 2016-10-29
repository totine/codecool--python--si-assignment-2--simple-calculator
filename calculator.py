# simple calculator

import sys


# constants

OPERATORS = "+-*/"
LETTERS = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż"


# input functions

def input_first_number():
    first_number=input("Enter a number (or a letter to exit): ")
    if first_number in LETTERS and first_number != "":
        end_program()
    else:
        while 1:
            try:
                type(int(first_number)) == int
                break
            except:
                print("It isn't an integer or a letter")
                first_number=input("Enter a number (or a letter to exit): ")
                if first_number in LETTERS and first_number != "":
                    end_program()
        first_number=int(first_number)
        return first_number


def input_operator():
    operator=input("Enter an operation: ")
    while operator not in OPERATORS or operator == "":
        print("It isn't correct operator")
        operator=input("Enter an operation: ")
    return operator


def input_second_number(if_divide):
    second_number=input("Enter another number: ")
    if if_divide == "/" and second_number=="0":
        while second_number=="0":
            print("Don't divide by 0!")
            second_number=input("Enter another number: ")
    else:
        while 2:
            try:
                type(int(second_number)) == int
                break
            except:
                print("It isn't an integer")
                second_number=input("Enter another number one more time: ")
        second_number=int(second_number)
        return second_number


# end program function

def end_program():
    sys.exit("See you next time")


# definitions of mathematic calculation

def addition(a, b):
    sum_ab = a + b
    return sum_ab

def subtraction(a, b):
    diff_ab = a - b
    return diff_ab

def multiplication(a, b):
    product_ab = a * b
    return product_ab

def division(a, b):
    if b == 0:
        print("Can't divide by 0")
        end_program()
    else:
        quotient_ab = a / b
        return quotient_ab


#function, which chooses a mathematical operation

def which_operation(operator, first_number, second_number):
    if operator == "+":
        result = addition(first_number, second_number)
        return result
    elif operator == "-":
        result = subtraction(first_number, second_number)
        return result
    elif operator == "*":
        result = multiplication(first_number, second_number)
        return result
    elif operator == "/":
        result = division(first_number, second_number)
        return result


# main function

def main():

    first_number = input_first_number()
    operator = input_operator()
    second_number = input_second_number(operator)
    result = which_operation(operator, first_number, second_number)

    print(result)

main()
