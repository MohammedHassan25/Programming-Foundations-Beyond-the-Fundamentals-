# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# You can define the basic properties and methods that a set of objects should share and can then customize each object as necessary after you create it .
# ------------------------------------------------------------------------------------------------------------------------------------------------------------

class Myfriends:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)

    def print_Myfriends(self):
        print(f'name : {self.name}, age : {self.age}')


Myfriends1 = Myfriends("Mohammed", 21)
Myfriends2 = Myfriends("Ali", 23)

Myfriends1.print_Myfriends()
Myfriends2.print_Myfriends()
