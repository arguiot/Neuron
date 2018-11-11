"""
-----------------------------------------------------
Copyright © Arthur Guiot 2018. All rights reserved
-----------------------------------------------------

/core/public/labels.py defines the 'labels' method that
will be used to load labels from a file for the
'classify' method.

"""

def labels(model):
	if model[1] == "tensorflow":
		import tensorflow as tf

		label_file = model[2][1]

		label = []
		proto_as_ascii_lines = tf.gfile.GFile(label_file).readlines()
		for l in proto_as_ascii_lines:
			label.append(l.rstrip())
		print("[Neuron - Labels] " + len(label) + " labels were loaded.")
		return label
	else:
		raise ValueError("[Neuron - Graph] ERROR: Only TensorFlow trained model are accepted.")
		return
