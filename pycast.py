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
@click.option('--podcast', prompt='What podcast do you want to listen to? [Enter the users SoundCloud username]')
def play(podcast):
    # Sound Cloud Integration
        client = soundcloud.Client(client_id='CLIENT-ID-GES-HERE')
        podcastName = str(podcast)

        try:
            tracks = client.get('/users/{}/tracks'.format(podcastName),limit=1)
            for track in tracks:
                stream_url = client.get(track.stream_url, allow_redirects=False)

            print stream_url.location
            url = stream_url.location
            file = urlopen(url)
            fileManager = open('test.mp3','wb')
            fileManager.write(file.read())
            fileManager.close()
            music = pyglet.resource.media('test.mp3')
            music.play()
            pyglet.app.run()

        except Exception, e:
            print 'Error: %s, Status Code: %d' % (e.message, e.response.status_code)




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
