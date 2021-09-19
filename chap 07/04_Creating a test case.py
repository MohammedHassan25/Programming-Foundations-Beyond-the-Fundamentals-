# -----------------------------------------------------------------------
# Test Cases : Commands or scripts designed to test a specific scenario
# Test cases are useful tool to ensure consistent results from your app
# -----------------------------------------------------------------------

def temperature(temp):
    if temp < 15:
        print("Pack a jacket!")
    elif temp > 15 and temp < 35:
        print("The weather is nice!")
    elif temp > 35:
        print("The weather is hot!")


temperature(14)
temperature(20)
temperature(36)
