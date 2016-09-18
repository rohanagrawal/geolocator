import urllib2
import json

api = 'c2aa5441d10de514faef5c4ce55dd86b439076c6'

url = 'http://api.locu.com/v1_0/venue/search/?'



def locu_search(query):
    local = query
    locality = local.replace(' ', '%20')

    new_url = url + 'api_key=' + api + '&locality=' + locality

    obj = urllib2.urlopen(new_url)
    data = json.load(obj)

    # for abc in data['objects']:
    #     print abc['name']

    print data