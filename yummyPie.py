import time
time.sleep(120)

import datetime
import git
import os
from tkinter import *

dir = os.path.dirname(os.path.realpath(__file__))

repo = git.cmd.Git(dir)

t = -1
lastpull = 0

def pull():
  global time
  try:
    repo.pull()
    with f as file.open(os.path.join(dir, "dinnerTime.txt"), "r"):
      timestr = f.read()
      #####################################################04/02/22 04:03
      t = time.mktime(datetime.datetime.strptime(timestr, "%d/%m/%y %H:%M").timetuple())
   except:
    pass
  
while time.time() < t or t <= 0:
  if time.time() - lastpull > 4*60*60:
    pull()
    lastpull = time.time()

def updateGif(ind, label):
  frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(100, update, ind, label)
    
if time.time() < t + 10*60*60:
  root = Tk()
  root.attributes("-zoomed", True)
  gifFrames = 10
  gif = [PhotoImage(file = os.path.join(dir, "raspberry.gif", format = "gif -index %i" %(i))) for i in range(gifFrames)]
  label = Label(root)
  label.pack()
  root.after(0, updateGif, 0, label)
  root.attributes("-fullscreen", True)
  root.mainloop()
