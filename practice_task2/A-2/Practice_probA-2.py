# 1
import csv
f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)
mx = 0
mx_station = ''
for row in data :
    row[4:] = map(int, row[4:])
    a = row[11:16:2]    #하차 인원 값 추출하기
    if sum(a) > mx :
        mx = sum(a)
        mx_station = row[3]+'('+row[1]+')'
print(mx_station, mx)

# 2
import csv
import matplotlib.pyplot as plt

f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)
mx = [0] * 24              # 시간대별 최대 승차 인원을 저장할 리스트 초기화
mx_station = [''] * 24     # 시간대별 최대 승차 인원 역 이름을 저장할 리스트 초기화

for row in data :
    row[4:] = map(int, row[4:])
    for j in range(24) :
        b = row[5 + j * 2]   # j값과 인덱스 번호 값의 관계식 사용
        if b > mx[j] :
            mx[j] = b
            mx_station[j] = row[3] + '( ' +str(j+4)+ ' )'

plt.rc('font',family='Malgun Gothic')
plt.bar(range(24), mx, color='b')    # 막대그래프 속성 변경
plt.xticks(range(24), mx_station, rotation=90)
plt.show()