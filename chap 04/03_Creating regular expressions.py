# ---------------------------------------------------------------------------------------------------------
# Regular Expression : Allows you to create a description of a pattern that you want to match
# re moduls contains methods for creating and working with regular expressions
# ---------------------------------------------------------------------------------------------------------

import re

print("*********************************************")
number1 = "98654"
number2 = "98654-0003"
phone_number = '544-646-4644'

number_expresstion = r'\d{5}'
print(re.search(number_expresstion, number1))
print(re.search(number_expresstion, number2))
print(re.search(number_expresstion, phone_number))
print("*********************************************")
