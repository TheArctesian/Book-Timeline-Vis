import pandas as pd

df = pd.read_csv("./goodreads_library_export.csv")
#print(df.to_string()) 
df = df.drop(columns=["Book Id",
                      'Author l-f',
                      'Additional Authors', 
                      'ISBN',
                      "ISBN13",
                      "My Rating",
                      "Average Rating",
                      "Publisher",
                      "Binding",
                      "Number of Pages",
                      "Year Published",
                      "Date Read",
                      "Date Added",
                      "Bookshelves",
                      "Bookshelves with positions",
                      "Exclusive Shelf",
                      "My Review",
                      "Spoiler",
                      "Private Notes",
                      "Owned Copies"
                    ])

df.insert(0, "type", ["Book"] * (len(df)), True)
print(df.columns.values)
print(df.info)
df.columns= ['type',"title", "author", "year", "views"]
df.to_json('GoodReadsData.json', orient="table")
