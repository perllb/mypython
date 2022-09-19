from app import app
from flask import request

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/add')
def add():
    data = request.args.get('data', None)
    _list = list(map(int, data.split(',')))
    total = sum(_list)
    return 'Result= ' + str(total)

def sum(arg):
    try: 
        total = 0
        for val in arg:
            total += val
        return total
    except Exception:
        return "Error occured!", 500

