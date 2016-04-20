import urllib
import json
import urllib2
import pprint

#http://api.openweathermap.org/data/2.5/forecast/city?id={CITYID}&APPID={APIKEY}
#b374e3ec0654bb0ecf1de54662bead9e
weather = urllib2.urlopen('http://api.openweathermap.org/data/2.5/forecast/city?id=5374361&APPID=b374e3ec0654bb0ecf1de54662bead9e')
weather = json.loads(weather.read())

pprint.pprint(weather)
