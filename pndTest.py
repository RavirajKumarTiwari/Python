import pandas as pd

data = {
    "apples": [4, 3, 6, 1],
    "orange": [3, 7, 4, 1]
}

index_title = [
    "Aaron", "Shaun", "James", "Wilson"
] 
df = pd.DataFrame(data, index=index_title)

print(df)
print(type(df))
print(df.loc["Aaron"])
print(df.loc["Aaron"],["Shaun"])
print(df["orange"].iloc[1:])
