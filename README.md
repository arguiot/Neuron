<div align="center">
	<img width="500" height="500" src="https://raw.githubusercontent.com/arguiot/Neuron/master/assets/Neuron.png"/>
	<h1>Neuron</h1>
	A tiny and very high level transfer learning library for image classification 📚
</div>

[![GitHub release](https://img.shields.io/github/release/arguiot/Neuron.svg)](https://github.com/arguiot/Neuron/releases)
[![Build Status](https://travis-ci.org/arguiot/Neuron.svg?branch=master)](https://travis-ci.org/arguiot/Neuron)
[![Github All Releases](https://img.shields.io/github/downloads/arguiot/Neuron/total.svg)](https://github.com/arguiot/Neuron/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/neuron-ml.svg)](https://pypi.org/project/neuron-ml/)
[![License](https://img.shields.io/github/license/arguiot/Neuron.svg)](LICENSE)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Farguiot%2FNeuron.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Farguiot%2FNeuron?ref=badge_shield)

## What is Neuron exactly?

Neuron is a tiny library that aims to simplify image classification (If you don't know what Image classification is, it's the process to tell from an image what object / thing / feature is on it).

Using Neuron, you'll be able to build production grade model under 5 lines of code. Yes, you read it correctly: 5 lines. Where as in common Machine Learning libraries like TensorFlow, PyTorch or Keras, you would do it in hundreds of lines.

> Of course, these libraries are much more complex and versatile than Neuron. Neuron isn't replacing these libraries if you need to build your own graph, but if you're doing so, you probably already know this.

## Install
Copy - paste that in a Terminal
```
pip install neuron-ml
```
## Demo
Here is an example of what Neuron can do:
```py
import neuron_ml as n

# TensorFlow

data = n.load("./dataset/") # formats the data
model = n.train(data) # train the data
n.export(model, [
	"./Model.pb",
	"./Labels.txt"
]) # Exports everything
n.clean(model) # Clean temporary files
```

And it can also load files and classify them (before using it for production, make sure you have good hardware, as the model can take up to 5 seconds to load and run).

```py
import neuron_ml as n

model = n.model([
	"./Model.pb",
	"./Labels.txt"
]) # Load the model
graph = n.graph(model) # Generate the graph
labels = n.labels(model) # Get the labels
n.classify(graph, labels, "./dataset/Celery/celery-1.jpg") # Classify. Will return a result object
```

> See the [wiki](https://github.com/arguiot/Neuron/wiki) for more informations.

# Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/arguiot/Neuron/tags).

# Authors

- **Arthur Guiot** - _Initial work_ - [@arguiot](https://github.com/arguiot)

Also look at the list of [contributors](https://github.com/arguiot/Neuron/contributors) who participated in this project. If you don't code but you have great ideas, don't hesitate to write your idea in the issue part. If your idea is accepted, I will add you to this list 😊.

# License

This project is licensed under the MIT License - see the <LICENSE> file for details

__Copyright © 2018 Arthur Guiot All Rights Reserved.__


[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Farguiot%2FNeuron.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Farguiot%2FNeuron?ref=badge_large)