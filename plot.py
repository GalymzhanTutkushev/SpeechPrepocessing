
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,15,0.1)
y=np.cos(x)
a=[[1,2,3], [2,4,9]]
b=[5,8,3]
print(np.shape(a))
c=np.concatenate(a,b)
print(c)
plt.plot(x,y)
plt.show()
