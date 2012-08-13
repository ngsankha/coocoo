# Coocoo sends notifications
# Copyright 2012, Sankha Narayan Guria <sankha93@gmail.com>
# This source code is released under MIT License 
#
# notifier.py : Run this script to send notifications

from socket import *
import sys, json

port = 50027

if len(sys.argv) < 4:
    print "Usage: notifier.py [address] [title] [text]"
else:
    packet = json.dumps({'title': sys.argv[2], 'text': sys.argv[3]})
    socket = socket(AF_INET, SOCK_STREAM)
    socket.connect((sys.argv[1], port))
    socket.send(packet)
    print "Notification to " + sys.argv[1] + " sent successfully!"
    socket.close()
