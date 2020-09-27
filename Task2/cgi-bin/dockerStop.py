#!/usr/bin/python3

print("content-type:text/html")
print()

import cgi
import subprocess as sp

data=cgi.FieldStorage()

def stopPod():
    name=data.getvalue('osNameStop')
    cmd=sp.getstatusoutput('sudo docker stop {0}'.format(name))
    if cmd[0]==0:
        print('Sucessfully Stoped Pod ')
        print(cmd[1])
    else:
        print("Unable To Execute The Command")
        print('<html><body><pre>'+'Error  ::-  '+cmd[0]+'</pre></body></html>')

stopPod()