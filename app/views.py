from flask import Blueprint, render_template
from .memes import getIMageMemes

views = Blueprint('views', __name__)

@views.route('/')
def home():
  image = getIMageMemes()
  return render_template('home.html', image=image)

  
