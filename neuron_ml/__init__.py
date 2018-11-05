"""
-----------------------------------------------------
Copyright © Arthur Guiot 2018. All rights reserved
-----------------------------------------------------

__init__.py is the core of the module. It imports all
of the required components, so the module can be
imported directly, without needing to do multiple
import statements.

"""
import core
import tools

load = core.public.load.load
train = core.public.train.train
