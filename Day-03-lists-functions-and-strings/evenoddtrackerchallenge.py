numbers = [4, 7, 10, 13, 18, 21]

def check_even_odd(numbers):
    even_count = 0
    odd_count = 0

    for num in numbers:
        if num % 2 == 0:
            even_count = even_count + 1
        else:
            odd_count = odd_count + 1

    return even_count, odd_count


even_count, odd_count = check_even_odd(numbers)

print("Even counts:", even_count)
print("Odd counts:", odd_count)
