from arts import day_9_art

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def calculator():

    print(day_9_art.logo)

    keep_playing = True
    first = float(input("Whats the first number: \n"))
    calc_dict = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    while keep_playing:
        op = input(""
                   "+\n"
                   "-\n"
                   "*\n"
                   "/\n"
                   "Pick an operator:\n")

        another_number = float(input("Whats the next number?: \n"))
        calculation_function = calc_dict.get(op)

        if not calculation_function:
            print("Invalid operator! Try again.")
            continue

        answer = calculation_function(first, another_number)
        print(f"{first} {op} {another_number} = {answer}")

        keep_playing = input(f"Type 'y' to continue with {answer} or type 'n' to start new calculation:\n")

        if keep_playing.lower() == 'y':
            first = answer
        else:
            keep_playing = False
            calculator()

calculator()