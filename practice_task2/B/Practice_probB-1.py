from keras.datasets import mnist
from keras.utils import np_utils

import numpy
import sys
import tensorflow as tf

# seed 값 설정
seed = 0
numpy.random.seed(seed)
tf.random.set_seed(3)

# MNIST 데이터셋 불러오기
(X_train, Y_class_train), (X_test, Y_class_test) = mnist.load_data()
# X_train, Y_class_train는 학습용, X_test, Y_class_test는 테스트용

print("학습셋 이미지 수 : %d 개" % (X_train.shape[0])) # 60,000
print("테스트셋 이미지 수 : %d 개" % (X_test.shape[0])) # 10,000

# 그래프로 확인
import matplotlib.pyplot as plt
plt.imshow(X_train[0], cmap='Greys') # 이미지 흑백으로 설정
plt.show() # 이미지 보여줌

# 코드로 확인
for x in X_train[0]: # X_train[0]는 784픽셀
    for i in x:
        sys.stdout.write('%d\t' % i) # 밝기에 따라 0~255까지 나타냄
    sys.stdout.write('\n')

# 차원 변환 과정 
X_train = X_train.reshape(X_train.shape[0], 784) # 1차원으로 변환
X_train = X_train.astype('float64') # 나눗셈 위해 실수형으로 변환
X_train = X_train / 255 # 0~255를 0~1로 변환

X_test = X_test.reshape(X_test.shape[0], 784).astype('float64') / 255 # 위의 과정과 같음

# 클래스 값 확인
print("class : %d " % (Y_class_train[0])) 

# 바이너리화 과정
Y_train = np_utils.to_categorical(Y_class_train, 10)
Y_test = np_utils.to_categorical(Y_class_test, 10) # 0, 1로만 이루어진 벡터로 변환

print(Y_train[0]) # 변환된 값 출력