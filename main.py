#!/usr/bin/python
# -*- coding: UTF-8 -*-
import importlib
import os
import models.rate
import database
import datetime
conf =models.rate.Service()

rate = conf.getConf(3,20)
print(rate);
rate.type=3
rate.update()