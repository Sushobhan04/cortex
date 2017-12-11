import numpy as np
import sys
import os

class Neurons(object):
	"""docstring for Neurons"""
	def __init__(self, size):
		super(Neurons, self).__init__()

		self.data = np.zeros(size)
		self.threshold = np.ones(size)

class Synapses(object):
	"""docstring for Synapses"""
	def __init__(self, sizes, sparse_dim):
		super(Synapses, self).__init__()

		self.data_size = sizes[0]
		self.label_size = sizes[1]
		self.hidden_size = sizes[2]

		self.input_size = np.sum(sizes)
		self.output_size = sizes[2]

		self.data = np.zeros(sparse_dim, sizes[2])
		self.indices = np.random.randint(np.output_size, size = (sparse_dim, sizes[2]))
		