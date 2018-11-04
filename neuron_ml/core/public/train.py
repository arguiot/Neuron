"""
-----------------------------------------------------
Copyright © Arthur Guiot 2018. All rights reserved
-----------------------------------------------------

/core/public/train.py defines the 'train' method that
will train the model.

"""

def train(loaded):
	import os
	import subprocess
	import sys
	import tempfile
	import shutil
	import inspect

	current_file = inspect.getfile(inspect.currentframe())
	script_dir = os.path.abspath(current_file + '../../script')

	script_createml = script_dir + '/CreateML/trainer.swift'
	script_tensorflow = script_dir + '/TensorFlow/retrain.py'

	method = loaded[1]
	path = loaded[0]
	output = []
	if method == "tensorflow":
		command = [
			sys.executable,
			script_tensorflow,
			'--image_dir',
			path,
			'--output_graph',
			path + '/retrained_graph.pb',
			'--output_labels',
			path + '/retrained_labels.txt'
		]
		process = subprocess.Popen(command, stdout=subprocess.PIPE)
	    for line in iter(process.stdout.readline, b''):
	        sys.stdout.write(line)
		output.extend([path + '/retrained_graph.pb', path + '/retrained_labels.txt'])
	else if method == "createml":

	else:
		raise ValueError("[Neuron - Train] ERROR: Wrong method. You have 2 options: 'tensorflow' or 'createml'.")
		return
	return [path, method, output]
