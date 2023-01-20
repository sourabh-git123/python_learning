
"""
    Following is covered here :
    a. to_string

        << Dunder >>
    b. __init__
    c. __len__
    d. __del__




"""
# class Sample():
#     pass

# mysample = Sample()

# print(mysample)

# Magic method

class Book():

    def __init__(self, title, author, pages):

        self.title = title
        self.author = author
        self.pages = pages

    """
        To string method is being called when we print the object only ,
        Note :  If tostring object is not defined then then it will print the memory
        reference 
    """
    def __str__(self):
        print("To string is being implemented..")
        return f" {self.title} by {self.author} "
        pass

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book object has been now deleted ")


# Object creation and to-string implementation

book_obj = Book('Python rocks', 'Jose', 405)
print(book_obj)
print(f"type of book : ")
print(type(book_obj))

print(f"len = {len(book_obj)}  ")






