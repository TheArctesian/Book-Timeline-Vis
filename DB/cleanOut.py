import json

NGRJSON = "GoodReads/GoodReadsData.json"
NLBJSON = "LetterBox/LetterBoxTable.json"
# Load the JSON data from the first file
with open( "GoodReads/GoodReadsData.json") as f1:
    grJ = json.load(f1)
# Load the JSON data from the second file
with open(NLBJSON) as f2:
    lbJ = json.load(f2)

def cleaner(JsonRef):
    del JsonRef["schema"]
    for i in JsonRef["data"]:
        del i["index"]
    return JsonRef["data"]

l1 = cleaner(grJ)
l2 = cleaner(lbJ)

joinedList = l1 + l2


with open('merged_file.json', 'w') as f:
    json.dump(joinedList, f)