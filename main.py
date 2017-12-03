from geocode_resolver import resolver

from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) 
def main():

	API_KEY = resolver.get_env_variables()
	address = request.args.get('address')
	if address is None:
		return jsonify({"status": "error", 'description': 'No address provided, bitch'})
	
	method = 'gmap'
	lat1 = resolver.resolve(address, API_KEY, method)
	return jsonify(lat1)

app.run()
