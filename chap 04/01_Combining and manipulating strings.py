# ----------------------------------------------------------------------------
# Concatenation : When mutiple strings are combined into a single string
# You can concatenate text to whatever a user enters, by using a plus sign (+)
# The int method converts a string to an integer
# ----------------------------------------------------------------------------

print("*********************************************")
value = input('Enter a number: ')
print(value)
print("*********************************************")

value = input('Enter a number: ')
print((value + ' is my favorite number!'))
# My program has taken the string value I entered and printed it 10 times (Not multiply it)
print(value * 10)
print("*********************************************")

# The Int method
value = input('Enter a number: ')
value_int = int(value)  # To convert value from str to int
print(value_int * 10)

print("*********************************************")
