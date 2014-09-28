from flask import Flask, render_template
from pymarkovchain import MarkovChain

app = Flask(__name__)
mc1 = MarkovChain('/var/www/personal/markov/posts')
mc2 = MarkovChain('/var/www/personal/markov/comments')

from app import views
