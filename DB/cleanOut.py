import json

NGRJSON = "GoodReads/GoodReadsData.json" # Good reads
NLBJSON = "LetterBox/LetterBoxTable.json" # Lettboxd
NGWJSON = "Glitchwave/games.json" # Games

# Load the JSON data from the first file
with open( "GoodReads/GoodReadsData.json") as f1:
    grJ = json.load(f1)
# Load the JSON data from the second file
with open(NLBJSON) as f2:
    lbJ = json.load(f2)

with open(NGWJSON) as f3:
    gwJ = json.load(f3)


def cleaner(JsonRef):
    del JsonRef["schema"]
    for i in JsonRef["data"]:
        del i["index"]
    return JsonRef["data"]

l1 = cleaner(grJ)
l2 = cleaner(lbJ)
l3 = cleaner(gwJ)
print(l3)
joinedList = l1 + l2 + l3



with open('merged_file.json', 'w') as f:
    json.dump(joinedList, f)