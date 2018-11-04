"""
-----------------------------------------------------
Copyright © Arthur Guiot 2018. All rights reserved
-----------------------------------------------------

/core/data/tensorflow.py will transfer and convert
images to the desired destination (TEMP directory).

"""

import os
import sys
import pandas as pd
from PIL import Image

def toJPG(source, destination):
	im = Image.open(source)
	rgb_im = im.convert('RGB')
	rgb_im.save(destination)


def organise_dataset(train, root_path):
	dataset_path = root_path
	train_data = train
	os.makedirs(dataset_path, exist_ok=True)
	folders = os.listdir(train_data)
	print("[Neuron - Load] Organising dataset by moving to dataset folder & converting to jpeg")
	for folder in folders:
		if folder != ".git" and os.path.isdir(train + '/' + folder):
			os.makedirs(dataset_path+'/'+folder, exist_ok=True)
			images = os.listdir(train + '/' + folder)
			for i in images:
				path = folder + '/' + i
				source = train_data + '/' + path
				destination = dataset_path + '/' + path
				# Moving files from source (train folder) to detination folder and convert to JPG
				jpg.toJPG(source, destination)


	print("[Neuron - Load] Dataset folders successfully created & copied all images in corresponding folders")
