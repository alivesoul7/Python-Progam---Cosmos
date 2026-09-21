query = input("Enter your note to store in Notebook: ")
try:
    if query.strip() == "":
        raise ValueError("empty note")
    with open("rick.txt", "w") as f:
        f.write(query)
except (OSError, ValueError):
    print("Provide some content in the notebook")

try:
    with open("rick.txt", "r") as f:
        content = f.read()
    print(content)
except OSError:
    print("Nothing found on the notebook")