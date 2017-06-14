import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

ON = 255
OFF = 0

def criaMundo(N):
	#return(np.random.choice([ON,OFF],N*N,p=[0.5,0.5]).reshape(N,N))
	return(np.random.choice([ON,OFF],N*N,p=[0.5,0.5]).reshape(4,4))

def atualizaMundo(mundo,N):
    mundo = np.random.choice([ON,OFF],N*N,p=[0.3,0.7].reshape(4,4))
    return mundo

def main():

	N = 4
	mundo = criaMundo(N)
	fig1,ax = plt.subplots()
	img = ax.imshow(mundo)
		
	animacao = animation.FuncAnimation(fig1, atualizaMundo, (mundo,N,))
	
	plt.show()

if __name__ == '__main__':
	main()
