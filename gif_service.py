import os, TenGiphPy
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('TENOR_KEY')

_T = TenGiphPy.Tenor(TOKEN)

def get_gif(tag):
    url = _T.random(tag)
    return url

def natural_twenty():
    return 'https://tenor.com/view/celebration-dance-goal-gif-13884471'
