from geocode_resolver import resolver
from geocode_resolver import resolver_backup

from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) 
def main():

	API_KEY = resolver.get_env_variables()
	HERE_app_id, HERE_app_code = resolver_backup.get_env_variables()

	address = request.args.get('address')

	if address is None:
		return jsonify({"status": "Error", 'description': 'No address provided.'})

	results = resolver.resolve(address, API_KEY)

	if results['status'] != 'OK':

		if address is None:
			return jsonify({"status": "Error", 'description': 'No address provided.'})

		backup_results = resolver_backup.resolve(address, HERE_app_id, HERE_app_code)		

		return jsonify(backup_results)

	return jsonify(results)

app.run()

