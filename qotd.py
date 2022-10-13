import random
import requests
from flask import Flask, request
import time


app = Flask(__name__)


@app.route("/")
def qotd():

 
    return doRequest()


        
    
def doRequest():
    randint = random.randint(0, len(quotes)-1)
    quote = quotes[randint]
    print(request.args.get("param"))
    print(quote)
    time.sleep(0.8)
    return(quote)


def getQuotes():
    
    with open("quotes.txt", 'r', encoding="utf-8") as quotesfile:
        lines = quotesfile.readlines()
        return lines







if __name__ == '__main__':
    quotes = getQuotes()
    app.run(host='0.0.0.0', port = '5000')
