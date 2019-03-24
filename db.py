from pymongo import MongoClient

client = MongoClient("mongodb://taling:12345@cluster0-shard-00-00-iveco.mongodb.net:27017,cluster0-shard-00-01-iveco.mongodb.net:27017,cluster0-shard-00-02-iveco.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
db = client.movieDb
collection = db.movies
for book in collection.find({"title":"오만과편견"}):
    print(book)


class movieConnector:
    def __init__(self):
        self.connectsString = 