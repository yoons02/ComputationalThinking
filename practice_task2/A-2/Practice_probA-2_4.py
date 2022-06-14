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

s_in = [0] * 24     # 승차 인원 저장 리스트 초기화
s_out = [0] * 24    # 하차 인원 저장 리스트 초기화

for row in data :
    row[4:] = map(int, row[4:]) # 4열부터 모두 정수형으로 바꿈
    for i in range(24) :
        s_in[i] += row[4+i*2] # 승차 인원 누적해서 더함
        s_out[i] += row[5+i*2] # 하차 인원 누적해서 더함

plt.title('지하철 시간대별 승하차 인원 추이')  # 제목 추가
plt.plot(s_in, label='승차')             # 승차 인원을 꺾은선 그래프로 표현
plt.plot(s_out, label='하차')            # 하차 인원을 꺾은선 그래프로 표현
plt.legend()  # 범례 추가
plt.grid() # 그리드 추가
plt.xticks(range(24), range(4,28)) # 범위 지정
plt.show() # 화면 보여줌