# Geocoding-Proxy-Service
Maintainer: Urvi Desai

Version: 0.0.1

## Dependencies
urllib2, urllib, flask

## Used APIs

Geocoding Service by Google : <https://developers.google.com/maps/documentation/geocoding/start>

Geocoding Service by HERE: <https://developer.here.com/documentation/geocoder/topics/quick-start.html>

## Preparation
```git clone https://github.com/urvi8/Geocoding-Proxy-Service/```

## Running the service 

Get your API key for the services mentioned above. 

```export API_KEY=YOUR GMAP API KEY```

```export API_app_id=YOUR HERE API ID```

```export API_app_code=YOUR HERE API CODE```

```python main.py``` 

## Using the service
```127.0.0.1:5000/?address="ADDRESS YOU WANT TO KNOW "```

## API Endpoints
```?address```

## Returned Values

Example Response: 

```Latitude: ```

```Longitude: ```

```Method:  ```

```Status:  ```

## Using the APIs

The general procedure to use a service by API is:

1. Find the API service documentation.
2. Find out if a URL can retrieve the required data.
3. If so, sign up for an API key for the service.
4. Figure out the parameteres needed to include in the URL to get the required data.
5. Load the URL in your browser along with the parameters and check the response.
6. Repeat steps 4 and 5 until you get the desired response.

As mentioned above, the given service uses publically available API services from Google and HERE. The documentation is easy to understand with the provided elaborate examples.

Here is the example for the above procedure: 

1. Documentation: [Google](https://developers.google.com/maps/documentation/geocoding/start) 

2. URL can be found under 'Geocoding Request and Response' with an example address.

3. Sign up for your key.

4. Parameters: API_KEY provided upon signing up.

5. Load the URL with your unique API_KEY for the required address as given in the example.

This will bring up [JSON](https://www.json.org/) format text consisting of arrays and objects which can be utilized to obtain the desired data, which in this case is latitude and longitude.
