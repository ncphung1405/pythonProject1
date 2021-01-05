import random
import numpy as np
n=random.randrange(50,1001)
print(n,'Giải độc đắc là!','\n')
a=list(np.random.randint(-1000,1000, size=n))
print('Các giải khuyến khích!')
print(a,'\n')
b=list(np.random.uniform(-1000,1000, size=n))
print('Chúc các bạn may mắn lần sau!')
print(b)