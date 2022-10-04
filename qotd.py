import random
from flask import Flask

app = Flask(__name__)



@app.route("/")
def qotd():
    randint = random.randint(0, len(quotes)-1)
    return(quotes[randint])

def getQuotes():
    
    with open("quotes.txt", 'r', encoding="utf-8") as quotesfile:
        lines = quotesfile.readlines()
        return lines







if __name__ == '__main__':
    quotes = getQuotes()
    app.run(debug = True, host='0.0.0.0', port = '8000')
