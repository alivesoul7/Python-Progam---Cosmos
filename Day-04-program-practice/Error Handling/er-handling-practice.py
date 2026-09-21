num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

try:
    if num2 == 0:
     result = num1/num2

    else:
        result = num1/num2
        print(result)
except ZeroDivisionError:
    print("Cannot be divide by Zero")