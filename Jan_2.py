#1월 2일
#튜플 언패킹

# a, b, c =(1, 2, 3)
# #리스트 언패킹
# d, e, f = [4, 5, 6]

# #문자열 언패킹
# g,h = 'ok'
# #결과 출력
# print(a,b,c, '튜플')
# print(d,e,f, '리스트 언패킹')
# print(g,h, '문자열 언패킹')


# # 튜플 수정 방법1 첫번째 요소를 100으로 바꾸기 위한거
# t = (1,2,3)
# new_t = (100,) +t[1:]
# print(new_t)
# #두번째 방법 리스트로 변환 후 다시 변환
# temp = list(t)
# temp[1] = 200
# t = tuple(temp)
# print(t)


# #튜플 실습1

# user = ('minji', 25, 'Seoul')

# #고객 이름을 eunji로 변경
# user_list = list(user)
# user_list[0] = 'eunji'
# restored_user = tuple(user_list)
# print(restored_user)

# name, age, city = restored_user
# print(name,age,city)

# if city == 'Seoul':
#     print('서울 지역 보안 정책 적용 대상입니다.')
# else:
#     print('일반 지역 보안 정책 적용 대상입니다.')

# users = ('minji', 'eunji', 'soojin', 'minji', 'minji')
# print(users.count('minji'))
# print(users.index('soojin'))

# list_users = list(users)
# sorted_users = sorted(list_users)
# print(sorted_users)


# 집합 생성
# a = {1,2,3}
# b = {3,4,5} #중복 허용 안함
# print(a | b) #합집합
# print(a&b)
# print(a - b)
# print(a^b) #a,b에 하나만 있는 원소 들어감 


#집합 실습
submissions = ['kim', 'lee', 'kim', 'park', 'choi', 'lee', 'lee']

print(f'제출한 학생 수: {len(set(submissions))}')
print(f'제출자 명단: {set(submissions)}')

user1 = {'SF', 'Action', 'Drama'}
user2 = {'Drama', 'Romance', 'Action'}
print(f'''공통 관심 장르: {user1 & user2}
서로 다른 장르: {user1 ^ user2}
전체 장르: {user1 | user2}''')

my_certi = {'SQL', 'Python', 'Linux'}
job_re = {'SQL', 'Python'}
print(f'지원 자격 충족 여부: {my_certi.issuperset(job_re)}')