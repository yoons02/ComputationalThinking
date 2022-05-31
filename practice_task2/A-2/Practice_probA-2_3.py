# 탑승
import csv
import matplotlib.pyplot as plt

f = open('subwaytime.csv') # csv 파일을 염
data = csv.reader(f) # csv 파일을 읽어 data에 저장
next(data)
next(data) # 헤더 데이터 넘김

mx = [0]*24          # 승차 인원 저장 리스트 초기화
mx_station = [" "]*24   # 승차 인원 역 이름 저장 리스트 초기화
for row in data :
    row[4:] = map(int, row[4:]) # 4열부터 모두 정수형으로 바꿈
    for j in range(24) : # 시간 단위
        a = row[j*2+4]  # 변수 j와 인덱스 사이의 관계를 통한 승차 인원 값 추출 및 저장
        if a > mx[j] : # 모든 자료
            mx[j] = a
            mx_station[j] = row[3] # 역정보 저장
            
print(mx_station)
print(mx)