import matplotlib.pyplot as plt
import numpy as np
import time

WEAK = 0
DUMP = 50
SMART = 100
NORMAL = 200
STRONG = 300

def generate_random_wordl(N):
	return(np.random.choice([WEAK,NORMAL,STRONG],N*N,p=[0.4,0.5,0.1]).reshape(N,N))

def update(world):
	tam = world.size
	print(tam)

'''xseno = np.linspace(0,2*np.pi,50,0.1)
yseno = np.sin(xseno)
ycos = np.cos(xseno)'''
mundo = generate_random_wordl(20)
plt.imshow(mundo)
for x in range(10):
	update(mundo)
	plt.show()
	time.sleep(1)
#plt.plot(xseno,ycos)



