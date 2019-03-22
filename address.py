class address:
    def __init__(self):
        self.movies = []
    
    def add_movie(self, movie):
        self.movies.append(movie)

    def get_list(self):
        return self.movies

    def get_schedule(self):
        sorted_movie = sorted(self.movies, key = lambda movie: movie.time)
        return sorted_movie

    def del_list(self, key):
        for i, n in enumerate(self.movies):
            if n.title == key:                  # self.key가 아니야. self라는 것은 해당 class 자체적으로 새로 정의될때 쓰는거야.
                del self.movies[i]

          