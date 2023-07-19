import pandas as pd

df = pd.read_csv("./games.csv")
#print(df.to_string()) 

df.insert(0, "type", ["Game"] * (len(df)), True)
print(df.columns.values)
print(df.info)
df.columns= ['type',"title", "author", "year", "views"]
df.to_json('games.json', orient="table")
