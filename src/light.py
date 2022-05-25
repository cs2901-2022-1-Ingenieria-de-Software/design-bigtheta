from device import Device

class Light(Device):
    def __init__(self, color: str, *args) -> None:
        self.color = color
        super().__init__(*args)

    def print_state(self) -> None:
        if self.get_state():
            print(f'{self.color} light is on.')
        else:
            print(f'{self.color} light is off.')

class RedLight(Light):
    def __init__(self, *args) -> None:
        super().__init__('Red', *args)

class YellowLight(Light):
    def __init__(self, *args) -> None:
        super().__init__('Yellow', *args)

class WhiteLight(Light):
    def __init__(self, *args) -> None:
        super().__init__('White', *args)
