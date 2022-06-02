from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.callbacks import ModelCheckpoint,EarlyStopping

import matplotlib.pyplot as plt
import numpy
import os
import tensorflow as tf

# seed 값 설정
seed = 0
numpy.random.seed(seed)
tf.random.set_seed(3)

# 데이터 불러오기
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()
# X_train, Y_class_train는 학습용, X_test, Y_class_test는 테스트용

X_train = X_train.reshape(X_train.shape[0], 28, 28, 1).astype('float32') / 255 
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1).astype('float32') / 255 # 실수로 변환 후 255로 나눠 1차원으로 변환
Y_train = np_utils.to_categorical(Y_train)
Y_test = np_utils.to_categorical(Y_test) # 0, 1로만 이루어진 벡터로 변환

# 컨볼루션 신경망 설정
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), input_shape=(28, 28, 1), activation='relu'))
model.add(Conv2D(64, (3, 3), activation='relu'))
# Conv2D(A, B, C, D)
# A : 마스크 개수, B : kernel 크기 (a*b), C : input_shape(row, col, color), D : 활성화 함수

model.add(MaxPooling2D(pool_size=2))
# MaxPooling2D : 한번 더 축소, 2배 축소

model.add(Dropout(0.25))
# Dropout : 노드 일부 꺼줌, 0.25 : 25%

model.add(Flatten())
# 1차원으로 변환

model.add(Dense(128, activation='relu'))
# 은닉층 128개

model.add(Dropout(0.5)) 
# 노드 50% dropout

model.add(Dense(10, activation='softmax'))
# 출력층 10개

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# categorical_crossentropy : 오차함수, adam : 최적화 함수

# 모델 최적화 설정
MODEL_DIR = './model/' # 모델 저장 폴더
if not os.path.exists(MODEL_DIR): # 만일 위의 폴더가 존재하지 않으면
    os.mkdir(MODEL_DIR) # 이 이름의 폴더를 만들어 줌

modelpath="./model/{epoch:02d}-{val_loss:.4f}.hdf5"
checkpointer = ModelCheckpoint(filepath=modelpath, monitor='val_loss', verbose=1, save_best_only=True)
# checkpointer에 모니터 할 값 지정, val_loss에는 오차값 지정됨

early_stopping_callback = EarlyStopping(monitor='val_loss', patience=10)
# 10회 이상 성과 향상이 없으면 자동으로 중단

# 모델의 실행
history = model.fit(X_train, Y_train, validation_data=(X_test, Y_test), epochs=30, batch_size=200, verbose=0, callbacks=[early_stopping_callback,checkpointer])
# 샘플 200개를 각각 30번 실행

# 테스트 정확도 출력
print("\n Test Accuracy: %.4f" % (model.evaluate(X_test, Y_test)[1]))

# 테스트셋의 오차
y_vloss = history.history['val_loss']

# 학습셋의 오차
y_loss = history.history['loss']

# 그래프로 표현
x_len = numpy.arange(len(y_loss))
plt.plot(x_len, y_vloss, marker='.', c="red", label='Testset_loss')
plt.plot(x_len, y_loss, marker='.', c="blue", label='Trainset_loss')

# 그래프에 그리드를 주고 레이블을 표시
plt.legend(loc='upper right') # 범례 우측 상단 위치
plt.grid() 
plt.xlabel('epoch') # x축
plt.ylabel('loss') # y축
plt.show()