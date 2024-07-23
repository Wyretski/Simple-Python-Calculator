print("Accepted Operations:\nAddition\nSubtraction\nMultiplication\nDivision\n (INPUT IS CASE SENSITIVE!)\n")
def calculate():
    desired_operation = str(input("What is your desired operation? "))
    desired_operation = desired_operation.lower()

    if desired_operation in "addplus+":
        try:
            int_1 = int(input("Integer 1: "))
            int_2 = int(input("Integer 2:"))
        except ValueError:
            return ("Invalid input!")
        result = int_1 + int_2
        return (f"{int_1} + {int_2} = {result}")
    elif desired_operation in "subtractionsubtractminus-":
        try:
            int_1 = int(input("Integer 1: "))
            int_2 = int(input("Integer 2: "))
        except ValueError:
            return("Invald input!")
        result = int_1 + int_2
        return (f"{int_1} - {int_2} = {result}")
    elif desired_operation in "multiplicationmultiplytimes*":
        try:
            int_1 = int(input("Integer 1: "))
            int_2 = int(input("Integer 2: "))
        except ValueError:
            return("Invald input!")
        result = int_1 + int_2
        return (f"{int_1} * {int_2} = {result}")
    elif desired_operation in "divisiondivide/":
        try:
            int_1 = int(input("Integer 1: "))
            int_2 = int(input("Integer 2: "))
        except ValueError:
            return("Invald input!")
        result = int_1 + int_2
        return (f"{int_1} - {int_2} = {result}")
    else:
        return ("Invalid input!")

print(calculate())