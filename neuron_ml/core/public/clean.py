# -*- coding: utf-8 -*-
"""
-----------------------------------------------------
Copyright © Arthur Guiot 2018. All rights reserved
-----------------------------------------------------

/core/public/clean.py defines the 'clean' method that
will be used to clean the temporary file that were
created.

"""

def clean(model):
	import shutil
	global_path = model[0]
	shutil.rmtree(global_path)
