# ---------------------------------------------------------------------------------------------------------
# To capitalize the first letter of a string, you can use the dot upper method (.capitalize())
# Python has several string methods that let you look for text as (.find(), .index(), .rfind(), .rindex())
# Slicing : Getting part of a string value
# ---------------------------------------------------------------------------------------------------------

# for example

first_name = 'mohammed'
last_name = 'hassan'
my_university = 'azhar university'

print('************************************************')

first_name_cap = first_name.capitalize()
last_name_cap = last_name.capitalize()
print(first_name_cap)
print(last_name_cap)

print('************************************************')

azhar_location = my_university.find('azhar ')
print(azhar_location)
university_word = my_university[6:]
print(university_word)

print('************************************************')
