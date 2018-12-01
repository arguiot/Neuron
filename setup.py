import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="neuron_ml",
    version="1.0.0",
    author="Arthur Guiot",
    author_email="arguiot@gmail.com",
    description="A tiny image classification library.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arguiot/Neuron",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
