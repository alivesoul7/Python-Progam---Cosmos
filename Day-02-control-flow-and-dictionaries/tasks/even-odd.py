#defining a function named Check even or Odd
def checkEvenorOdd(num):
 if num % 2 == 0:
    return f"{num} is even"
 else:
    return f"{num} is odd"

#taking input from the user
number = int(input("Enter a number: "))

#passing the parameter to the function
result = checkEvenorOdd(number)

#Displaying the result to the user
print(result)