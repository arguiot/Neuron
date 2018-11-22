# -*- coding: utf-8 -*-
"""
-----------------------------------------------------
Copyright © Arthur Guiot 2018. All rights reserved
-----------------------------------------------------

/core/public/classify.py defines the 'classify' method that
will be used to classify any images using a given model.

"""


def classify(graph, labels, image):
	import numpy as np
	import tensorflow as tf
	import time
	start = time.time()
	def read_tensor_from_image_file(file_name,
									input_height=299,
									input_width=299,
									input_mean=0,
									input_std=255):
		input_name = "file_reader"
		output_name = "normalized"
		file_reader = tf.read_file(file_name, input_name)
		if file_name.endswith(".png"):
			image_reader = tf.image.decode_png(
				file_reader, channels=3, name="png_reader")
		elif file_name.endswith(".gif"):
			image_reader = tf.squeeze(
				tf.image.decode_gif(file_reader, name="gif_reader"))
		elif file_name.endswith(".bmp"):
			image_reader = tf.image.decode_bmp(file_reader, name="bmp_reader")
		else:
			image_reader = tf.image.decode_jpeg(
				file_reader, channels=3, name="jpeg_reader")
		float_caster = tf.cast(image_reader, tf.float32)
		dims_expander = tf.expand_dims(float_caster, 0)
		resized = tf.image.resize_bilinear(
			dims_expander, [input_height, input_width])
		normalized = tf.divide(tf.subtract(resized, [input_mean]), [input_std])
		sess = tf.Session()
		result = sess.run(normalized)

		return result

	file_name = image
	input_height = 299
	input_width = 299
	input_mean = 0
	input_std = 255
	input_layer = "Placeholder"
	output_layer = "final_result"

	t = read_tensor_from_image_file(
		file_name,
		input_height=input_height,
		input_width=input_width,
		input_mean=input_mean,
		input_std=input_std)

	input_name = "import/" + input_layer
	output_name = "import/" + output_layer
	input_operation = graph.get_operation_by_name(input_name)
	output_operation = graph.get_operation_by_name(output_name)

	with tf.Session(graph=graph) as sess:
		results = sess.run(output_operation.outputs[0], {
			input_operation.outputs[0]: t
		})
	results = np.squeeze(results)

	top_k = results.argsort()[-5:][::-1]

	dictionnary = {
		"labels": labels,
		"top": "",
		"prob": 0.0,
		"results": {}
	}
	for i in top_k:
		dictionnary["results"][labels[i]] = results[i]
	max = np.amax(results)
	index = results.tolist().index(max)
	dictionnary["prob"] = results[index]
	dictionnary["top"] = labels[index]
	end = time.time()

	print("[Neuron - Classify] Classified as '" + dictionnary["top"] + "' in " + str(end - start) + "s.")
	return dictionnary
