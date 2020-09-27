#!/usr/bin/python3

print("content-type:text/html")
print()

import cgi
import subprocess as sp

def viewRunningPods():
    cmd=sp.getstatusoutput('sudo docker ps')
    if cmd[0]==0:
        print('<html><body><pre>'+cmd[1]+'</pre></body></html>')
    else:
        print("Unable To Execute The Command")
        print('<html><body><pre>'+'Error  ::-  '+cmd[0]+'</pre></body></html>')

viewRunningPods()

