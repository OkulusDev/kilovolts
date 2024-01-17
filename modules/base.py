

class Component:
    """Компонент"""
    def __init__(self, name: str, component_type: str, voltage: float, 
                 resistance: float, amperage: float, wired_objects: list=[]):
        """Инициализация
        
        Ввод:
            name: str - Имя компонента
            wired_with - С каким объектом проведен провод (None по умолчанию)"""
        self.wired_objects: list = wired_objects    # колво связных объектов
        self.name = name                            # имя компонента
        self.component = component_type             # тип компонента
        self.amperage = amperage                    # ток (амперы)
        self.voltage = voltage                      # напряжение (вольты)
        self.resistance = resistance                # сопротивление

    def get_name(self) -> str:
        """Получение полного имени компонента

        Вывод:
            str"""
        return f'Component {self.component} {self.name} (amperage: {self.amperage}; voltage: {self.voltage})'
    
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
        return f'Component {self.component} {self.name}'
