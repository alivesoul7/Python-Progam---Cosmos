shopping_list = ["Book", "Mobile Phone", "Smart watch", "Table"]

shopping_list.append("Headphone")
print(f"\nShopping list after append: {shopping_list}\n")

shopping_list.remove("Smart watch")
print(f"Shopping list after removal of item: {shopping_list}\n")

if "Book" in shopping_list:
    print(True)

length = len(shopping_list)
print(f"Length of the shopping_list is: {length}\n")

for item in shopping_list[1:5]:
    print(item)