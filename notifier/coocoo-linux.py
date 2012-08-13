# Coocoo sends notifications
# Copyright 2012, Sankha Narayan Guria <sankha93@gmail.com>
# This source code is released under MIT License 
#
# coocoo-linux.py : Notification server for Linux using libnotify

from socket import *
import pynotify, json

port = 50027
socket = socket(AF_INET, SOCK_STREAM)
data = ''

socket.bind(('', port))
socket.listen(5)
if not pynotify.init("Coocoo"):
    print "Unable to initialize libnotify."

while True:
    connection = socket.accept()
    while True:
        data += connection.recv(4096)
        if not data: break
    packet = json.load(data)
    n = pynotify.Notification(packet['title'], packet['text'])
    if not n.show():
        print packet['title'] + " : " + packet['text']
    connection.close()
