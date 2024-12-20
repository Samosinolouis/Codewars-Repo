'''Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.

Examples
Input: [1, 5.2, 4, 0, -1]
Output: 9.2

Input: []
Output: 0

Input: [-2.398]
Output: -2.398

Assumptions
You can assume that you are only given numbers.
You cannot assume the size of the array.
You can assume that you do get an array and if the array is empty, return 0.
What We're Testing
We're testing basic loops and math operations. This is for beginners who are just learning loops and math operations.
Advanced users may find this extremely easy and can easily write this in one line.'''

def sum_array(a):
    a = sum(a)
    if a == 0:
        return 0
    else:
        return a

'''
TEST CASE:
import codewars_test as test
from solution import sum_array

from random import random, randint
@test.describe("Testing sum array")
def tests():
    @test.it("Fixed tests")
    def fixed_tests(): 
        test.assert_equals(sum_array([]), 0)
        test.assert_equals(sum_array([1, 2, 3]), 6)
        test.assert_equals(sum_array([1.1, 2.2, 3.3]), 6.6)
        test.assert_equals(sum_array([4, 5, 6]), 15)
        test.assert_equals(sum_array(range(101)), 5050)

    @test.it("Random tests")
    def random_tests():
        for i in range(100):
            L = [round(random()*1000, 3) for i in range(randint(10, 100))]
            actual_sum = sum(L)
            test.assert_approx_equals(sum_array(L), actual_sum, margin=1e-5)'''