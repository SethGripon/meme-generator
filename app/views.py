from flask import Blueprint, render_template, request, redirect, url_for, session
from .memes import getIMageMemes

views = Blueprint('views', __name__)

meme = {
  'top_text': '',
  'bottom_text': '',
  'img': ''
}

@views.route('/')
@views.route('/home')
def home():
  return render_template('home.html')

@views.route('/generateMeme', methods=['GET','POST'])
def generateMeme():
  if request.method == 'POST':
    if not request.form['top_text'] or not request.form['bottom_text']:
      return 'No inputted text', 404
    else:
      meme['top_text'] = request.form['top_text']
      meme['bottom_text'] = request.form['bottom_text']

      return render_template('meme.html', meme=meme)

@views.route('/randomImage')
def randomImage():
  meme['img'] = getIMageMemes()
  return meme['img']


  
