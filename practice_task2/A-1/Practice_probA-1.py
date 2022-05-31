import csv
import matplotlib.pyplot as plt
import platform

f = open('subwayfee.csv')
data = csv.reader(f)
next(data)

mx = 0
rate = 0
mx_station = " "

for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    if row[6] != 0 and (row[4]+row[6]) > 100000 :
        rate = row[4] / (row[4]+row[6])
        if rate > mx :
            mx = rate
            mx_station = row[3] + ' ' + row[1]

print(mx_station, round(mx*100,2))

# 2
mx = [0]*4
mx_station = [" "]*4
label = ['유임승차','유임하차','무임승차','무임하차']

for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
        if row[i] > mx[i-4] :
            mx[i-4] = row[i]
            mx_station[i-4] = row[3] +' '+ row[1]
for i in range(4) :
    print(label[i]+ ':' + mx_station[i], mx[i])

# 3
if platform.system() == 'Darwin': #맥
        plt.rc('font', family='AppleGothic')

plt.rcParams['axes.unicode_minus'] = False #한글 폰트 사용시 마이너스 폰트 깨짐 해결

f = open('subwayfee.csv')
data = csv.reader(f)
next(data)

label = ['유임승차','유임하차','무임승차','무임하차']
c = ['#14CCC0', '#389993', '#FF1C6A', '#CC14AF']

for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    plt.figure(dpi=300)
    plt.title(row[3]+' '+row[1])
    plt.pie(row[4:8], labels=label, colors=c, autopct='%1.f%%')
    plt.axis('equal')
    plt.savefig(row[3]+' '+row[1]+'.png')
    plt.show()