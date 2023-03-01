import json
import coalas
class Schema:
    def __init__(self, Name, Author, Image, DatePublished, DateRead, Watched):
        self.Name = Name
        self.Author = Author
        self.Image = Image
        self.DatePublished = DatePublished
        self.DateRead = DateRead
        self.Watched = watched

# I am locking at this class and relising I don't like OOP in this language
# Even TS is better, I have no type saftey on init


if __name__ == "__main__":
    data = coalas.csvReader(watcher.csv)
    print(data)
