from flask import Flask, render_template
from pymarkovchain import MarkovChain

app = Flask(__name__)
mc1 = MarkovChain('./posts')
mc2 = MarkovChain('./comments')

from app import views
