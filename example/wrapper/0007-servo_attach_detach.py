#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2018, UFACTORY, Inc.
# All rights reserved.
#
# Author: Vinman <vinman.wen@ufactory.cc> <vinman.cub@gmail.com>

import os
import sys
import time
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from xarm.wrapper import XArmAPI

xarm = XArmAPI('192.168.1.113')
xarm.motion_enable(enable=True)
xarm.set_mode(0)
xarm.set_state(state=0)

# detach a servo
xarm.set_servo_detach(servo_id=1)
time.sleep(5)
# attach a servo
xarm.set_servo_attach(servo_id=1)
time.sleep(5)
xarm.disconnect()
