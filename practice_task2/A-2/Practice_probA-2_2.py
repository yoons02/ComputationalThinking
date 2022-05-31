import csv

f = open('subwaytime.csv') # csv 파일을 염
data = csv.reader(f) # csv 파일을 읽어 data에 저장
next(data) 
next(data) # 헤더 데이터 넘김

mx = 0 # 이용자수 저장 변수 초기화
mx_station = '' # 역정보, 호선정보 저장 변수 초기화

t = int(input('몇 시의 승차 인원이 가장 많은 역이 궁금하세요? : ')) # 시간 입력 후 t에 저장

for row in data :
    row[4:] = map(int, row[4:]) # 4열부터 모두 정수형으로 바꿈
    a = row[4+(t-4)*2]          # 인덱스와 승차시간 관계를 이용해 입력 받은 시각의 승차인원 추출 및 저장
    if a > mx :                 # 승차인원이 가장 많은 역과 인원을 찾는 과정
        mx = a                  # 가장 많을 때의 승차인원을 mx에 저장
        mx_station = row[3]+'('+ row[1]+')' # 역정보(호선정보)
print(mx_station, mx)           # 승차 인원이 가장 큰 역과 인원 수 출력
