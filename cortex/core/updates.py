import numpy as np 

def oja_update(x, y, w, delta = 0):
	_y = y - delta
	_i = x - _y*w

	update = _i*_y

	# print(update.shape)
	
	mean_update = np.mean(update, axis = 0)
	return mean_update