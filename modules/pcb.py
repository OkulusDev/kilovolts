#!/usr/bin/python3
"""Module 'PCB'
Copyright (C) Alexeev Bronislav, 2024"""


class PCB:
    """Printed Circuit Board (печатная плата)"""
    def __init__(self, PCB_name: str, components: list=[],
                 connections: list=[]):
        self.PCB_name = PCB_name
        self.components: list = components
        self.connections: list = connections

    def add_component(self, component) -> None:
        self.components.append(component)

    def connect_components(self, first_object, second_object) -> int:
        first_object.new_wire(second_object)
        second_object.new_wire(first_object)
        self.connections.append([first_object, second_object])
        index = self.connections.index([first_object, second_object])
        
        return index

    def get_connection_by_index(self, index: int) -> list:
        return self.connections[index]
    
    def remove_connection_by_index(self, index: int, wired_objects: list) -> None:
        self.connections[index][0].remove_wire(
                            self.wired_objects.index(self.connections[index][0])
        )
        self.connections[index][1].remove_wire(
                            self.wired_objects.index(self.connections[index][1])
        )

    def get_info(self) -> str:
        result = f'\nPCB {self.PCB_name}\n'

        result += 'Components:\n'
        for component in self.components:
            result += f'{component.get_name()}\n'

        result += 'Connections:\n'
        for connection in self.connections:
            result += f'{connection[0]} -> {connection[1]}\n'

        return result

