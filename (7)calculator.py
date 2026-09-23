### calcutlator program
try: 
    operator = input('enter the operator (+ - * /): ')
    num1 = float(input('enter the 1st number: '))
    num2 = float(input('enter the 2nd number: '))

    # make a statements
    if operator == "+":
        result = num1 + num2
        print(result)
    elif operator == "-":
        result = num1 - num2
        print(result)
    elif operator == "*":
        result = num1 * num2
        print(result)
    elif operator == "/":
        if num2 == 0:
            print(f"the number can't be divided by 0")
        else:
            result = num1 / num2
            print(result)
    else:
        print(f"please check ur operator input!")
        
except ValueError:
    # eror handling if the user input invalid number or else
    print(f"please correct ur number input")
    
