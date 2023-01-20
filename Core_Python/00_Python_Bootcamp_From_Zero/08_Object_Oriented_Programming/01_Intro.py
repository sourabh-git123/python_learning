
class NameOfClass():

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def some_method(self):
        print(f"param1 = {self.param1} ")
        print(f"param2 = {self.param2} ")


def main():

    param1 = 'First Parameter String'
    param2 = 'Second Parameter String'

    obj = NameOfClass(param1, param2)
    obj.some_method()

if __name__ == '__main__':
    main()

