books = ("Deep Work","Atomic Habits","Mindset","Eat that Frog")
single = (10,)
mixed = ("Emotional Intelligence",25,"Finley")

print(books[2],books[-1])
print(books[0:2])

name , age , role = mixed
print(f"nameis {age} as {role}")

nums = (4,2,7,9)
print("Counts of 2: ",nums.count(2))

combined = books + ("As a man thinketh",)
print("Total iterms: ",len(combined))

nested = ("points",(3,4))
print("X: ",nested[1][0])