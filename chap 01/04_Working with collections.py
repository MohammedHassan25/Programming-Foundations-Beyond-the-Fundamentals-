# -------------------------------------------------------------------------------------------------------------------------
# It's important to note that index numbering does not start at one . It starts at zero
# To reference the data at given list index, you refrence the variable name followed by the index number in square brackets
# To reference a dictionary item, I start by referencing the name of the variable that stores the dictionary value
# A dictionary doesn't use index numbers though because each item in a dictionary has a label
# -------------------------------------------------------------------------------------------------------------------------

# For Example in List :

# city1 = "Cairo"
# city2 = "Alex"
# city3 = "Assuit"

cities = [
    'Cairo',
    'Alex',
    'Assuit',
]

print(cities[2])

# For Example in Dictionary :

# Name = "Mohammed Hassan"
# My_Country = "Egypt"
# My_City = "Assuit"

CV = {
    'Name': 'Mohammed Hassan',
    'My_Country': 'Egypt',
    'My_City': 'Assuit'
}

# Wrong :-
# print(CV[2])

# Right :-
print(CV['Name'])
