import numpy as np

def connection_indices(input_size, output_size, num_connections, ctype = "random"):
	indices = np.zeros((num_connections, output_size))

	if ctype == "random":
		indices = np.random.randint(0, input_size, size = (num_connections, output_size), dtype = np.int)

	return indices

def generate_patches(inp, patch_shape, step):
	input_shape = inp.shape
	patches = np.zeros((input_shape[0], input_shape[1]//step[0], input_shape[2]//step[1], patch_shape[0], patch_shape[1]))
	for i in range((input_shape[1] - patch_shape[0])//step[0]):
		for j in range((input_shape[2] - patch_shape[1])//step[1]):
			patches[:,i,j] = inp[:, i*step[0]:i*step[0]+patch_shape[0], j*step[1]:j*step[1]+patch_shape[1]]

	return patches
