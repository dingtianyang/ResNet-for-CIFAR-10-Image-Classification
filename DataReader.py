import os
import pickle
import numpy as np

"""This script implements the functions for reading data.
"""

def load_data(data_dir):
	"""Load the CIFAR-10 dataset.

	Args:
		data_dir: A string. The directory where data batches
			are stored.

	Returns:
		x_train: An numpy array of shape [50000, 3072].
			(dtype=np.float32)
		y_train: An numpy array of shape [50000,].
			(dtype=np.int32)
		x_test: An numpy array of shape [10000, 3072].
			(dtype=np.float32)
		y_test: An numpy array of shape [10000,].
			(dtype=np.int32)
	"""

	### YOUR CODE HERE
	x_train = []
	y_train = []
	for i in range(5):
		filename_train = data_dir + "data_batch_" + str(i + 1)

		with open(filename_train, 'rb') as fo:
			dict_train = pickle.load(fo, encoding='bytes')

		x = dict_train[b'data']
		y = np.array(dict_train[b'labels'])

		if i == 0:
			x_train = x
			y_train = y
		else:
			x_train = np.concatenate((x_train, x), axis=0)
			y_train = np.concatenate((y_train, y), axis=0)

	filename_test = data_dir + "test_batch"
	with open(filename_test, 'rb') as fo:
		dict_test = pickle.load(fo, encoding='bytes')

	x_test = dict_test[b'data']
	y_test = np.array(dict_test[b'labels'])

	x_train = x_train.astype(np.float32)
	y_train = y_train.astype(np.int32)
	x_test = x_test.astype(np.float32)
	y_test = y_test.astype(np.int32)
	### END CODE HERE

	return x_train, y_train, x_test, y_test

def train_valid_split(x_train, y_train, split_index=45000):
	"""Split the original training data into a new training dataset
	and a validation dataset.

	Args:
		x_train: An array of shape [50000, 3072].
		y_train: An array of shape [50000,].
		split_index: An integer.

	Returns:
		x_train_new: An array of shape [split_index, 3072].
		y_train_new: An array of shape [split_index,].
		x_valid: An array of shape [50000-split_index, 3072].
		y_valid: An array of shape [50000-split_index,].
	"""
	x_train_new = x_train[:split_index]
	y_train_new = y_train[:split_index]
	x_valid = x_train[split_index:]
	y_valid = y_train[split_index:]

	return x_train_new, y_train_new, x_valid, y_valid

