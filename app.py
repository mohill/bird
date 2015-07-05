#!/usr/bin/python2.7

from flask import Flask
from flask import json
from flask import request

from bson.json_util import dumps

# local modules  
from bird import Bird

app = Flask(__name__)
app.config['DEBUG'] = False

""" Flask route for /
	Returns string to user with status 200.
"""
@app.route('/')
def index():
	return "bird application", 200

""" Flask route for /birds and /birds/<id>
	Returns JSON-data to user if bird(s) found.
"""
@app.route('/birds', methods=['GET'])
@app.route('/birds/<id>', methods=['GET'])
def birds_get(id=None):
	B = Bird()

	result = B.list(id)

	if not result:
		return "Not found", 404

	return dumps(result), 200

""" Flask route for /birds POST.
	Validates recieved JSON-data and stores into Mongo-document.
	Returns JSON-data to user from inserted bird.
"""
@app.route('/birds', methods=['POST'])
def birds_post():
	# validate posted json, checks invalid JSON and mandatory fields.
	try:
		content = request.get_json()
		row = (content['name'], content['family'], content['continents'])
	except (ValueError, KeyError, TypeError):
	    # mandatory fields missing or invalid json, return 400.
	    return "Bad request", 400

	# checks for visible field, if not set default to false. 
	try:
		isinstance(content['visible'], bool)
	except (ValueError, KeyError):
   		visible = False
	else:
		visible = content['visible']
		
	# create Bird.
	B = Bird(
		content['name'],
		content['family'],
		content['continents'],
		visible
	)

   	# insert bird and return id to user.
	try:
		id = B.insert()
	except:
		return "Error inserting bird into MongoDB.", 400

	# fetch bird-data with id from insert.
	result = B.list(id)

	# if no result, return to user.
	if not result:
		return "Error, bird inserted but not found.", 400

	# return json-data to user..
	return dumps(result), 200

""" Flask route for /birds/id DELETE
	Deletes bird with ID and returns OK, 200 if found.
"""
@app.route('/birds/<id>', methods=['DELETE'])
def birds_delete(id=None):
	if id is None:
		return "Error, no id given", 404

	B = Bird()

	if B.delete(id) is True:
		return "OK", 200
	else:
		return "Not found", 404

""" Defines our application, listening-host and port.
"""
if __name__ == "__main__":
	app.run(debug = False, host="0.0.0.0", port=8000)