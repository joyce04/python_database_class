import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

from perceptron import 퍼셉트론

iris = pd.read_csv('data/iris.data', header=None)

data = iris[:100]

y = data[4]
X = data.iloc[:, 0:4].values.astype('float32')

y = np.where(y == 'Iris-setosa', 1, -1)

X_train, X_test, y_train, y_test = train_test_split(X, y)

model = 퍼셉트론()

error_history = model.fit(X_train, y_train, 
                          학습횟수=10, 학습률=0.01)

plt.plot(error_history, 'go--')
plt.show()
