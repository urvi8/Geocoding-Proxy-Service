import os
import json
import urllib, urllib2


def get_env_variables():

	return os.environ.get('HERE_app_id'), os.environ.get('HERE_app_code')


def resolve(address, HERE_app_id, HERE_app_code):

	url_base = "https://geocoder.cit.api.here.com/6.2/geocode.json?"
	params = {"searchtext": address, "app_id": HERE_app_id, "app_code": HERE_app_code}
	params_encoded = urllib.urlencode(params)

	response = urllib2.urlopen(url_base + params_encoded)

	data = json.load(response)   

	backup_result = {}

	if len(data['Response']['View']) == 0:
		backup_result['Status'] = "Error"
		backup_result['description'] = 'Unknown Error'		

	elif len(data['Response']['View']) != 0:
		backup_result = {"Status": 'OK', "Latitude": data['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Latitude'], "Longitude": data['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Longitude'], "Method": "HERE"}

	return backup_result


