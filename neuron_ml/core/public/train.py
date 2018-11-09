"""
-----------------------------------------------------
Copyright © Arthur Guiot 2018. All rights reserved
-----------------------------------------------------

/core/public/train.py defines the 'train' method that
will train the model.

"""

def train(loaded, steps=1000):
	import os
	import subprocess
	import sys
	import tempfile
	import shutil
	import inspect
	import neuron_ml.tools.subprocess_checker as valid
	current_file = inspect.getfile(inspect.currentframe())
	script_dir = os.path.abspath(current_file + '../../../../script')

	script_createml = script_dir + '/CreateML/trainer.swift'
	script_tensorflow = script_dir + '/TensorFlow/retrain.py'

	method = loaded[1]
	path = loaded[0]
	output = []
	print("[Neuron - Train] Start training the model using the '" + method + "' method.")
	if method == "tensorflow":
		command = [
			sys.executable,
			script_tensorflow,
			'--image_dir',
			path,
			'--output_graph',
			path + '/retrained_graph.pb',
			'--output_labels',
			path + '/retrained_labels.txt',
			'--how_many_training_steps',
			str(steps)
		]
		process = subprocess.Popen(command, stdout=subprocess.PIPE)
		for line in iter(process.stdout.readline, b''):
			sys.stdout.write(line)
		output.extend([path + '/retrained_graph.pb', path + '/retrained_labels.txt'])
	elif method == "createml":
		if valid.command("swift"):
			command = [
				"swift",
				script_createml,
				path,
				path + '/ExportedModel.mlmodel'
			]
			process = subprocess.Popen(command, stdout=subprocess.PIPE)
			for line in iter(lambda: process.stdout.read(1), b''):
				sys.stdout.buffer.write(line)
			output.extend([path + '/ExportedModel.mlmodel'])
		else:
			raise ValueError("[Neuron - Train] ERROR: Swift must be installed on your machine. Check https://swift.org for details.")
			return
	else:
		raise ValueError("[Neuron - Train] ERROR: Wrong method. You have 2 options: 'tensorflow' or 'createml'.")
		return
	print("[Neuron - Train] Training is done.")
	return [path, method, output]
