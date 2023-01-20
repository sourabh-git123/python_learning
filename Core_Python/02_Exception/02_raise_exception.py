"""
    Here, we can raise exception according to our condition and will not depend on the compiler for raising the
    exception
    We have caught these exception :

    a. TypeError
    b. ZeroDivisionError
    c. Exception         - Generic exception

"""

try:

    i = 2
    if i == 2:
        raise Exception("Generic exception is raised...")
    new_list = []
    print(new_list[i])

    # str = "Hello"
    str = 87

    if not type(str) is int:
        raise TypeError("Only integers number are allowed ")

    a = 30
    b = 0

    if b == 0:
        raise ZeroDivisionError("Number cannot be decided by Zero ")

    print("Code looks Good..")

except TypeError as e:
    import traceback
    print(f"Type Error Exception occurred : {traceback.print_exc()}  ")

except ZeroDivisionError as e:
    import traceback
    print(f"Zero Division Error Exception occurred : {traceback.print_exc()}  ")

except Exception as e:
    import traceback
    print(f"Generic Exception occurred : {traceback.print_exc()}  ")


