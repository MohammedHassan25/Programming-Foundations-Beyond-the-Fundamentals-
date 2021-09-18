# ----------------------------------------------------------------------------------------------------------------
# for :- Specifies a variable name that we can use in each iteration of the loop to reference the current value
# In :- Indicates that what follows is the set of values that we want to iterate through
# ----------------------------------------------------------------------------------------------------------------

# for example

spices = [
    'salt',
    'pepper',
    'cumin',
    'turmeric',
]
for x in spices:
    print(x)
print()

for x in spices:
    print(x)
    print("That's good")   # It will be repeated with each iteration
print()

for x in spices:
    print(x)
print("That's good")       # It will not be repeated with each iteration
