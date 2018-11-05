"""
-----------------------------------------------------
Copyright © Arthur Guiot 2018. All rights reserved
-----------------------------------------------------

/core/public/export.py defines the 'export' method that
will be used to export the trained model.

"""
def export(model, path, method="default"):
	import shutil
	global_path = model[0]
	technology = model[1]
	outputed_files = model[2]
	if technology == "tensorflow":
		if method == "default" and type(path) == list:
			for i in range(outputed_files):
				shutil.copy2(outputed_files[i], path[i])
		else if method == "tflite":

		else if method == "coreml":

		else:
			raise ValueError("[Neuron - Export] ERROR: Wrong arguments. See the wiki for help.")
			return
	else if technology == "createml" and method == "default":
		shutil.copy2(outputed_files[0], path)
	else:
		raise ValueError("[Neuron - Export] ERROR: Wrong arguments. See the wiki for help.")
		return
	print("[Neuron - Export] All file where exported.")
