# Geocoding-Proxy-Service
Maintainer: Urvi Desai

Version: 0.0.1

## Dependencies
urllib2, urllib, flask

## Used API's

Geocoding Service by Google : <https://developer.here.com/documentation/geocoder/topics/quick-start.html>

Geocoding Service by HERE: <https://developers.google.com/maps/documentation/geocoding/start>

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

### Returned Values

Example Response: 

```Latitude: ```

```Longitude: ```

```Method:  ```

```Status:  ```
