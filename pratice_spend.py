    logs = []
    x = input('입력하세요:')
    
    if x == 'END':
        break

    if ',' in x:
        log = x.split(',')[0]
    else:
        log = x
    
    if log.isdigit():
        logs.append(int(log))

#2단계 기본 분석
print(f'''유효 소비: {logs}
소비 횟수: {len(logs)}
평균 소비: {sum(logs)}
평균 소비: {sum(logs)/len(logs)}''')
average = sum(logs)/len(logs)
#3단계 고급 조건 분석
more_co = []
for l in logs:
    if l > average:
        more_co.append(l)
print(f'평균 초과 소비: {more_co}')

cont_co = [logs[0]]
for l in logs[1:]:
    if l > cont_co[-1]:
        cont_co.append(l)
    else:
        break
print(f'연속 증가 구간: {cont_co}')

#4단계 패턴 분석:
under_5000 = []
same_up_5000 = []
for l in logs:
    if l >= 5000:
        same_up_5000.append(l)
    else:
        under_5000.append(l)
print(f'''5000 미만: {under_5000}
5000 이상: {same_up_5000}''')

#최빈값 찾기
from collections import Counter

dic_logs = Counter(logs)
max_value = max(dic_logs.values())
for k,v in dic_logs.items():
    if v == max_value:
        print (f'최빈 소비 금액: {k}')
        break
sort_logs = sorted(logs)
re_sort_logs = sorted(logs, reverse =True)
print(f'''오름차순: {sort_logs}
내림차순: {re_sort_logs}
원본: {logs}''')