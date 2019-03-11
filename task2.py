"""
===================   TASK 2   ====================
* Name: Valid Mobile Number In Montenegro
*
* Write a function `valid_mobile_number` that will
* return True if given string is valid mobile phone
* number in Montenegro. Consider that +382 code will
* not be passed.
*
* Phone number is valid if:
*
*  - Has 9 or 10 digits
*  - Begins with '06'
*  - Third digit has to be one of [3, 6, 7, 8, 9]
*  - Contains digits only
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""


def valid_mobile_number(phone_number):
    length_test = len(phone_number) == 9 or len(phone_number) == 10
    stars_with_test = phone_number.startswith("06")
    third_char_test = phone_number[2] == "3" or phone_number[2] == "6" or phone_number[2] == "7" or phone_number[2] == "8" or phone_number[2] == "9"
    all_digits_test = phone_number.isdigit()

    if (length_test and stars_with_test and third_char_test and all_digits_test):
        return True
    else:
        return False

def main():

    number_to_test = "067458884"
    if valid_mobile_number(number_to_test):
        print("Phone number is valid in Montenegro!")
    else:
        print("Phone number is invalid in Montenegro!")

main()
