from modules.base import Component


class Transistor(Component):
    """Транзистор (компонент)
    Транзистор - это полупроводниковый компонент, который управляет потоком
    электрического тока в цепи. Он может работать в различных режимах, таких
    как усиление сигнала, коммутация и стабилизация напряжения. Транзисторы
    широко используются в электронных устройствах, таких как усилители,
    микропроцессоры, телевизоры и другие."""
    def __init__(self, name: str, transistor_type: str, voltage: float, 
                 amperage: float, collector: float, emitter: float,
                 wired_objects: list=[]):
        super().__init__(f'{transistor_type} {name}',
                         'Transistor', voltage, amperage, wired_objects)
        self.collector_current = collector
        self.transistor_type = transistor_type
        self.emitter_current = emitter
        if not self.verify_params():
            raise ValueError('Верификация данных провалена. Возможно, вы указали несуществующий тип транзистора')

    def verify_params(self) -> bool:
        if self.transistor_type.upper() in ['NPN', 'PNP', 'MOS-N', "MOS-P"]:
            return True

        return False

    def is_on(self):
        if self.transistor_type.upper() == 'NPN':
            return self.voltage > 0 and self.collector_current > 0 \
                                        and self.emitter_current > 0
        elif self.transistor_type.upper() == 'PNP':
            return self.voltage < 0 and self.collector_current < 0 \
                                        and self.emitter_current < 0
        elif self.transistor_type.upper() == 'MOS-N':
            return self.voltage > 0 and self.collector_current > 0 \
                                        and self.emitter_current > 0
        elif self.transistor_type.upper() == 'MOS-P':
            return self.voltage < 0 and self.collector_current < 0 \
                                        and self.emitter_current < 0
        else:
            return False

