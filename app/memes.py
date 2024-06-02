from flask import Flask, jsonify
import requests
import random

meme_url = 'https://api.imgflip.com/get_memes'

def getIMageMemes():
  number = random.randint(1, 100)
  response = requests.get(meme_url)

  if response.status_code == 200:
    data = response.json()
    memes = data['data']['memes']
    return memes[number]['url']
  else:
    return 'Nothing found', 404
