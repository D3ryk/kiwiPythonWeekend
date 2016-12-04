from flask import Flask, request

#ToDo: Solve importing ticket_searcher module better way and not to add upper dir by this nice hack..
import sys, os, json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ticket_searcher import TicketSearcher
from config_loader import ConfigLoader
from datetime import datetime

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True

config_loader = ConfigLoader('config.json')
config_loader.start()


@app.route('/search', methods=['GET'])
def search():
    source = request.args.get('src')
    destination = request.args.get('dst')
    date = request.args.get('date')
    error = {}

    if date:
        try:
            date = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            error = {'error': 'Bad date format for parameter date should be in %Y-%m-%d'}
    else:
        date = datetime.today()

    if not error:
        ts = TicketSearcher()
        connections = ts.get_connections(source, destination, date)
        response = json.dumps(ts.get_best_connection(connections))
    else:
        response = json.dumps(error)

    return response

app.run()