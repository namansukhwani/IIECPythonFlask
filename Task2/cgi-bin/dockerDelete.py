#!/usr/bin/python3

print("content-type:text/html")
print()

import cgi
import subprocess as sp

data=cgi.FieldStorage()

def deletePod():
    name=data.getvalue('osNameDelete')
    cmd=sp.getstatusoutput('sudo docker rm {0}'.format(name))
    if cmd[0]==0:
        print('Sucessfully Deleted Pod with name  ')
        print(cmd[1])
    else:
        print("Unable To Execute The Command")
        print('<html><body><pre>'+'Error  ::-  '+cmd[0]+'</pre></body></html>')


deletePod()