import csv

f = open('subwaytime.csv') # csv 파일을 염
data = csv.reader(f) # csv 파일을 읽어 data에 저장
next(data) 
next(data) # 헤더 데이터 넘김

mx = 0 # 이용자수 저장 변수 초기화
mx_station = '' # 역정보, 호선정보 저장 변수 초기화

for row in data : 
    row[4:] = map(int, row[4:]) # 4열부터 모두 정수형으로 바꿈
    a = row[11:16:2] # 11, 13, 15
    if sum(a) > mx : # 출근 시간 때 이용자 수가 가장 많은 역을 찾는 과정
        mx = sum(a) # 출근 시간 때 이용자 수의 합
        mx_station = row[3]+'('+row[1]+')' # 역정보(호선정보)

print(mx_station, mx)