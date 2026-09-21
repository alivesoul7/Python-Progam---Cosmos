# 1. Writing Files Safely
with open("writenote.txt", "w") as f:
    f.write("Hey this is finley simula")

# 2. Reading Files Safely
with open("writenote.txt","r") as f:
    content = f.read()
    print(content)