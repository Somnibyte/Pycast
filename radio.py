# Version 1.0
# Python Radio in Development

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import pyglet
import os

url = "URL-GOES-HERE"
file = urlopen(url)
fileManager = open('test.wav','wb')
fileManager.write(file.read())
fileManager.close()

os.remove('test.wav')
"""
music = pyglet.resource.media('test.wav')
music.play()
pyglet.app.run()
"""

"""
output = open('test.mp3','wb')
output.write(mp3file.read())
output.close()
"""
