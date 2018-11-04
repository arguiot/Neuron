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
	from neuron_ml import core.data as data

	if method == "tensorflow":
		# Prepare and load for TensorFlow
	else if method == "createml":
		# Prepare and load data for CreateML
	else:
		raise ValueError("[Neuron - Load] ERROR: Wrong method. You have 2 options: 'tensorflow' or 'createml'.")
		return
