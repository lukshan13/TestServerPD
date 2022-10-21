import random
import requests
from flask import Flask, request
import time

from opentelemetry import trace

from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.trace.export import ConsoleSpanExporter

import SLConsoleSpanExporter

provider = TracerProvider()
processor = BatchSpanProcessor(SLConsoleSpanExporter.SLConsoleSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)


app = Flask(__name__)


@app.route("/")
def qotd():

    with tracer.start_as_current_span("quote_request"):
        return doRequest()


        
    
def doRequest():
    randint = random.randint(0, len(quotes)-1)
    quote = quotes[randint]
    print(quote)
    time.sleep(0)
    i = random.randint(0,5)
    print(i)
    if i == 5:
        raise KeyError("Lol")
    return(quote)


def getQuotes():
    
    with open("quotes.txt", 'r', encoding="utf-8") as quotesfile:
        lines = quotesfile.readlines()
        return lines







if __name__ == '__main__':
    quotes = getQuotes()
    app.run(host='0.0.0.0', port = '5000')
