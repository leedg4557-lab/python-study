# x,y = 1, 2
# x,y = y, x
# print(x,y)


# a = 1
# b = 3.14
# c = '안녕'
# d = True

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))


# #가능한 경우
# print(int(3.7)) # 소수점 이하 절삭
# print(int("10")) # 10
# print(int(True)) # 1
# print(int(False)) # 0

# #불가능한 경우
# print(int("3.14")) #invalid literal
# print(int("abc"))

#{} 중괄호 활용법 앞에다가 f를 넣어줘야됨
# cat = '고양이'
# age = 15
# gender = '수컷'
# name = '꽁꽁이'
# skill = '냥냥 펀치'

# print(f'우리집 {cat}는 나이가{age}살이고 성별은{gender}입니다.\n이름은 {name}이고 주특기는 {skill}입니다.')


#영화 제목, 상영 상태(상영중), 개봉 날짜, 줄거리, 장르, 국가, 평점(실관람객 평점은 플롯으로 선언하고 스트링으로 변환해서 보여준다, 네티즌 평점), 순위, 누적,관객수
#실행 후 캡쳐 업로드 print코드는 복사해서 준 리더님께 보내기
# movie_name = '아바타: 불과 재'
# current_stae = '상영중'
# open_date = '2025.12.17'
# summary= """판도라를 위협하는 재의 부족, 더 이상 인간만이 적이 아니다! 
# 모두의 운명을 뒤흔들 거대한 전투가 시작된다! 
# 인간들과의 전쟁으로 첫째 아들 ‘네테이얌’을 잃은 후, ‘제이크’와 ‘네이티리’는 깊은 슬픔에 빠진다. 
# 상실에 빠진 이들 앞에 '바랑'이 이끄는 재의 부족이 등장하면서, 판도라는 더욱 큰 위험에 빠지게 되고, 
# ‘설리’ 가족은 선택의 기로에 서게 되는데…"""
# genre = 'SF'
# national = '미국'
# people_score = 8.95
# netizen_score = 8.15
# score = '1위'
# people_sum = '417만명'
# print(f'영화제목은 {movie_name}이고 현재 상영 상태는 {current_stae}이며 개봉 날짜는 {open_date}이다.\n영화의 줄거리는 {summary}이며 장르는 {genre}이다.\n제작한 국가는 {national}이다.\n실관람객 평점은{str(people_score)}이며 네티즌 평점은 {str(netizen_score)}이다.\n현재 누적 관객수는 {people_sum}이며 현재 박스 오피스 {score}이다. ')
# print(type(people_score))


# 나에대해 소개하기 변수 20개 선언
# age = 26
# tti = '용'
# name = '이동재'
# birth = '9월 6일'
# blood_type = 'AB'
# mbti = 'ISTP'
# middle_school = '장안중'
# high_school = '신정고'
# university = '한국 항공대'
# major = '전자정보공학부'
# current = '졸업 예정'
# home_town = '부산'
# live_local = '상암동'
# love_city = '대전'
# best_food = '치킨'
# worst_food = '홍합'
# best_color = '빨간색'
# worst_color = '노란색'
# hobby_1= '헬스'
# hobby_2= '잠자기'
# print(f"""저는 {age}살 {tti}띠 {name}입니다.
# 저의 중학교는 {middle_school}이며 고등학교는 {high_school} 대학교는 {university}입니다.
# 과는 {major}이며 현재 {current}입니다.\n저는 {home_town}에서 태어났으며 현재{live_local}에 거주하고 있으며 가장 좋아하는 도시는 {love_city}입니다.
# 저가 가장 좋아하는 음식은 {best_food}, 가장 싫어하는 음식은 {worst_food}입니다.
# 저가 가장 좋아하는 색깔은 {best_color}, 가장 싫어하는 음식은 {worst_color}입니다.
# 저는 쉴때 {hobby_1}와 {hobby_2}를 좋아합니다.""")

#12월 31일 수업 실습1
# money = 300000

current_money = (money - 80000 - (9000*5) + 120000) + ((money - 80000 - (9000*5) + 120000) * 0.2) -(((money - 80000 - (9000*5) + 120000) + ((money - 80000 - (9000*5) + 120000) * 0.2))/3)
print(f'현재 남은 금액은 {int(current_money)}원 입니다.')