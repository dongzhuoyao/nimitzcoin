# Author: Tao Hu <taohu620@gmail.com>

import os
from setuptools import setup,find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "nimitzcoin",
    version = "0.0.2",
    author = "Tao Hu",
    author_email = "taohu620@gmail.com",
    description = ("A digital currency quantitative trading tool."),
    license = "BSD",
    keywords = "python",
    url = "http://packages.python.org/an_example_pypi_project",
    packages=find_packages(),
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)