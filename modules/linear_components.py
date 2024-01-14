#!/usr/bin/python3
"""Module 'Linear Components'
Линейный компонент (linear component) - это электронный компонент, который обладает
линейной зависимостью между входным и выходным сигналами. Это означает, что выходной
сигнал линейно пропорционален входному сигналу. Линейные компоненты широко применяются
в электронике для управления сигналами, фильтрации, усиления и других задач.
Copyright (C) Alexeev Bronislav, 2024"""


class LinearComponent:
    """Линейный компонент"""
    def __init__(self, name: str, component_type: str, voltage: float, 
                 amperage: float, wired_objects: list=[]):
        """Инициализация
        
        Ввод:
            name: str - Имя компонента
            wired_with - С каким объектом проведен провод (None по умолчанию)"""
        self.wired_objects: list = wired_objects    # колво связных объектов
        self.name = name                            # имя компонента
        self.component = component_type             # тип компонента
        self.amperage = amperage                    # ток (амперы)
        self.voltage = voltage                      # напряжение (вольты)

    def get_name(self) -> str:
        """Получение полного имени компонента

        Вывод:
            str"""
        return f'Linear Component {self.component} {self.name} (amperage: {self.amperage}; voltage: {self.voltage})'
    
    def change_wire(self, new_object) -> None:
        """Меняем провод (объект)

        Ввод:
            new_object - Новый объект"""
        self.wired_objects: list = [new_object]

    def remove_wire(self, objects):
        self.wired_objects.remove(objects)

    def new_wire(self, new_object) -> None:
        self.wired_objects.append(new_object)

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


class Transistor(LinearComponent):
    """Транзистор (линейный компонент)
    Транзистор - это полупроводниковый компонент, который управляет потоком
    электрического тока в цепи. Он может работать в различных режимах, таких
    как усиление сигнала, коммутация и стабилизация напряжения. Транзисторы
    широко используются в электронных устройствах, таких как усилители,
    микропроцессоры, телевизоры и другие."""
    def __init__(self, name: str, transistor_type: str="NPN", voltage:float=0.0,
                 amperage:float=0.0, wired_objects: list=[]):
        """Инициализация транзистора

        Ввод:
            name: str - имя транзистора
            wired_with - с кем соединен проводом (по умолчанию None)
            transistor_type: str - тип транистора (по умолчанию NPN)"""
        super().__init__(name, f'Transistor {transistor_type}', voltage,
                         amperage, wired_objects)
        self.transistor_type = transistor_type      # тип транзистора

    def change_type(self, new_type: str):
        """Изменение типа транзистора

        Ввод:
            new_type: str - новый тип"""
        self.transistor_type = transistor_type

