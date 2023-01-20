
class Dog():

    # Class variable
    species = 'mammal'
    def __init__(self, breed, name, spots):

        "Attribute : that we will take in the argument "
        self.breed = breed
        self.name = name

        " Expect boolean "
        self.spots = spots

    # OPERATION / Actions
    def bark(self):
        pass

class Circle():

    pi = 3.14
    def __init__(self, radius):
        self.radius = radius

    # Method
    def get_circumference(self):
        return self.radius * self.pi * 2



def main():

    print("From main...")
    my_dog_obj = Dog(breed= 'Lab', name='Tom', spots= False)
    print(type(my_dog_obj))

    print(my_dog_obj.species)
    print(id(my_dog_obj.species))




    circle_obj = Circle(30)
    print(circle_obj.pi)


if __name__ == '__main__':
    main()















