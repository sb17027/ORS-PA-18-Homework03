"""
===================   TASK 3   ====================
* Name:  Euclidean algorithm
*
* Write a function `gcd` that will calculate
* greatest common divisor for two integer values.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

def gcd(a,b):
    while a != b:
        if a > b:
            a=a-b
        else:
            b=b-a
    return a
def main():
    a=14
    b=7
    gcd_result=gcd(a,b)
    print("GCD for a and b: ", gcd_result)
main()
