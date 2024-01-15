#!/usr/bin/python3
"""Kilovolts - An open, fast and simple python PCB emulator
Copyright (C) Alexeev Bronislav, 2024"""
from modules.linear_components import Resistor
from modules.transistors import Transistor
from modules.pcb import PCB

# Создание PCB
pcb = PCB('MyPCB')

# Создание компонентов и добавление их на плату
r1 = Resistor('R1', 100.0, 9.0, 0.1)
pcb.add_component(r1)
t1 = Transistor('T1', 'NPN', 0.7, 0.1, 1.2, 2.0)
pcb.add_component(t1)
# Соединияем компоненты проводом
pcb.connect_components(r1, t1)

# Выводим имена компонентов и информацию о PCB
print(r1.get_name())
print(t1.get_name())
print(pcb.get_info())
