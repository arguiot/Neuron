# -*- coding: utf-8 -*-
"""
-----------------------------------------------------
Copyright © Arthur Guiot 2018. All rights reserved
-----------------------------------------------------

/core/public/load.py defines the 'load' method that
will be used to prepare data for training.

"""

def load(dataset, method="tensorflow"):
	import os
	import tempfile
	import shutil
	import neuron_ml.core.data as data

	def createDir():
		return tempfile.mkdtemp()


	if method == "tensorflow":
		# Prepare and load for TensorFlow
		temp = createDir()
		data.tensorflow.organise_dataset(dataset, temp)
		return [temp, method]
	elif method == "createml":
		# Prepare and load data for CreateML
		temp = createDir()
		data.createml.organise_dataset(dataset, temp)
		return [temp, method]
	else:
		raise ValueError("[Neuron - Load] ERROR: Wrong method. You have 2 options: 'tensorflow' or 'createml'.")
		return
