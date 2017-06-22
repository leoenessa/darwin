import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

ON = 255 #forte
OFF = 0  #fraco

def criaMundo(N):
	return(np.random.choice([ON,OFF],N*N,p=[0.5,0.5]).reshape(N,N))
	

def atualizaMundo(frameNum, mundo,N,img):
	new_mundo = mundo.copy()
	total = 0
	for l in range(new_mundo.shape[0]):
		for c in range(new_mundo.shape[1]):
			total= (new_mundo[(l-1)%N,(c-1)%N]+new_mundo[(l-1)%N,c]+new_mundo[(l-1)%N,(c+1)%N]+
			new_mundo[l,(c-1)%N]+new_mundo[l,(c+1)%N]+
			new_mundo[(l+1)%N,(c-1)%N]+new_mundo[(l+1)%N,c]+new_mundo[(l+1)%N,(c+1)%N])	
			'''
			Se for forte (ON) mas houver outro forte ao lado, se torna fraco.
			Se for fraco e houver no maximo um forte, se torna forte
			'''
			if(new_mundo[l,c]==ON):
				if(total>=ON):
					new_mundo[l,c]=OFF
			else:
				if(total<=ON):
					new_mundo[l,c]=ON
				else:
					pass
					#print("%d: %d"%(total,int(new_mundo[l,c])))

	mundo[:]=new_mundo[:]
	img.set_data(mundo)
	return(img,)

def main():
	try:		
		N = 50
		mundo = criaMundo(N)
		print(mundo)
		fig1,ax= plt.subplots()
		img = ax.imshow(mundo)
		animacao = animation.FuncAnimation(fig1, atualizaMundo, fargs=(mundo,N,img,), blit=True)
		plt.show()
	except Exception as ex:
		 print(str(ex))

if __name__ == '__main__':
	try:
		main()
	except Exception as fuyck:
		pass
