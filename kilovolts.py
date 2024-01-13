#!/usr/bin/python3
"""Kilovolts - An open, fast and simple python PCB emulator
Copyright (C) Alexeev Bronislav, 2024"""
from modules.components import Resistor

r1 = Resistor('R1', None, 100.0)
print(r1.resistance)
