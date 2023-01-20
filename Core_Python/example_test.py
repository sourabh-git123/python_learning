#
# student_dict = {
#
#     'Ram' : '9878787787',
#     'Shyam': '8754343434'
#
# }
#
# for name, mob in student_dict.items():
#
#     print(f"name --> {name}", end = "  ")
#     print(f"mob  --> {mob}", end = "  ")
import json


def add(first_no = None, second_no = None):
    sum_no = first_no + second_no

    print(f"Sum of No : ({first_no})  and  ({second_no})  is  ({sum_no})")

def division(first_no = None, second_no = None):

    try:

        first_no = int(first_no)
        second_no = int(second_no)

        if second_no == 0:
            print("No cannot be divided by zero..")
            return -1

        div_no = first_no/second_no

        print(f"Div of No : ({first_no})  and  ({second_no})  is  ({div_no})")
        return div_no

    except TypeError:
        print("Please pass integer value / numerical value ..")
        return -1

    except ValueError:
        print("Please pass integer value / numerical value ..")
        return -1

    except:
        import traceback
        print(f"gen exc : {traceback.print_exc()}")
        print(f"Returning with generic exception ")
        return -1


def write_to_file(content_to_write):

    import os

    fileName = "abc.txt"
    path = os.getcwd() + fileName

    with open(path, "w") as file_handle:
        str_content = json.dumps(content_to_write)
        file_handle.write(str_content)


if __name__ == "__main__":
    print("From main..")
    # add(35, 25)

    print("Calling div...")
    # return_value = division(10, 3)
    # print(f"1 returning from division : {return_value}")

    return_value = division("Hello", 3)

    print(f"return value = {return_value}")


