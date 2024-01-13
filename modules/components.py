#!/usr/bin/python3
"""Module 'Components'
Copyright (C) Alexeev Bronislav, 2024"""


class LinearComponent:
    """Линейный компонент"""
    def __init__(self, name: str, wired_with=None):
        """Инициализация
        
        Ввод:
            name: str - Имя компонента
            wired_with - С каким объектом проведен провод (None по умолчанию)"""
        self.wired_object = wired_with
        self.name = name

    def get_name(self) -> str:
        """Получение полного имени компонента

        Вывод:
            str"""
        return f'LinearComponent {self.component} {self.name}, wired {self.name}'
    
    def change_wire(self, new_object) -> None:
        """Меняем провод (объект)

        Ввод:
            new_object - Новый объект"""
        self.wired_object = new_object

    def __repr__(self):
        return f'<Linear Component {self.component_type} "{self.name}">'


class Resistor(LinearComponent):
    """Резистор (линейный компонент)"""
    def __init__(self, name: str, wired_with=None, resistance: float=0.0):
        """Инициализация резистора

        Ввод:
            name: str - имя резистора
            wired_with - с кем соединен проводом (по умолчанию None)
            resistance: float - сопротивление (по умолчанию 0.0)"""
        super().__init__(name, wired_with)      # Инициализация родителя
        self.resistance = resistance            # Сопротивление

    def change_resistance(self, new_res: float):
        """Изменение сопротивления резистора

        Ввод:
            new_res: float - новое значение сопротивления"""
        self.resistance = new_res


class Transistor(LinearComponent):
    """Транзистор (линейный компонент)"""
    def __init__(self, name: str, wired_with=None, transistor_type: str="NPN"):
        """Инициализация транзистора

        Ввод:
            name: str - имя транзистора
            wired_with - с кем соединен проводом (по умолчанию None)
            transistor_type: str - тип транистора (по умолчанию NPN)"""
        super().__init__(name, wired_with)          # Инициализация родителя
        self.transistor_type = transistor_type      # тип транзистора

    def change_type(self, new_type: str):
        """Изменение типа транзистора

        Ввод:
            new_type: str - новый тип"""
        self.transistor_type = transistor_type

