#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 11:52:13 2022

@author: keyreeltian
"""

import schedule
import time


def task():
    print("Hello, I'm task!")
    return


schedule.every(15).seconds.do(task)

while True:
    schedule.run_pending()
    time.sleep(1)
