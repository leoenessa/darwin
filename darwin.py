import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ON = 255
OFF = 0

def criaMundo(N):
	return(np.random.choice([ON,OFF],N*N,p=[0.5,0.5]).reshape(N,N))

def atualizaMundo(frameNum, world):
    if(world[0,0] == OFF):
    	world[0,0]=ON
    else:
    	world[0,0]=OFF

def main():

	fig1 = plt.figure()
	mundo = criaMundo(4)
	print(mundo)
	img = plt.imshow(mundo)

	animacao = animation.FuncAnimation(fig1, atualizaMundo, fargs=(mundo.all))

	plt.show()

if __name__ == '__main__':
	main()