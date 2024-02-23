from art import logo
import operator

# def addition(first, second):
#     return first + second
#
#
# def multiplication(first, second):
#     return first * second
#
#
# def division(first, second):
#     return first / second
#
#
# def subtraction(first, second):
#     return first - second


# operation_list = {
#     "+": addition,
#     "-": subtraction,
#     "*": multiplication,
#     "/": division
# }

operation_list = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

print(logo)


def main_cal():
    first = None
    while True:
        [first, operation, second] = ask_for_input(first)
        answer = calculate_result(first, operation, second)
        print(f"{first} {operation} {second} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            first = answer
        else:
            break


def ask_for_input(num):
    first = num if num else float(input("What is the first's number? "))
    for operation in operation_list:
        print(operation)
    input_operation = input("Pick an operation: ")
    second = float(input("What is the second's number? "))
    return [first, input_operation, second]


def calculate_result(first, operation, second):
    return operation_list[operation](first, second)


main_cal()
