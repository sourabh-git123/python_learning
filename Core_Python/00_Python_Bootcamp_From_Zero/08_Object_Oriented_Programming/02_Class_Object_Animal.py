
class Animal():
    def __init__(self):
        # Calling of Constructor
        # print()
        print("Constructor of animal is called...")
        print("ANIMAL CREATED")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

# Inheriting Animal Class
class Dog(Animal):

    def __init__(self):
        print("Constructor of Dog is called...")
        Animal.__init__(self)

        print("Dog Created ")

#
# animal_obj = Animal()
# animal_obj.who_am_i()
# animal_obj.eat()


dog_obj = Dog()






