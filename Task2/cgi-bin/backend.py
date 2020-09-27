#!/usr/bin/python3

print("content-type:text/html")
print()

import cgi
import subprocess as sp

data=cgi.FieldStorage()

#all commands
try:
    x=data.getvalue('linuxCmd') 
    if x=='None':
        exit()
    else :
        out=sp.getstatusoutput(x)
        if out[0]==0:
            print('<html><body><pre>'+out[1]+'</pre></body></html>')
        else:
            print("Unable To Execute The Command")
            print('<html><body><pre>'+'Error  ::-  '+out[1]+'</pre></body></html>')
except:
    #print("not avilable")
    pass
