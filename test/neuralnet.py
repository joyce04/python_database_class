import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    y = exp_a / np.sum(exp_a)
    return y

def softmax_batch(A):
    return np.apply_along_axis(softmax, 1, A)

def cross_entropy_error_batch(y_pred, y):
    delta = 1e-7
    batch_size = len(y)
    return -np.sum(y * np.log(y_pred + delta)) / batch_size

def numerical_gradient(f, x):
    h = 1e-4
    기울기 = np.zeros_like(x)
    
    # 편미분: 각 축별로 미분 수행
    for idx in range(len(x)):
        val = x[idx]
        # f(x+h)
        x[idx] = val + h
        fxh1 = f(x) 
        # f(x-h)
        x[idx] = val -h
        fxh2 = f(x)
        # 수치 미분
        기울기[idx] = (fxh1 - fxh2) / (2*h)
        
    return 기울기

def numerical_gradient_batch(f, X):
    if X.ndim == 1:
        return numerical_gradient(f, X)
    
    기울기 = np.zeros_like(X)
    for idx, x in enumerate(X):
        기울기[idx] = numerical_gradient(f, x)
    return 기울기

class Layer:
    def __init__(self, 입력수, 출력수, 활성화):
        self.W = np.random.randn(입력수, 출력수)
        self.b = np.random.randn(출력수)
        self.activation = 활성화
        
    def forward(self, X):
        z = np.dot(X, self.W) + self.b
        return self.activation(z)

class FeedForwardNet:
    def __init__(self, 손실함수):
        self.layers = []
        self.loss_func = 손실함수
        
    def add(self, layer):
        self.layers.append(layer)
        
    def predict(self, X):
        """신경망 순전파"""
        layer_output = X
        for layer in self.layers:
            layer_output = layer.forward(layer_output)            
        y = layer_output
        return y

    def 손실산출(self, X, y):
        y_pred = self.predict(X)
        loss = self.loss_func(y_pred, y)
        return loss
    
    def fit(self, X, y, 학습횟수, 학습률, 배치크기):
        loss_history = []
        for i in range(학습횟수):
            print('훈련', i+1)
            # 1. 미니 배치
            미니배치_색인 = np.random.choice(len(X), 배치크기)
            X_batch = X[미니배치_색인]
            y_batch = y[미니배치_색인]
            # 2. W, b에 대한 기울기 산출
            기울기 = []
            for layer in self.layers:
                f = lambda W: self.손실산출(X_batch, y_batch)
                dW = numerical_gradient_batch(f, layer.W)
                db = numerical_gradient_batch(f, layer.b)
                기울기.append((dW, db))
            # 3. 매개변수 갱신
            for layer, (dW, db) in zip(self.layers, 기울기):
                layer.W -= dW * 학습률
                layer.b -= db * 학습률
            # 4. 손실 수집
            loss = self.손실산출(X_batch, y_batch)
            loss_history.append(loss)
            print('\t손실:', loss)

        return loss_history