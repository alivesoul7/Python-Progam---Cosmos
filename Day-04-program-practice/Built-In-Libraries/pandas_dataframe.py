import pandas as pd

#1. Define rw data_dictionary
data = {
    "name" : ["Alice" , "Bob" , "Carol"],
    "age" : [25,30,35]
}

df = pd.DataFrame(data)

print(df)
print(df["age"].mean())