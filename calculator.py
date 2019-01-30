while True:
    try:
        firstNumber = int(input("Enter a number (or a letter to exit): "))
    except ValueError:
        break
        
    operation = None
    while operation == None:
        operation = str(input("Enter an operation: "))

        if operation in ['+', '-', '*', '/']:
            break
        else:
            operation = None
    while True:
        try:
            secondNumber = int(input("Enter another number: "))
        except ValueError:
            continue
        break

    if operation == "+":
        result = firstNumber+secondNumber
        print("Result: "+str(result))
    elif operation == "-":
        result = firstNumber-secondNumber
        print("Result: "+str(result))
    elif operation == "*":
        result = firstNumber*secondNumber
        print("Result: "+str(result))
    elif operation == "/":
        if secondNumber == 0:
            print("Can't divide by zero")
        else:
            result = firstNumber/secondNumber
            print("Result: "+str(result))