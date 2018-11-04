import numpy as np

def cross_entropy_error(y_pred, y):
    delta = 1e-7
    batch_size = len(y)
    return -np.sum(y * np.log(y_pred + delta)) / batch_size

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    y = exp_a / np.sum(exp_a)
    return y

def softmax_batch(A):
    return np.apply_along_axis(softmax, 1, A)

class ReLu:
    def __init__(self):
        self.mask = None
        
    def forward(self, x):
        self.mask = x > 0
        out = np.where(self.mask, x, 0)
        return out
    
    def backward(self, dout):
        dx = np.where(self.mask, dout, 0)
        return dx

class Sigmoid:
    def __init__(self):
        self.out = None
        
    def forward(self, x):
        out = 1 / (1 + np.exp(-x))
        self.out = out
        return out
    
    def backward(self, dout):
        dx = dout * self.out * (1 - self.out)
        return dx

class Affine:
    def __init__(self, 입력수, 출력수):
        self.W = np.random.randn(입력수, 출력수)
        self.b = np.random.randn(출력수)
        self.X = None
        self.dW = None
        self.db = None
        
    def forward(self, X):
        self.X = X
        out = np.dot(X, self.W) + self.b
        return out
    
    def backward(self, dout):
        dX = np.dot(dout, self.W.T)
        self.dW = np.dot(self.X.T, dout)
        self.db = np.sum(dout, axis=0)
        return dX

class SoftmaxWithLoss:
    def __init__(self):
        self.y_pred = None
        self.y = None
        
    def forward(self, X, y):
        self.y = y
        self.y_pred = softmax_batch(X)
        loss = cross_entropy_error(self.y_pred, y)
        return loss
    
    def backward(self, dout=1):
        batch_size = len(self.y)
        dx = (self.y_pred - self.y) / batch_size
        return dx


class FeedForwardNetBackPropClassifier:
    def __init__(self):
        self.layers = []

    def add(self, layer):
        self.layers.append(layer)

    def predict(self, X):
        layer_output = X
        for layer in self.layers[:-1]:            
            layer_output = layer.forward(layer_output)

        return layer_output

    def compute_loss(self, X, y):
        y_pred = self.predict(X)
        loss = self.layers[-1].forward(y_pred, y)
        return loss

    def fit(self, X, y, batch_size, 훈련횟수, 학습률):
        loss_history = []
        for i in range(훈련횟수):
            print('훈련', i+1)
            # 1. Mini batch
            batch_indice = np.random.choice(len(X), batch_size)
            X_batch = X[batch_indice]
            y_batch = y[batch_indice]
            # 2. 경사 (Gradient) 산출
            #   1) 순전파
            self.compute_loss(X_batch, y_batch)
            #   2) 역전파
            dout = 1
            for layer in reversed(self.layers):
                dout = layer.backward(dout)

            # 3. 매개변수 갱신
            for layer in self.layers:
                if isinstance(layer, Affine):
                    layer.W -= layer.dW * 학습률
                    layer.b -= layer.db * 학습률

            loss = self.compute_loss(X_batch, y_batch)
            loss_history.append(loss)
            print('\tLoss:', loss)
        return loss_history
