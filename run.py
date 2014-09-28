#!venv/bin/python

from app import app
from pymarkovchain import MarkovChain

MarkovChain('./markov').generateDatabase("Hi my name is bob! Hi his name is bill!")
app.run(debug=True)
