import csv

f = open('subwayfee.csv') # csv 파일을 염
data = csv.reader(f) # csv 파일을 읽어 data에 저장
next(data) # 헤더 데이터 넘김

mx = [0]*4 # 크기가 4인 빈 배열 선언
mx_station = [" "]*4 # 크기가 4인 빈 배열 선언
label = ['유임승차','유임하차','무임승차','무임하차'] # 크기가 4인 배열 선언

for row in data : 
    for i in range(4,8) : # 4열 ~ 7열의 정보를
        row[i] = int(row[i]) # 정수형으로 바꿈
        if row[i] > mx[i-4] : # 승차인원이 가장 많은 역을 찾는 과정
            mx[i-4] = row[i] 
            mx_station[i-4] = row[3] +' '+ row[1] # '역이름' + ' ' + '호선' 
            
for i in range(4) : # 4번 반복
    print(label[i]+ ':' + mx_station[i], mx[i]) # 승차종류 : 역정보, 호선정보, 인원 출력