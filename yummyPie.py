import time
time.sleep(120)

import datetime
import git
import os

dir = os.path.dirname(os.path.realpath(__file__))

repo = git.cmd.Git(dir)

t = -1
lastpull = 0

def pull():
  global time
  try:
    repo.pull()
    with f as file.open(os.path.append(dir, "dinnerTime.txt"), "r"):
      timestr = f.read()
      #####################################################30/02/22 04:03
      t = time.mktime(datetime.datetime.strptime(timestr, "%d/%m/%y %H:%M").timetuple())
   except:
    pass
  
while time.time() < t or t <= 0:
  if time.time() - lastpull > 4*60*60:
    pull()
    lastpull = time.time()
  
