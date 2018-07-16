"""
Copyright (C) EvoCount UG - All Rights Reserved
Unauthorized copying of this file, via any medium is strictly prohibited
Proprietary and confidential

Suthep Pomjaksilp <sp@laz0r.de> 2018
"""

import logging
import asyncio
import json

from nexedge import *

if __name__ == '__main__':
    # logging
    logging.basicConfig(level=logging.DEBUG)

    # async loop
    loop = asyncio.get_event_loop()

    serial_conf = {
        "url": '/dev/ttyUSB1',
        "baudrate": 9600,
        #"baudrate": 57600,
    }
    # r = Radio(loop=loop, serial_kwargs=serial_conf, retry_sending=False)
    # loop.create_task(read_queue(r.data_queue))
    # loop.create_task(read_channel(r.channel))
    # loop.create_task(r.receiver())
    # loop.create_task(send_random(r))
    # loop.create_task(trigger_channel_status(r))

    # add listener for "about-me"
    c = RadioCommunicator(loop=loop,
                          serial_kwargs=serial_conf,
                          listeners=["about-me", "about-you"])

    # start the handler
    loop.create_task(c.data_handler())
    # dt_nom = 20
    # for s in range(1, 5):
    #     loop.create_task(send_via_com(c, s*dt_nom))

    loop.run_forever()
    loop.close()