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
                 resistance: float, amperage: float, wired_objects: list=[]):
        super().__init__(name, component_type, voltage, resistance, amperage, 
                         wired_objects)

    def get_name(self) -> str:
        """Получение полного имени компонента

        Вывод:
            str"""
        return f'Linear Component {self.component} {self.name} (amperage: {self.amperage}; voltage: {self.voltage}; resistance: {self.resistance})'

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
        super().__init__(name, 'Resistor', voltage, resistance, amperage, 
                         wired_objects)

    def change_resistance(self, new_res: float):
        """Изменение сопротивления резистора

        Ввод:
            new_res: float - новое значение сопротивления"""
        self.resistance = new_res


class Capacitor(LinearComponent):
    """Конденсатор - это электронный компонент, способный накапливать и 
    хранить электрический заряд. Он состоит из двух проводящих пластин,
    разделенных изолятором (диэлектриком). Конденсаторы имеют емкость,
    измеряемую в фарадах (Ф). Большая емкость означает большую способность
    конденсатора накапливать заряд."""
    def __init__(self, name: str, capacitance=10e-6, voltage: float=0.0,
                 resistance: float=0.0, amperage: float=0.0, 
                 wired_objects: list=[]):
        super().__init__(name, 'Capacitor', voltage, resistance, amperage, 
                         wired_objects)
        self.capacitance = capacitance

    def change_capicitance(self, new_cap: float):
        self.capacitance = new_cap


class Inductor(LinearComponent):
    """Индуктор - это электронный компонент, использующийся для создания и
    хранения магнитного поля. Он состоит из проводящей катушки, обычно
    изготовленной из провода, намотанного вокруг магнитопровода. Индукторы
    обладают индуктивностью, измеряемой в генри (Гн). Большая индуктивность
    означает большую способность индуктора создавать магнитное поле."""
    def __init__(self, name: str, inductance=1e-3, voltage: float=0.0,
                 resistance: float=0.0, amperage: float=0.0, 
                 wired_objects: list=[]):
        super().__init__(name, 'Inductor', voltage, resistance, amperage, 
                         wired_objects)
        self.inductance = inductance

    def change_inductance(self, new_ind):
        self.inductance = new_ind


class Potentiometer(LinearComponent):
    """Потенциометр - это переменный резистор с тремя выводами, который
    позволяет изменять сопротивление в зависимости от положения подвижного
    контакта. Потенциометры широко используются для регулировки напряжения или
    уровня сигнала в электрических цепях."""
    def __init__(self, name: str, resistance: float, voltage: float=0.0,
                 amperage: float=0.0, wired_objects: list=[]):
        super().__init__(name, 'Potentiometer', voltage, resistance, amperage, 
                         wired_objects)

    def change_resistance(self, new_res: float):
        self.resistance = new_res


class PolarizedCapacitor(LinearComponent):
    """Поляризованный конденсатор - это тип конденсатора, который имеет
    полярность, то есть он должен быть подключен в цепь с учетом правильной
    полярности. Он обычно используется для фильтрации постоянного напряжения или
    для создания временных задержек в электрических цепях. Поляризованные
    конденсаторы имеют положительный и отрицательный выводы, и их емкость
    измеряется в микрофарадах (мкФ) или пикофарадах (пФ)."""
    def __init__(self, name: str, polarity: bool, capacitance: float=100e-6,
                 voltage: float=0.0, resistance: float=0.0, amperage=0.0, 
                 wired_objects: list=[]):
        super().__init__(name, 'Polarized Capacitor', voltage, resistance, amperage,
                        wired_objects)
        self.capacitance = capacitance
        self.polarity = polarity

    def change_capicitance(self, new_cap: float):
        self.capacitance = new_cap

    def change_polarity(self, new_pol: bool):
        self.polarity = new_pol


class Photoresistor(LinearComponent):
    """Фоторезистор, также известный как фотоэлектрический резистор или LDR
    (Light-Dependent Resistor), - это резистор, чье сопротивление изменяется в
    зависимости от интенсивности света, падающего на него. Он используется для
    обнаружения или измерения освещенности в различных приложениях, таких как
    автоматические световые выключатели или фотореле."""
    def __init__(self, name: str, resistance: float, voltage: float=0.0,
                 amperage: float=0.0, wired_objects: list=[]):
        super().__init__(name, 'Photoresistor', voltage, resistance, amperage, wired_objects)

    def change_resistance(self, new_res: float):
        self.resistance = new_res

