# -*- coding: utf-8 -*-
"""
-----------------------------------------------------
Copyright © Arthur Guiot 2018. All rights reserved
-----------------------------------------------------

/core/public/image.py defines the 'image' method that
will be used to encode an image in order to classify
it.

"""

def image(path):
	import tensorflow as tf
	input_name = "file_reader"
	file_reader = tf.read_file(file_name, input_name)
	if file_name.endswith(".png"):
		return tf.image.decode_png(
			file_reader, channels=3, name="png_reader")
	elif file_name.endswith(".gif"):
		return tf.squeeze(
			tf.image.decode_gif(file_reader, name="gif_reader"))
	elif file_name.endswith(".bmp"):
		return tf.image.decode_bmp(file_reader, name="bmp_reader")
	else:
		return tf.image.decode_jpeg(
			file_reader, channels=3, name="jpeg_reader")
