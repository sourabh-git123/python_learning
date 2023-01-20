
class Dog():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says woof !'

class Cat():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow !"


niko = Dog("Niko")
felix = Cat("Felix")

print(niko.speak())
print("--------------------------------")
print(felix.speak())

for pet in [niko, felix]:
    print(type(pet))
    print(pet.speak())

