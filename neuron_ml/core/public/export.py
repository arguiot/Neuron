# -*- coding: utf-8 -*-
"""
-----------------------------------------------------
Copyright © Arthur Guiot 2018. All rights reserved
-----------------------------------------------------

/core/public/export.py defines the 'export' method that
will be used to export the trained model.

"""


def export(model, path, method="default"):
	import shutil
	import subprocess
	import sys
	global_path = model[0]
	technology = model[1]
	outputed_files = model[2]
	if technology == "tensorflow" and len(outputed_files) == 2:
		if method == "default" and type(path) == list:
			for i in range(len(outputed_files)):
				shutil.copy2(outputed_files[i], path[i])
		elif method == "tflite":
			import neuron_ml.tools.subprocess_checker as valid
			if valid.command("toco"):
				command = [
					"toco",
					"--graph_def_file",
					outputed_files[0],
					"--output_file",
					path,
					"--input_arrays",
					"Placeholder",
					"--output_arrays",
					"final_result"
				]
				print(" ".join(command))
				process = subprocess.Popen(command, stdout=subprocess.PIPE)
				for line in iter(lambda: process.stdout.read(1), b''):
					sys.stdout.buffer.write(line)
			else:
				raise ValueError(
					"[Neuron - Export] ERROR: TOCO not found. Please install TensorFlow's TOCO cli.")
				return
		elif method == "coreml":
			import tfcoreml as tf_converter
			tf_converter.convert(tf_model_path=outputed_files[0],
								 mlmodel_path=path,
								 output_feature_names=[
									 'final_result:0'],
								 image_input_names='input',
								 class_labels=outputed_files[1],
								 red_bias=-1,
								 green_bias=-1,
								 blue_bias=-1,
								 image_scale=2.0 / 299.0
								 )
		else:
			raise ValueError(
				"[Neuron - Export] ERROR: Wrong arguments. See the wiki for help.")
			return
	elif technology == "createml" and method == "default":
		shutil.copy2(outputed_files[0], path)
	else:
		raise ValueError(
			"[Neuron - Export] ERROR: Wrong arguments. See the wiki for help.")
		return
	print("[Neuron - Export] All file where exported.")
