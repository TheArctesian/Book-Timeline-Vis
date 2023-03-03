from flask import Flask, jsonify, request
import json
from waitress import serve

app = Flask(__name__)
NGRJSON = "GoodReads/GoodReadsData.json"
NLBJSON = "LetterBox/LetterBoxTable.json"


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

books = cleaner(grJ)
movies = cleaner(lbJ)
joinedMedia = books + movies

@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = request.environ.get(
        'HTTP_ORIGIN')
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response

# Tester
@app.route('/')
def ping():
    return 'Server is up'


@app.route('/Media/', methods=['GET', 'POST'])
def getMedia():
    if request.method == 'POST':
        res = request.json
    else:
        return jsonify(joinedMedia)
    
@app.route('/Media/Books', methods=['GET', 'POST'])
def getBooks():
    if request.method == 'POST':
        res = request.json
    else:
        try:
            return jsonify(books) 
        except Exception as e:
            return str(e)

@app.route('/Media/Movies', methods=['GET', 'POST'])
def getMovies():
    if request.method == 'POST':
        res = request.json
        return res
    else:
        try:
            return jsonify(movies)
        except Exception as e:
            return str(e)


'''
@app.route('/Advisory', methods=['GET', 'POST'])
def Advisory():
    if request.method == 'POST':
        res = request.json
        advisory = json.load(open('static/Advisory.json', 'r'))
        # Make copy and save as backup (redundancy)
        with open('static/Advisory.bak.json', 'w') as f:
            json.dump(advisory, f, ensure_ascii=False, indent=2)  # Write
        with open('static/Advisory.json', 'w') as f:
            # Re write file with updates
            json.dump(res, f, ensure_ascii=False, indent=2)
        return "200"
    else:
        try:
            advisory = json.load(open('static/Advisory.json', 'r'))
            return jsonify(advisory)
        except Exception as e:
            return str(e)

# These are all for refetching the backup database


@app.route('/AdvisoryBak')
def Advisorybak():
    try:
        advisory = json.load(open('static/Advisory.bak.json', 'r'))
        return advisory
    except Exception as e:
        return str(e)


@app.route('/Teacher', methods=['GET', 'POST'])
def Teacher():
    if request.method == 'POST':
        res = request.json
        teacher = json.load(open('static/teachers.json', 'r'))
        # Make copy and save as backup (redundancy)
        with open('static/teachers.bak.json', 'w') as f:
            json.dump(teacher, f, ensure_ascii=False, indent=2)
        with open('static/teachers.json', 'w') as f:
            json.dump(res, f, ensure_ascii=False, indent=2)
        return "200"
    else:
        try:
            teacher = json.load(open('static/teachers.json', 'r'))
            return jsonify(teacher)
        except Exception as e:
            return str(e)


@app.route('/TeacherBak')
def TeacherBak():
    try:
        teacher = json.load(open('static/teachers.bak.json', 'r'))
        return jsonify(teacher)
    except Exception as e:
        return str(e)


@app.route('/YearGroups/Y13',  methods=['GET', 'POST'])
def Y13():
    if request.method == 'POST':
        res = request.json
        Y13 = json.load(open('static/YearGroups/Y13.json', 'r'))
        # Make copy and save as backup (redundancy)
        with open('static/YearGroups/Y13.bak.json', 'w') as f:
            json.dump(Y13, f, ensure_ascii=False, indent=2)
        with open('static/YearGroups/Y13.json', 'w') as f:
            json.dump(res, f, ensure_ascii=False, indent=2)
        return "200"
    else:
        try:
            Y13 = json.load(open('static/YearGroups/Y13.json', 'r'))
            return Y13s
        except Exception as e:
            return str(e)


@app.route('/YearGroups/Y13Bak')
def Y13bak():
    try:
        Y13 = json.load(open('static/YearGroups/Y13.bak.json', 'r'))
        return Y13
    except Exception as e:
        return str(e)

'''

if __name__ == '__main__':
    # This servers the app under WSGI (production level encryption)
  #  app.run(debug=True)
    serve(app, host="0.0.0.0", port=5000)

# and there we go 100 lines for a api and my own db paradigm
