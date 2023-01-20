
a = int(20)
b = int(4)
new_dict = {
    "name" : "Kumar Sanu"
}
try:
    pass
    c = a/b
    print(c)

except ZeroDivisionError:
    pass
    print("Zero Division error occurred")

try:
    pass
    var = new_dict['name']
    print(f"name from dict  = {var}")

except KeyError:
    pass
    print("Key error occurred")

try:
    pass
    c = 10 / 0
    print(f"Dividing 10 by zero : {c} ")

except Exception as e:
    pass
    print("Divid by zero occurred..")

else:
    pass
    print("Else part of dictionary is executed..")
