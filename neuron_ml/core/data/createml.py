# -*- coding: utf-8 -*-
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
			images = os.listdir(data + '/' + folder)
			count = len(images)
			n_test = int(round(count * 0.9)) # Will take 10% for tests. Max 10 images
			if n_test > 10:
				n_test = 10
			r_test = range(n_test)

			train = path + '/Train/' + folder
			test = path + '/Test/' + folder
			os.makedirs(train)
			os.makedirs(test)
			for i in range(count):
				p = folder + '/' +images[i]
				s = data + '/' + folder + '/' + images[i]
				if i in r_test: # Move to test
					d = path + '/Test/' + p
					shutil.copy2(s, d)
				else:
					d = path + '/Train/' + p
					shutil.copy2(s, d)
	print("[Neuron - Load] Dataset folders successfully created & copied all images in corresponding folders")
