import pytest

def fizzBuzz(number: int)-> str:
    return_str = []
    if number % 3 == 0:
        return_str.append("Fizz")
    if number % 5 == 0:
        return_str.append("Buzz")
    return "".join(return_str)

def test_returnFizzWith3():
    retVal = fizzBuzz(3)
    assert retVal == "Fizz"   


def test_returnBuzzWith5():
    retVal = fizzBuzz(5)
    assert retVal == "Buzz"   

def test_returnFizzWith6():
    retVal = fizzBuzz(6)
    assert retVal == "Fizz"   


def test_returnBuzzWith10():
    retVal = fizzBuzz(10)
    assert retVal == "Buzz"   

def test_returnBuzzWith15():
    retVal = fizzBuzz(15)
    assert retVal == "FizzBuzz" 