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

# current_money = (money - 80000 - (9000*5) + 120000) + ((money - 80000 - (9000*5) + 120000) * 0.2) -(((money - 80000 - (9000*5) + 120000) + ((money - 80000 - (9000*5) + 120000) * 0.2))/3)
# print(f'현재 남은 금액은 {int(current_money)}원 입니다.')

#실습2
# intro = '둠칫'
# drop = '두둠칫'
# print(intro + drop *2 + intro)

# name = input('이름을 입력해 주세요:')
# score = int(input("정수를 입력하세요:"))
# print(f'이름은 {name}입니다.')
# print(f'입력한 정수는 {score}입니다.')

# a = int(input('첫 번째 값:'))
# b = int(input('두 번째 값:'))
# print(a + b)


# fruit = '사과 참외 수박'.split() #띄워쓰기를 기준으로 리스트로 만들어준다
# print(fruit)


# name = input('이름을 입력하세요:')
# age = int(input('나이를 입력하세요:'))
# print(f'안녕하세요. 저는 {name}이고, {age}살입니다.')

# x = int(input("가로 길이를 입력하세요:"))
# y = int(input('세로 길이를 입력하세요:'))
# print(f'넓이: {x*y}')
# print(f'둘레: {x*2 +y*2}')

# x = input('네 자릿수 정수를 입력하세요:')
# print(f'천의 자리: {x[0]}')
# print(f'백의 자리: {x[1]}')
# print(f'십의 자리: {x[2]}')
# print(f'일의 자리: {x[3]}')


# ymd = input('년, 월, 일을 입력해주세요:')
# hms = input('시, 분, 초를 입력해주세요:')
# y = ymd.split('.')[0]
# m = ymd.split('.')[1]
# d = ymd.split('.')[2]
# h = hms.split(':')[0]
# m = hms.split(':')[1]
# s = hms.split(':')[2]
# print(f'RE3의 개강일은 {y}년 {m}월 {d}일\n시작 시간은 {h}시 {m}분 {s}초입니다.')



#문자열을 리스트로
# list1 = list()
# strlist = list('codingOn')
# print(list1)
# print(strlist, '데이터 값 들어온거 확인용')# 이런느낌으로 디버깅

# #문제1
# nums = [10,20,30,40,50]
# print(nums[0])
# print(nums[-1])

# #문제2
# nums = [100,200,300,400,500,600,700]
# print(nums[2:5])

# #문제3
# nums = [1,2,3,4,5]
# print(nums * 2)

# #문제4
# items = ['a','b','c','d','e']
# print(items[::-1])

# #문제5
# data = ['zero', 'one', 'two', 'three', 'four', 'five']
# print(data[::2])

# #문제6
# movies = ['인셉션', '인터스텔라', '어벤져스', '라라랜드', '기생충']
# movies[2:4] = ['매트릭스', '타이타닉']
# print(movies)

# #문제7
# subjects = ['국어', '수학', '영어', '물리', '화학', '생물', '역사', '지구과학', '윤리' ]
# print(subjects[3:8:2])

# #문제8
# data = ['A','B','C','D','E','F','G','H','I']
# data1 = data[0:3]
# data2 = data[3:6]
# data3 = data[6:]
# print(data1[::-1], data2[::-1], data3[::-1])

# #문제1
# fruits = ['apple', 'banana', 'cherry', 'grape', 'watermelon','strawberry']
# del fruits[1:4]
# print(fruits)

# #문제2
# letters = ['A','B']
# letters = letters *3

# del letters[2]
# print(letters)

##스페셜 문제
# 사용자 입력 
# c1 = int(input('소비1:'))
# c2 = int(input('소비2:'))
# c3 = int(input('소비3:'))
# c4 = int(input('소비4:'))
# c5 = int(input('소비5:'))
# c6 = int(input('소비6:'))
# c7 = int(input('소비7:'))
# c8 = int(input('소비8:'))
# c9 = int(input('소비9:'))
# c10 = int(input('소비10:'))
# # 1단계: 10개 정수 data에 저장
# data = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]
# #2단계 : 리스트 수정
# data.append(int(5000))
# data.insert(0, int(3000))
# data.remove(0)
# #3단계: 부분 분석
# first5 = data[0:5]
# last5 = data[-5:]
# print(f'처음 5일: {first5}')
# print(f'처음 5일: {last5}')
# #4단계: 전체 소비 금액, 전체 평균 소비 금액, 처음 5일 평균 소비 금액을 출력. 마지막 5일 평균 소비 금액을 출력
# total = sum(data)
# total_avg = total/len(data)
# first5_avg = sum(first5)/len(first5)
# last5_avg = sum(last5)/len(last5)
# print(f'''총 소비: {total}
# 전체 평균: {total_avg}
# 처음 5일 평균: {first5_avg}
# 마지막 5일 퍙균: {last5_avg}''')
# #5단계 리스트 복사 및 추가 수정
# data_copy = data[:]
# data_copy.pop(0)
# data_copy.pop(-1)
# print(f'수정된 리스트: {data_copy}')
# print(f'수정된 리스트: {data}')



#문제 추가
data = []
while True:
    i = input('입력:').split(',')
    if len(i) == 1:
        if str(i) == 'END':
            break
        if int(i).isdigit():
            if int(i) >= 0:
                data.append(i)
            elif int(i) <0 :
                continue
        else:
            continue
    elif len(i) == 2:
        if int(i[0]) >= 0:
            data.append(i[0])
        else:
            continue

print(data)
    







