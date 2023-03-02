import json
import pandas as pd
import numpy as np

class Schema:
    def __init__(self, Name, Author, Image, DatePublished, DateRead, Watched):
        self.Name = Name
        self.Author = Author
        self.DatePublished = DatePublished
        self.Watched = watched


if __name__ == "__main__":
    # Read
    wdf = pd.read_csv("./watched.csv")
    ldf = pd.read_csv("./watchlist.csv")

    # Parse
    wdf = wdf.drop(columns=["Date", "Letterboxd URI"])
    ldf = ldf.drop(columns=["Date", "Letterboxd URI"])

    # Add watcher var
    wdf.insert(2, "Watched", [1] * (len(wdf)), True)
    ldf.insert(2, "Watched", [0] * (len(ldf)), True)
    wdf.insert(1, "Watched", [""] * (len(wdf)), True)
    ldf.insert(1, "Watched", [""] * (len(ldf)), True)

    # Add empty Author Line (#TODO add director names)

    print(type(wdf.columns.values))
    print(wdf.shape[0])

    wdf.to_json('data.json', orient="values")
