from flask import Flask, request

#ToDo: Solve importing ticket_searcher module better way and not to add upper dir by this nice hack..
import sys, os, json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ticket_searcher import TicketSearcher
from datetime import datetime

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True


@app.route('/search', methods=['GET'])
def search():
    source = request.args.get('src')
    destination = request.args.get('dst')
    date = request.args.get('date')

    ts = TicketSearcher()
    connections = ts.get_connections(source, destination, datetime.strptime(date, '%Y-%m-%d'))

    return json.dumps(ts.get_best_connection(connections))