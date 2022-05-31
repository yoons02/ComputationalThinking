import csv
import matplotlib.pyplot as plt
import platform

if platform.system() == 'Darwin': # 한글 폰트 깨짐 해결을 위한 코드
        plt.rc('font', family='AppleGothic')

plt.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시 마이너스 폰트 깨짐 해결

f = open('subwaytime.csv') # csv 파일을 염
data = csv.reader(f) # csv 파일을 읽어 data에 저장
next(data)
next(data) # 헤더 데이터 넘김 

mx = [0] * 24        # 하차 인원 저장 리스트 초기화
mx_station = [''] * 24    # 하차 인원 역 이름 저장 리스트 초기화

for row in data :
    row[4:] = map(int, row[4:]) # 4열부터 모두 정수형으로 바꿈
    for j in range(24) : # 시간 단위
        b = row[5 + j * 2]  # 변수 j와 인덱스 사이의 관계를 통한 하차 인원 값 추출 및 저장
        if b > mx[j] : # 모든 자료
            mx[j] = b 
            mx_station[j] = row[3] + '( ' +str(j+4)+ ' 시)' # 역정보(시간)

plt.figure(dpi=70) # 크기 지정
plt.bar(range(24), mx, color='b')  # 막대그래프 속성 변경
plt.xticks(range(24), mx_station, rotation=90) # x축 (90도 돌림)
plt.show() # 화면 보여줌