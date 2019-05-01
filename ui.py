from scheduler import movie_list, schedule_list
from movie import movie, movieUtil
from schedule import schedule, scheduleUtil


class ui:
    def __init__(self):                        # movie라는 입력값이 없는데 넣으면 에러뜸
        self.movie_list = movie_list()         # movie는 코드 설게시점에서 ui 안에서 정의되지 않아. 객체가 만들어지고 movie 생기지. 
        self.schedule_list = schedule_list()

    def run(self):
        print("기능을 선택하시오")
        print("1. 영화목록 입력")
        print("2. 영화목록 보기")
        print("3. 영화목록 삭제")
        print("4. 영화 스케줄표 입력")
        print("5. 영화 스케줄표 보기")

        while 1:                        # while == 1 이 아니야.
            op = input("번호를 입력하세요")
            if op == '1':
                m1 = self.input_movie()
                self.movie_list.add_movie(m1)
            if op == '2':
                for movie in self.movie_list.get_movie():
                    print(movie.title, movie.runtime)
            if op == "3":
                key = input("어떤 영화를 삭제하시겠습니까?")
                self.movie_list.del_movie(key)
            #schedule 입력
            if op == '4':
                s1 = self.input_schedule()
                self.schedule_list.add_schedule(s1)     
            #schedule 가져오기
            if op == '5':
                for schedule in self.schedule_list.get_schedule():  # 이런식으로도 수정할 수 있어.
                    print(schedule.time, schedule.title, schedule.room, schedule.runtime, schedule.price)


    def input_movie(self):                        #입력값 쓸 필요가 없지. input으로 넣을거니까
        inputtitle = input('제목:')
        inputtime = int(input('시간:'))
        return movie(inputtitle, inputtime)

    def input_schedule(self):
        inputtime = int(input('시간: '))
        inputroom = input('상영관: ')
        inputmovie = input('영화: ')
        inputprice = int(input("가격: "))
        for movie in self.movie_list.get_movie():
            if movie.title == inputmovie:
                title = movie.title
                runtime = movie.runtime
        return schedule(inputtime, inputroom, title, runtime, inputprice)

    def reservation(self):
        reserv_movie = input("예매하실 영화를 선택하시오. : ")
        reserv_time = input("시간을 선택하시오. : ")
        reserv_number = int(input("인원을 선택하시오. : "))
        
        for schedule in self.schedule_list.get_schedule():
            if schedule.title == reserv_movie:
                reserv_price = schedule.price

        total_price = reserv_number*reserv_price

        print("%s, %s시, %s매 예매되었습니다. 가격은 총 %s원 입니다." % (reserv_movie, reserv_time, reserv_number, total_price)) 
        
        