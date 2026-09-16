grades = [85 , 92 , 78]
grades.append(98)
grades.remove(85)

if 92 in grades:
    print("92 is in the list")
total_count = len(grades)
total_sum = sum(grades)
loweset = min(grades)
highest = max(grades)

print(f"Count: {total_count} , Min: {loweset} , Max; {highest} , Sum: {total_sum}")
