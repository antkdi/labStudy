import numpy as np
import matplotlib.pyplot as plt

#Data Set
x = np.arange(0,6,0.1); # 0 부터 6까지 0.1 간격으로 생성
y = np.sin(x)

#Generate Graph
plt.plot(x,y)
plt.show()

