#!/usr/bin/python3
"""Kilovolts - An open, fast and simple python PCB emulator
Copyright (C) Alexeev Bronislav, 2024"""
from modules.linear_components import Resistor, Transistor
from modules.pcb import PCB

pcb = PCB('MyPCB')

r1 = Resistor('R1', 100.0)
pcb.add_component(r1)
t1 = Transistor('T1', "NPN")
pcb.add_component(t1)

pcb.connect_components(r1, t1)
print(r1.get_name())
print(t1.get_name())
print()
print(pcb.get_connection_by_index(0))
print(pcb.get_info())

