from bottle import Bottle, request
from dateparser.search import search_dates
import dateparser
import datetime
import json

app = Bottle()


@app.get('/api')
def api():
    date = request.query.get('date')
    result = resolve(date)
    return dict(data=result)


def converter(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()


def resolve(date: str):
    response = {
        'date': dateparser.parse(date).ctime()
    }

    return response
