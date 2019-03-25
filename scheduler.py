from db import movieConnector

class movie_list:
    def __init__(self):
        self.movies = []
        self.movieConnector = movieConnector()
        
    def add_movie(self, movie):
        self.movies.append(movie)
        self.movieConnector.append_movie(movie)

    def get_list(self):
        return self.movieConnector.get_movies()  

    def del_list(self, key):
        for i, n in enumerate(self.movies):
            if n.title == key:                  # self.key가 아니야. self라는 것은 해당 class 자체적으로 새로 정의될때 쓰는거야.
                del self.movies[i]    


class scheduler:
    def __init__(self):
        self.schedules = []

    def add_schedule(self, schedule):
        self.schedules.append(schedule)

    def get_schedule(self):
        sorted_schedules = sorted(self.schedules, key = lambda schedule:schedule.time)
        return sorted_schedules



          