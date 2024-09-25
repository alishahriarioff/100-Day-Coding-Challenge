# Calculator program
from art import logo
from replit import clear

# Add Function
def add(n1, n2):
    return n1 + n2
# Subtract Function
def subtract(n1, n2):
    return n1 - n2
# Multiply Function
def multiply(n1, n2):
    return n1 * n2
# Divide Function
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    num1 = float(input("Whats the first number? "))
    for operator in operations:
            print(operator)
    calculating = True
    while calculating:
        operation_symbol = str(input("pic a operation: "))
        num2 = float(input("Whats the next number? "))

        function = operations[operation_symbol]
        answer = function(num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        
        sould_continue = str(input(f"type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")).lower()
        if sould_continue == 'y':
            num1 = answer
        else:
            calculating = False
            clear()
            calculator()

calculator()