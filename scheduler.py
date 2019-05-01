from db import movieConnector

class movie_list:
    def __init__(self):
        self.movies = []
        self.movieConnector = movieConnector()
        
        
    def add_movie(self, movie):
        self.movieConnector.append_movie(movie)
        
    def get_movie(self):
        return self.movieConnector.get_movies()

    def del_movie(self, key):
        for i, n in enumerate(self.movies):
            if n.title == key:                  # self.key가 아니야. self라는 것은 해당 class 자체적으로 새로 정의될때 쓰는거야.
                del self.movies[i]    


class schedule_list:
    def __init__(self):
        self.schedules = []
        self.movieConnector = movieConnector()

    def add_schedule(self, schedule):
        self.movieConnector.append_schedule(schedule)

    def get_schedule(self):
        return self.movieConnector.get_schedules()
        



          