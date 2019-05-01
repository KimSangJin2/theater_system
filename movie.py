class movie:
    def __init__(self, title, runtime):
        self.title = title
        self.runtime = runtime

    def get_dict(self):
        return {
                    "title" : self.title,
                    "runtime" : self.runtime
        }

class movieUtil:
    def parse(self, dict):
        return movie(dict["title"], dict["runtime"])    
