import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def home():
    return '''<h1>KOSMOS</h1>
<p>A prototype API for try API functionality.</p>'''


@app.route('/api/v1/resources/kosmos/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('kosmos.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_people = cur.execute('SELECT * FROM kosmos;').fetchall()

    return jsonify(all_people)



@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.route('/', methods=['GET','POST'])
def index():
    if (request.method == 'POST'):
        some_json = request.get_json()
	return jsonify({'you sent': some_json}),201
    else:
	return jsonify({'about' : 'Hello World!'}),201
	 

@app.route('/', methods=['GET','POST'])
def delete():
    conn = sqlite3.connect('kosmos.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    cursor.execute('''DELETE FROM kosmos WHERE ip = ?''', (delete_ip,))
    db.commit()

@app.route('/', methods=['GET','POST'])
def update():
    conn = sqlite3.connect('kosmos.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    cursor.execute('''UPDATE kosmos SET name = ? WHERE id = ?''', (newName, kosmos_id))




@app.route('/api/v1/resources/kosmos', methods=['GET','POST'])
def api_filter():
    query_parameters = request.args

    id = query_parameters.get('id')
    name = query_parameters.get('name')
    ip = query_parameters.get('ip')

    query = "SELECT * FROM kosmos WHERE"
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if name:
        query += ' name=? AND'
        to_filter.append(name)
    if ip:
        query += ' ip=? AND'
        to_filter.append(ip)
    if not (id or name or ip):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('kosmos.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)



app.run()

