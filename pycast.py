# Version 1.0
# Python Radio in Development

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import pyglet
import click
import soundcloud
import os
import json

@click.group(invoke_without_command = True)
@click.pass_context
def cli(ctx):
    return

@cli.command()
def list():
    podcasts = ['vergecast']
    for index, podcast in enumerate(podcasts):
        print("{} : {}".format(index + 1,podcast))

@cli.command()
@click.option('--podcast', prompt='What podcast do you want to list to?')
def play(podcast):
    # Sound Cloud Integration
    """
    client = soundcloud.Client(client_id='CLIENT-ID-GOES-HERE')
    tracks = client.get('/tracks', limit=10)
    for track in tracks:
        print track.title
    app = client.get('/apps/124')
    print app.permalink_url
    """
    # find all sounds of buskers licensed under 'creative commons share alike'
    client = soundcloud.Client(client_id='CLIENT-ID-GOES-HERE')
    tracks = client.get('/tracks', q=podcast, license='cc-by-sa')


"""
url = "URL-GOES-HERE"
file = urlopen(url)
fileManager = open('test.wav','wb')
fileManager.write(file.read())
fileManager.close()

os.remove('test.wav')
"""


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
