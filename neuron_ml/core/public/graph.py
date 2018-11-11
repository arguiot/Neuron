"""
-----------------------------------------------------
Copyright © Arthur Guiot 2018. All rights reserved
-----------------------------------------------------

/core/public/graph.py defines the 'graph' method that
will be used to load the graph from a file for the
'classify' method.

"""

def graph(model):
	if model[1] == "tensorflow":
		model_file = model[2][0]
		graph = tf.Graph()
		graph_def = tf.GraphDef()

		with open(model_file, "rb") as f:
			graph_def.ParseFromString(f.read())
		with graph.as_default():
			tf.import_graph_def(graph_def)
		print("[Neuron - Graph] Graph was correctly loaded.")
		return graph
	else:
		raise ValueError("[Neuron - Graph] ERROR: Only TensorFlow trained model are accepted.")
		return
