# What is Neuron exactly?

Neuron is a tiny library that aims to simplify image classification (If you don't know what Image classification is, it's the process to tell from an image what object / thing / feature is on it).

Using Neuron, you'll be able to build production grade model under 5 lines of code. Yes, you read it correctly: 5 lines. Where as in common Machine Learning libraries like TensorFlow, PyTorch or Keras, you would do it in hundreds of lines.

> Of course, these libraries are much more complex and versatile than Neuron. Neuron isn't replacing these libraries if you need to build your own graph, but if you're doing so, you probably already know this.

Neuron's model can be used and converted for **every** devices you plan to support for your next greatest project. Neuron will even expose the raw TensorFlow graph is you want to tune it a bit (only for advanced users).

## Demo

Simple trainer:
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


Now, try it yourself by installing it: `pip install neuron-ml`
