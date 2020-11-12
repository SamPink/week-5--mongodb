from pymongo import MongoClient
import requests
import json

class mongo:
    def __init__(self):
        self.client = MongoClient()
        self.mydb = self.client["wikidatabase"]
        self.mycol = self.mydb["wiki"]

    def store(self, dict):
        self.mycol.insert_one(dict)
    
    def get(self, name):
        myquery = { "ArticleName": name }
        mydoc = self.mycol.find(myquery)
        for x in mydoc:
            print(x)

def getWiki(term):
    url = 'https://en.wikipedia.org/api/rest_v1/page/summary/{}'.format(term)
    j = requests.get(url).json()
    data = {}
    if j['title'] == 'Not found.':
        return json.dumps(data)
    data['ArticleName'] = j['title']
    data['pageId'] = j['pageid']
    data['imageURL'] = j['originalimage']['source']
    data['lang'] = j['lang']
    data['description'] = j['description']
    data['url'] = j['content_urls']['desktop']['page']
    data['info'] = j['extract']
    return json.dumps(data)

database = mongo()

#thing = json.loads(getWiki('Banana'))
#database.store(thing)

database.get('Banana')



