"""
-----------------------------------------------------
Copyright © Arthur Guiot 2018. All rights reserved
-----------------------------------------------------

/core/data/createml.py will transfer and convert
images to the desired destination (TEMP directory)
for CreateML usage.

"""

def organise_dataset(data, path):
	import os
	import sys
	import pandas as pd
	import shutil
	os.makedirs(path, exist_ok=True)
	folders = os.listdir(data)
	print("[Neuron - Load] Organising dataset by moving to dataset folder & converting to jpeg")
	for folder in folders:
		if folder != ".git" and os.path.isdir(data + '/' + folder):
			images = os.listdir(train + '/' + folder)
			count = len(images)
			n_test = int(round(count * 0.9)) # Will take 10% for tests. Max 10 images
			if n_test > 10:
				n_test = 10
			r_test = range(n_test)

			train = path + '/Train/'
			test = path + '/Test/'
			os.makedirs(train)
			os.makedirs(test)
			for i in range(count):
				p = folder + '/' +images[i]
				s = data + '/' + p
				if i in r_test: # Move to test
					d = test + p
					shutil.copy2(s, d)
				else:
					d = train + p
					shutil.copy2(s, d)
	print("[Neuron - Load] Dataset folders successfully created & copied all images in corresponding folders")
