from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint,EarlyStopping

import matplotlib.pyplot as plt
import numpy
import os
import tensorflow as tf

# seed 값 설정
seed = 0
numpy.random.seed(seed)
tf.random.set_seed(3)

# MNIST 데이터 불러오기
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()
# X_train, Y_class_train는 학습용, X_test, Y_class_test는 테스트용

X_train = X_train.reshape(X_train.shape[0], 784).astype('float32') / 255 
X_test = X_test.reshape(X_test.shape[0], 784).astype('float32') / 255 # 실수로 변환 후 255로 나눠 1차원으로 변환

Y_train = np_utils.to_categorical(Y_train, 10)
Y_test = np_utils.to_categorical(Y_test, 10) # 0, 1로만 이루어진 벡터로 변환

# 모델 프레임 설정
model = Sequential()
model.add(Dense(512, input_dim=784, activation='relu')) # 은닉층
model.add(Dense(10, activation='softmax')) # 출력층

# 모델 실행 환경 설정
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy']) # 딥러닝 실행 환경 설정

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
plt.legend(loc='upper right')
# plt.axis([0, 20, 0, 0.35])
plt.grid()
plt.xlabel('epoch') # x축
plt.ylabel('loss') # y 축
plt.show()