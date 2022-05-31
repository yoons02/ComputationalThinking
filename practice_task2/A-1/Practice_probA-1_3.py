import csv
import matplotlib.pyplot as plt
import platform

if platform.system() == 'Darwin': # 한글 폰트 깨짐 해결을 위한 코드
        plt.rc('font', family='AppleGothic')

plt.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시 마이너스 폰트 깨짐 해결

f = open('subwayfee.csv') # csv 파일을 염
data = csv.reader(f) # csv 파일을 읽어 data에 저장
next(data) # 헤더 데이터 넘김

label = ['유임승차','유임하차','무임승차','무임하차'] # 크기가 4인 라벨 배열 지정
c = ['#14CCC0', '#389993', '#FF1C6A', '#CC14AF'] # 크기가 4인 색상 배열 지정

for row in data :
    for i in range(4,8) : # 4열 ~ 7열의 정보를
        row[i] = int(row[i]) # 정수형으로 바꿈
    plt.figure(dpi=150) # 크기 지정
    plt.title(row[3]+' '+row[1]) # 제목 : 역정보, 호선정보
    plt.pie(row[4:8], labels=label, colors=c, autopct='%1.f%%') # 원그래프
    plt.axis('equal') # 비율 일정
    plt.savefig(row[3]+' '+row[1]+'.png') # png파일 저장
    plt.show() # 화면 띄움