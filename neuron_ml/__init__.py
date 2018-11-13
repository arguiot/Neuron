"""
-----------------------------------------------------
Copyright © Arthur Guiot 2018. All rights reserved
-----------------------------------------------------

__init__.py is the core of the module. It imports all
of the required components, so the module can be
imported directly, without needing to do multiple
import statements.

"""
import neuron_ml.core

load = core.public.load.load
train = core.public.train.train
export = core.public.export.export
clean = core.public.clean.clean
classify = core.public.classify.classify
graph = core.public.graph.graph
labels = core.public.labels.labels
model = core.public.model.model
