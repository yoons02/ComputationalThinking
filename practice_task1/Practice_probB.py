from random import * # random 모듈로부터 모두 import
from math import sqrt # sqrt 함수를 사용하기 위해 math 모듈로부터 import

n = int(input("반복횟수를 입력하시오: ")) # 찍을 점의 개수 n을 입력

inside = 0 # 내부에 찍인 점의 개수를 0으로 초기화

for i in range(0, n): # 사용자로부터 입력받는 n 만큼 반복

    x = random() # 0~1 중 난수를 x에 할당

    y = random() # 0~1 중 난수를 y에 할당

    if sqrt(x*x+y*y) <= 1: # 원의 반지름이 1인 원의 방정식에 x, y값을 대입한다. 만약 1보다 작거나 같을 경우

        inside += 1 # inside 변수에 1을 추가해 나간다

pi = 4*inside/n # 시뮬레이션(몬테카를로법)을 이용한 원주율 계산식

print(pi) # 원주율 값 출력
