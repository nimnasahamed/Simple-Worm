from sys import argv
import subprocess
import os

script = argv
name = str(script[0])
print (name)

cmd = 'start payload.txt'
os.system(cmd)
os.mkdir('clone')
os.system(r"copy payload.txt clone")
os.system(r"copy" + name + "clone")
