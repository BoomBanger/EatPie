import time
time.sleep(5)

import datetime
import os
import git
import pyglet
from pyglet.window import Platform

dir = os.path.dirname(os.path.realpath(__file__))

repo = git.cmd.Git(dir)

t = -1
lastpull = 0

with open(os.path.join(dir, "dinnerTime.txt"), "r") as f:
    timestr = f.read()
    #####################################################04/02/22 04:03
    t = time.mktime(datetime.datetime.strptime(timestr, "%m/%d/%y %H:%M:%S").timetuple())
    #t += 5*3600 #only for replit, thinks we are in london

def pull():
    global time, dir, repo
    try:
        repo.pull()
        with open(os.path.join(dir, "dinnerTime.txt"), "r") as f:
            timestr = f.read()
            #####################################################04/02/22 04:03
            t = time.mktime(datetime.datetime.strptime(timestr, "%d/%m/%y %H:%M:%S").timetuple())
            #t += 5*3600 #only for replit, thinks we are in london
    except:
       pass
  
while time.time() < t:
    print("waiting")
    if time.time() - lastpull > 4*60*60:
        pull()
        lastpull = time.time()

if time.time() < t + 10*60*60:
    monitor = Platform().get_default_display().get_default_screen()

    sprite = pyglet.sprite.Sprite(pyglet.resource.animation(os.path.join(dir, "text.gif")))
    H_ratio = max(sprite.height, monitor.height) / min(sprite.height, monitor.height)
    W_ratio = max(sprite.width, monitor.width) / min(sprite.width, monitor.width)

    sprite.scale = min(H_ratio, W_ratio)

    window = pyglet.window.Window(width=monitor.width, height=monitor.height, fullscreen=True)

    pyglet.gl.glClearColor(1, 1, 1, 1)

    @window.event
    def on_draw():
        window.clear()
        sprite.draw()

    pyglet.app.run()
