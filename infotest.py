# -*- coding: utf-8 -*-
#!/usr/bin/env python2
from pyepsolartracer.client import EPsolarTracerClient
from pyepsolartracer.registers import registers,coils
from test.testdata import ModbusMockClient as ModbusClient

import time 

# configure the client logging
import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

client = EPsolarTracerClient()
client.connect()

sources = [
    #registername und abkürzung
    {"name": "Charging equipment input voltage", "shortname": "input_voltage"},
    {"name": "Charging equipment input current", "shortname": "input_current"},
    {"name": "Temperature inside equipment", "shortname": "modul_temp"}

]

while True:
    for reg in sources: 
        value = client.read_input(reg["name"])
        print((reg["shortname"], value.value, value.register.unit()[1]))
    #abfragefrequenz
    time.sleep(2)

client.close()
