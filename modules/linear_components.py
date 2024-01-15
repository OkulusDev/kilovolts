#!/usr/bin/python3
"""Module 'Linear Components'
Линейный компонент (linear component) - это электронный компонент, который обладает
линейной зависимостью между входным и выходным сигналами. Это означает, что выходной
сигнал линейно пропорционален входному сигналу. Линейные компоненты широко применяются
в электронике для управления сигналами, фильтрации, усиления и других задач.
Copyright (C) Alexeev Bronislav, 2024"""
from modules.base import Component


class LinearComponent(Component):
    """Линейный компонент"""
    def __init__(self, name: str, component_type: str, voltage: float, 
                 amperage: float, wired_objects: list=[]):
        super().__init__(name, component_type, voltage, amperage, wired_objects)

    def get_name(self) -> str:
        """Получение полного имени компонента

        Вывод:
            str"""
        return f'Linear Component {self.component} {self.name} (amperage: {self.amperage}; voltage: {self.voltage})'

    def __repr__(self):
        return f'Linear Component {self.component} {self.name}'


class Resistor(LinearComponent):
    """Резистор это линейный компонент, который представляет собой электрический
    элемент с определенным сопротивлением. Он ограничивает поток электрического
    тока в цепи. Резисторы обычно используются для контроля силы тока, создания
    делителей напряжения, фильтрации сигналов и других приложений."""
    def __init__(self, name: str, resistance: float=0.0, voltage: float=0.0,
                 amperage: float=0.0, wired_objects: list=[]):
        """Инициализация резистора

        Ввод:
            name: str - имя резистора
            wired_with - с кем соединен проводом (по умолчанию None)
            resistance: float - сопротивление (по умолчанию 0.0)"""
        super().__init__(name, 'Resistor', voltage, amperage, wired_objects)
        self.resistance = resistance            # Сопротивление

    def change_resistance(self, new_res: float):
        """Изменение сопротивления резистора

        Ввод:
            new_res: float - новое значение сопротивления"""
        self.resistance = new_res

