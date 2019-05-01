class schedule:
    def __init__(self, time, room, title, runtime, price):
        self.time = time
        self.room = room
        self.title = title
        self.runtime = runtime
        self.price = price

    def get_dict(self):
        return {
                    "time" : self.time,
                    "room" : self.room,
                    "title" : self.title,
                    "runtime" : self.runtime,
                    "price" : self.price
        }

class scheduleUtil:
    def parse(self, dict):
        return schedule(dict["time"],dict["room"], dict["title"], dict["runtime"], dict["price"])