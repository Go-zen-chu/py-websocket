#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import logging
import time
import threading
import signal
from websocket_server import WebsocketServer

def new_client(client, server):
    server.send_message_to_all("New client joined, id:{}".format(client['id']))

def send_message_every(server):
    cnt = 0
    while cnt < 3:
        if server != None:
            server.send_message_to_all("gu")
            time.sleep(1)
            server.send_message_to_all("none")
            time.sleep(10)
            server.send_message_to_all("choki")
            time.sleep(1)
            server.send_message_to_all("none")
            time.sleep(10)
            server.send_message_to_all("pa")
            time.sleep(1)
            server.send_message_to_all("none")
            time.sleep(10)
        else:
            print("server is none")
            time.sleep(10)
        cnt += 1

def main():
    server = WebsocketServer(9090, host='127.0.0.1', loglevel=logging.INFO)
    server.set_fn_new_client(new_client)
    send_message_thread = threading.Thread(target=send_message_every, args=(server,))
    send_message_thread.start()
    try:
        server.run_forever()
    except:
        print("Exception!")

if __name__ == "__main__":
    main()
