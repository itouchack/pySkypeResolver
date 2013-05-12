import json
import urllib2

userName = raw_input('Username: ')

apiURL = urllib2.urlopen('http://54.214.64.71:8080/api/%s' % (userName))
for index in json.load(apiURL):
	print index['public'], index['local']