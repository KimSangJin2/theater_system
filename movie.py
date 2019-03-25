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

class schedule:
    def __init__(self, time, room, title, runtime):
        self.time = time
        self.room = room
        self.title = title
        self.runtime = runtime



    
    
