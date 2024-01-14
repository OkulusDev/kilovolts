#!/usr/bin/python3
"""Module 'Linear Components'
Copyright (C) Alexeev Bronislav, 2024"""


class LinearComponent:
    """Линейный компонент"""
    def __init__(self, name: str, component_type: str, wired_objects: list=[]):
        """Инициализация
        
        Ввод:
            name: str - Имя компонента
            wired_with - С каким объектом проведен провод (None по умолчанию)"""
        self.wired_objects: list = wired_objects
        self.name = name
        self.component = component_type

    def get_name(self) -> str:
        """Получение полного имени компонента

        Вывод:
            str"""
        return f'Linear Component {self.component} {self.name} (connected by a wire to the {self.wired_objects})'
    
    def change_wire(self, new_object) -> None:
        """Меняем провод (объект)

        Ввод:
            new_object - Новый объект"""
        self.wired_objects: list = [new_object]

    def remove_wire(self, index):
        self.wired_objects.pop(index)

    def new_wire(self, new_object) -> None:
        self.wired_objects.append(new_object)

    def __repr__(self):
        return f'Linear Component {self.component} {self.name}'


class Resistor(LinearComponent):
    """Резистор (линейный компонент)"""
    def __init__(self, name: str, resistance: float=0.0, wired_objects: list=[]):
        """Инициализация резистора

        Ввод:
            name: str - имя резистора
            wired_with - с кем соединен проводом (по умолчанию None)
            resistance: float - сопротивление (по умолчанию 0.0)"""
        super().__init__(name, 'Resistor', wired_objects)      # Инициализация родителя
        self.resistance = resistance            # Сопротивление

    def change_resistance(self, new_res: float):
        """Изменение сопротивления резистора

        Ввод:
            new_res: float - новое значение сопротивления"""
        self.resistance = new_res


class Transistor(LinearComponent):
    """Транзистор (линейный компонент)"""
    def __init__(self, name: str, transistor_type: str="NPN", wired_objects: list=[]):
        """Инициализация транзистора

        Ввод:
            name: str - имя транзистора
            wired_with - с кем соединен проводом (по умолчанию None)
            transistor_type: str - тип транистора (по умолчанию NPN)"""
        super().__init__(name, f'Transistor {transistor_type}', wired_objects)          # Инициализация родителя
        self.transistor_type = transistor_type      # тип транзистора

    def change_type(self, new_type: str):
        """Изменение типа транзистора

        Ввод:
            new_type: str - новый тип"""
        self.transistor_type = transistor_type

