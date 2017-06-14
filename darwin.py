import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

ON = 255
OFF = 0

def criaMundo(N):
	return(np.random.choice([ON,OFF],N*N,p=[0.5,0.5]).reshape(N,N))
	

def atualizaMundo(frameNum,N,mundo,img):
	total = 0
	new_mundo = mundo.copy()
	for linha in range(new_mundo.shape[0]):
		for col in range(new_mundo.shape[1]):
			if(new_mundo[linha,col]==0):
				total+=1
	new_mundo = np.random.choice([ON,OFF],N*N,p=[0.5,0.5]).reshape(N,N)
	img.set_data(mundo)
	#mundo[:]=new_mundo[:]
	#mundo=new_mundo
	mundo = new_mundo.copy()
	print(mundo)
	print(new_mundo)
	print(total)
	return(img,)

def main():
	try:		
		N = 4
		mundo = criaMundo(N)
		print(mundo)
		fig1,ax = plt.subplots()
		img = ax.imshow(mundo)
		animacao = animation.FuncAnimation(fig1, atualizaMundo, fargs=(N,mundo,img,), blit=True)
		plt.show()
	except Exception as ex:
		print("DEU MERDA AQUI FORA!")

if __name__ == '__main__':
	try:
		main()
	except Exception as fuyck:
		pass
