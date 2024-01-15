#!/usr/bin/python3
"""Module 'PCB'
Copyright (C) Alexeev Bronislav, 2024"""


class PCB:
    """Printed Circuit Board (Printed Circuit Board) - это печатная плата, 
    которая представляет собой основу для монтажа и соединения электронных 
    компонентов в электрической цепи. PCB обеспечивает механическую поддержку 
    компонентов и электрическое соединение между ними с помощью проводников и 
    металлических трасс"""
    def __init__(self, PCB_name: str, components: list=[],
                 connections: list=[]):
        """Инициализация

        Ввод:
            PCB_name: str - имя платы
            components: list - список компонентов по умолчанию ([])
            connections: list - список соединенных компонентов по умолчанию"""
        self.PCB_name = PCB_name
        self.components: list = components
        self.connections: list = connections
        self.power_consumption = 0.0

    def add_component(self, component) -> None:
        """Добавление компонента в список

        Аргументы:
            component - объект класса компонента (компонент)"""
        self.components.append(component)
        self.power_consumption = component.voltage * component.amperage

    def connect_components(self, first_object, second_object) -> int:
        first_object.new_wire(second_object)
        second_object.new_wire(first_object)
        self.connections.append([first_object, second_object])
        index = self.connections.index([first_object, second_object])
        
        return index

    def get_connection_by_index(self, index: int) -> list:
        """Получение соединенных компонентов по индексу

        Ввод:
            index: int - индекс в списке соединенний

        Вывод:
            list"""
        return self.connections[index]

    def get_component_by_index(self, index: int) -> list:
        """Получение компонент по индексу

        Ввод:
            index: int - индекс в списке компонентов

        Вывод:
            list"""
        return self.components[index]

    def remove_component(self, component) -> None:
        """Удаление компонента (со всеми соединениями)

        Ввод:
            component - объект класса компонента (компонент)"""
        self.components.remove(component)
        
        for connection in self.connections:
            if connection[0] == component or connection[1] == component:
                self.connections.remove([connection[0], connection[1]])
    
    def get_info(self) -> str:
        """Получение информации о PCB

        Вывод:
            str"""
        result = f'\nPCB "{self.PCB_name}"\n'

        result += f'Компоненты ({len(self.components)}):\n'
        for component in self.components:
            result += f'{component.get_name()}'
            if component.component == 'Transistor':
                is_on = ' (on)' if component.is_on() else ' (off)'
                result += is_on
            result += '\n'

        result += f'Связи ({len(self.connections)}):\n'
        for connection in self.connections:
            result += f'{connection[0]} -> {connection[1]}\n'

        result += f'Потребляемая мощность: {self.power_consumption} Вт'

        return result

