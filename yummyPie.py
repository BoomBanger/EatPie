import time
time.sleep(5)

import datetime
import git
import os
import git
from tkinter import *

dir = os.path.dirname(os.path.realpath(__file__))

repo = git.cmd.Git(dir)

t = -1
lastpull = 0

with open(os.path.join(dir, "dinnerTime.txt"), "r") as f:
    timestr = f.read()
    #####################################################04/02/22 04:03
    t = time.mktime(datetime.datetime.strptime(timestr, "%m/%d/%y %H:%M:%S").timetuple())

print(t)

def pull():
    global time, dir, repo
    try:
        repo.pull()
        with open(os.path.join(dir, "dinnerTime.txt"), "r") as f:
            timestr = f.read()
            #####################################################04/02/22 04:03
            t = time.mktime(datetime.datetime.strptime(timestr, "%d/%m/%y %H:%M:%S").timetuple())
    except:
       pass
  
while time.time() < t:
    print("waiting")
    if time.time() - lastpull > 4*60*60:
        pull()
        lastpull = time.time()
print("done")
def updateGif(i, label):
    try:
        frame = PhotoImage(file = os.path.join(dir, "test.gif"), format = "gif -index %i" %(i))
        label.configure(image = frame)
        label.image = frame
    except:
        i = 0
        frame = PhotoImage(file = os.path.join(dir, "test.gif"), format = "gif -index %i" %(i))
        label.configure(image = frame)
        label.image = frame
    root.after(100, updateGif, i + 1, label)
    
if time.time() < t + 10*60*60:
    root = Tk()
    #root.attributes("-zoomed", True)
    label = Label(root)
    label.pack()
    root.after(0, updateGif, 0, label)
    #root.attributes("-fullscreen", True)
    root.mainloop()
