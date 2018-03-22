# Request info from Google Maps API using python
# The code will Geolocation API location requests

import httplib2
import json

def getGeocodeLocation(inputString):
  google_api_key = "AIzaSyCDzpGohjYJuQ6q-ATjPFnJA-Q2QZnaf_E"
  locationString = inputString.replace(" ", "+")
  url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'%(locationString, google_api_key))
  h = httplib2.Http()
  response, content = h.request(url, 'GET')
  result = json.loads(content)
  print("response header: %s \n \n") % response
  result = json.loads(h.request(url,'GET')[1])
  latitude = result['results'][0]['geometry']['location']['lat']
  longitude = result['results'][0]['geometry']['location']['lng']
  return (latitude,longitude)

