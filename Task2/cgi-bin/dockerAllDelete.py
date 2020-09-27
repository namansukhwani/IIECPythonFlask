#!/usr/bin/python3

print("content-type:text/html")
print()

import subprocess as sp

def deleteAll():
    cmd=sp.getstatusoutput('sudo docker rm $(sudo docker ps -a -f status=exited -q)')
    if cmd[0]==0:
        print('Deleting.....')
        print('<html><body><pre>'+cmd[1]+'</pre></body></html>')
    else:
        print("Unable To Execute The Command")
        print('<html><body><pre>'+'Error  ::-  '+cmd[0]+'</pre></body></html>')

deleteAll()