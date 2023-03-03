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

print(df.columns.values)
print(df.info)

df.to_json('data.json', orient="values")
