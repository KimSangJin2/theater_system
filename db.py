from pymongo import MongoClient    # 필요한 모듈은 1.pymongo  2.movie  3.movieutil(?)
from movie import movie
from movie import movieUtil



class movieConnector:               # DB와 연동되는 하나의 클래스를 만나자
                                    # 생성자: 연동 주소 / 기능1.디비 -> 코드 / 기능2. 코드(추가) -> 디비 
    def __init__(self):
        self.userId = "taling"
        self.password = "12345"
        self.connectString = "mongodb+srv://%s:%s@cluster0-iveco.mongodb.net/test?retryWrites=true" % (self.userId, self.password)

    def get_movies(self):
        client = MongoClient(self.connectString)   
        db = client.movieDb
        collection = db.movies                      

		# [{}, {}]   # 기존에는 <---- 처럼 리스트로 덮인 딕셔너리 구조임. 이를 class에 맞게 전환시켜줘야 해(그래야 이후 movie_list, scheduler가 잘 작동되겠지?).    
        movieCollection = collection.find({})       # 1. find로 디비에서 가져와
        util = movieUtil()                          ## movieutil은 movie파일 에서 새로 만든 class / 뒤에 parse를 끄집어내기 위함
        movies = []
        for movieDict in movieCollection:
            movie = util.parse(movieDict)           # 2. class 형식에 맞게 전환(이를 위해 parse를 만든 것)
            movies.append(movie)
        return movies



    def append_movie(self, movie):
        client = MongoClient(self.connectString)
        db = client.movieDb
        collection = db.movies
        movie_json = movie.get_dict()               # 몽고디비가 원하는 형식으로 전환(json)
        movies = collection.insert_one(movie_json)  # insert_one은 몽고디비에 추가해주는 공식
		# collection.close()


connector = movieConnector()
movies = connector.get_movies() 