import numpy as np

class 뉴런:
    def __init__(self, w, b):
        self.w = w
        self.b = b
        
    def predict(self, X):
        z = np.dot(X, self.w) + self.b
        y = np.where(z > 0, 1, -1)
        return y
    
class 퍼셉트론(뉴런):
    def __init__(self):
        뉴런.__init__(self, w=None, b=None)
        
    def fit(self, X, y, 학습횟수, 학습률):
        """학습"""
        # 가중치 초기화
        특징수 = X.shape[1]
        self.w = np.zeros(특징수)
        self.b = 0.
        # 학습
        error_history = []
        for _ in range(학습횟수):            
            종합오류 = 0
            for xi, yi in zip(X, y): # 각 샘플에 대해 ...
                yi_pred = self.predict(xi)
                error = yi - yi_pred
                종합오류 += error**2
                # 가중치 갱신
                delta = error * 학습률
                self.w += delta * xi
                self.b += delta
            error_history.append(종합오류)
        return error_history