def check_even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

numbers = [4, 7, 10, 13, 18, 21]
evens, odds = 0, 0
for num in numbers:
    result = check_even_odd(num)
    print(f"{num} is {result}")
    if result == "Even":
        evens += 1
    else:
        odds += 1
print(f"Evens: {evens} , Odds : {odds} ")