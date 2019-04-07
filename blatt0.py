import math
import scipy.special


def is_palindrome(s):
    return s == s[::-1]


def flatten(n):
    result = []
    if isinstance(n, list):
        for i in n:
            print(i)
            result = result + i
        return result
    return n


def print_pascal(depth):
    result = []
    for i in range(depth):
        result = result + [print_pascal_it(i)]
    return result

def print_pascal_it(depth):
    result = []
    for i in range(depth+1):
        result = result + [scipy.special.binom(depth, i)]
    return result


def solve_equation(a, b, c):
    if a > 1:
        return solve_equation(a / a, b / a, c / a)
    if a == 0:
        raise ValueError("Not a quadratic equation")
    if a < 0:
        return solve_equation(a / a, b / a, c / a)
    first = - b / 2
    second = ((b / 2) ** 2) - c
    if second < 0:
        raise ValueError("This Equations has no solution in the real numbers")
    second_mod = math.sqrt(second)
    return [first + second_mod, first - second_mod]


def fizz_buzz(n):
    result = []
    for i in range(n):
        if i == 0:
            continue
        if i % 3 == 0 and i % 5 == 0:
            result = result + ["Fizz Buzz"]
            continue
        if i % 3 == 0:
            result = result + ["Fizz"]
            continue
        if i % 5 == 0:
            result = result + ["Buzz"]
            continue
        result = result + [i]
    return result


def myint(bin):
    temp = bin[::-1]
    leng = len(bin)
    result = 0
    multiplicator = 1
    for i in range(0, leng - 2):
        result = result + int(temp[i]) * multiplicator
        multiplicator = multiplicator * 2
    return result


def mybin(inte):
    if inte == 0:
        return "0b0"
    input = ""
    rechnung = inte
    while rechnung > 0:
        help = int(rechnung / 2)
        temp = rechnung - help * 2
        input = input + str(temp)
        rechnung = help
        print(temp)
    return "0b" + input[::-1]
