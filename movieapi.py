from pymongo import MongoClient

client = MongoClient('localhost', 38897)
db = client.movie_test
collection = db.douban25

all = collection.find( { } )

def getValue():
	return all
