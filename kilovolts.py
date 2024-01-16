#!/usr/bin/python3
"""Kilovolts - An open, fast and simple python PCB emulator
Copyright (C) Alexeev Bronislav, 2024"""
from modules.linear_components import Resistor, Capacitor, Inductor, \
                                        Potentiometer, Photoresistor, \
                                        PolarizedCapacitor
from modules.transistors import Transistor
from modules.pcb import PCB

# Создание PCB
pcb = PCB('MyPCB')

# Создание компонентов и добавление их на плату
r1 = Resistor('R1', 100.0, 9.0, 0.1)
pcb.add_component(r1)
t1 = Transistor('T1', 'NPN', 0.7, 0.1, 1.2, 2.0)
pcb.add_component(t1)
c1 = Capacitor('C1', 10e-6, 0.8, 0.1)
pcb.add_component(c1)
i1 = Inductor('I1', 1e-3, 0.2, 3.4)
pcb.add_component(i1)
pm1 = Potentiometer('PM1', 0.2, 0.3, 1.3)
pcb.add_component(pm1)
p1 = Photoresistor('P1', 1.2, 3.1, 9.0)
pcb.add_component(p1)
pc1 = PolarizedCapacitor('PC1', True, 100e-6, 2.0, 3.3)
pcb.add_component(pc1)
# Соединияем компоненты проводом
pcb.connect_components(r1, t1)
pcb.connect_components(r1, c1)
pcb.connect_components(c1, t1)
pcb.connect_components(r1, i1)
pcb.connect_components(i1, t1)
pcb.connect_components(r1, pc1)
pcb.connect_components(i1, pm1)
pcb.connect_components(p1, pm1)
pcb.connect_components(pc1, p1)

# Выводим имена компонентов и информацию о PCB
print(r1.get_name())
print(t1.get_name())
print(c1.get_name())
print(i1.get_name())
print(pcb.get_info())
