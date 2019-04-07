from blatt0 import print_pascal
from blatt0 import fizz_buzz
from blatt0 import solve_equation
from blatt0 import myint, mybin
from blatt0 import is_palindrome
from blatt0 import flatten
import random


def test_palindrom():
    input = "anna"
    assert is_palindrome(input) == True


def test_pascal():
    input = 4
    assert print_pascal(5) == [[1.0], [1.0, 1.0], [1.0, 2.0, 1.0], [1.0, 3.0, 3.0, 1.0], [1.0, 4.0, 6.0, 4.0, 1.0]]


def test_flatten1():
    input = []
    assert flatten(input) == []


def test_flatten2():
    input = [["Hallo"]]
    assert flatten(input) == ["Hallo"]


def test_flatten3():
    assert flatten([["Hallo"],["Welt"]]) == ["Hallo", "Welt"]


def test_solve_equation1():
    assert solve_equation(1, 0, 0) == [0.0, 0.0]


def test_solve_equation3():
    assert solve_equation(1, -6, 5) == [5.0, 1.0]


def test_solve_equation4():
    assert solve_equation(2, -3, 1) == [2.0, 0.0]


def test_fizz_buzz():
    output = [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "Fizz Buzz", 16, 17, "Fizz",
              19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "Fizz Buzz", 31, 32, "Fizz", 34, "Buzz",
              "Fizz"]
    assert fizz_buzz(37) == output


def test_int_to_bin():
    input = random.sample(range(1000), 10)
    for x in input:
        assert mybin(x) == bin(x)


def test_bin_to_int():
    input = [(i, bin(i)) for i in random.sample(range(1000), 10)]
    for i, bini in input:
        assert myint(bini) == i
