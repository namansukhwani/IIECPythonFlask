#!/usr/bin/python3

print("content-type:text/html")
print()

import cgi
import subprocess as sp

data=cgi.FieldStorage()


def createDocker():
    name=data.getvalue('osName')
    os=data.getvalue('os')
    cmd=sp.getstatusoutput('sudo docker run -d -it --name {0} {1}'.format(name,os))
    if cmd[0]==0:
        print('Sucessfully launched Your Pod with id ')
        print(cmd[1])
    else:
        print("Unable To Execute The Command")
        print('<html><body><pre>'+'Error  ::-  '+cmd[0]+'</pre></body></html>')

createDocker()