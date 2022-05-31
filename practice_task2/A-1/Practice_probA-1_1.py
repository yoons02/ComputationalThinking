import csv

f = open('subwayfee.csv') # csv 파일을 염
data = csv.reader(f) # csv 파일을 읽어 data에 저장
next(data) # 헤더 데이터 넘김

mx = 0 
rate = 0
mx_station = " " # 빈 값들 지정

for row in data :
    for i in range(4,8) : # 4열 ~ 7열의 정보를
        row[i] = int(row[i]) # 정수형으로 바꿈
    if row[6] != 0 and (row[4]+row[6]) > 100000 : # 100,000명 이상인 경우에만
        rate = row[4] / (row[4]+row[6]) # rate = 유임승차인원 / 전체인원
        if rate > mx : # 비율이 가장 높은 역을 찾는 과정
            mx = rate # 비율이 가장 높을 때의 값을 mx에 저장
            mx_station = row[3] + ' ' + row[1] # '역이름' + ' ' + '호선' 

print(mx_station, round(mx*100,2)) # 역정보, 호선정보, 유임승차비율 출력