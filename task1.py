"""
===================   TASK 1   ====================
* Name: Sum Number Digits
*
* Write a function `sum_digits` that will return
* sum of digits for given integer number.
* If passed value is invalid, function should
* return -1 which indicates something went wrong.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

import numbers
def sum_digits(number):
    if(not isinstance(number,numbers.Number)):
        return -1
    number = abs(number)
    s = 0
    while number:
        s += number % 10
        number = number // 10
    return s

def main():

    int_number = 12
    digit_sum = sum_digits(int_number)
    print("Sum of digits for given numbers is: ", digit_sum)
main()
