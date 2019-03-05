# -*- coding: utf-8 -*-
"""
-----------------------------------------------------
Copyright © Arthur Guiot 2018. All rights reserved
-----------------------------------------------------

test.py will train a "fake" model to check that
everything works as it should. You can use it as a
demo file.

"""
import neuron_ml as n
import os

# TensorFlow
data = n.load(os.path.abspath("./dataset/"))
model = n.train(data, 100)
n.export(model, [
	os.path.abspath("./Model.pb"),
	os.path.abspath("./Labels.txt")
])

# TFLite
n.export(model, os.path.abspath("./Model.tflite"), "tflite")

# Classify
graph = n.graph(model)
labels = n.labels(model)
image = n.image("./dataset/Celery/celery-1.jpg")
n.classify(graph, labels, image)

# CoreML
n.export(model, os.path.abspath("./Model.mlmodel"), "coreml")

# CreateML
data = n.load(os.path.abspath("./dataset/"), "createml")
model = n.train(data)
n.export(model, os.path.abspath("./CreateML.mlmodel"))

# Clean
n.clean(model)
