import os
import json
import urllib, urllib2


def get_env_variables():

#	return os.environ.get('API_HERE'), os.environ.get('API_GMAP')
	return os.environ.get('API_KEY')

def resolve(address, API_KEY, method):

	url_base = "https://maps.googleapis.com/maps/api/geocode/json?"
	params = {"address": address, "key":API_KEY}
	params_encoded = urllib.urlencode(params)
#	response = urllib2.urlopen('address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=AIzaSyCFjTLEFL_VZI5KMBSHbfNCLuJRJJC8N7g')
	response = urllib2.urlopen(url_base + params_encoded)
#	print url_base + params_encoded
	data = json.load(response)   

	final_result = {}
	
	
#	print type(data)

	if data['status'] != 'OK':
		final_result['status']=data['status']
		final_result['description'] = "Please refer to https://developers.google.com/maps/documentation/geocoding/start"
		

	elif data['status'] =='OK':
		final_result = {"status": data['status'], "latitude": data['results'][0]['geometry']['location']['lat'], "longitude": data['results'][0]['geometry']['location']['lng']}
	else:
		final_result['status'] = "Error"
		final_result['description'] = 'Unknown Error'
	return final_result
#	return data


