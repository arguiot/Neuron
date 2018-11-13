"""
-----------------------------------------------------
Copyright © Arthur Guiot 2018. All rights reserved
-----------------------------------------------------

/core/public/model.py defines the 'model' method that
will be used to generate a model object from pre
trained graphs

"""

def model(files, method="tensorflow"):
	import os
	return [0, method, files]
