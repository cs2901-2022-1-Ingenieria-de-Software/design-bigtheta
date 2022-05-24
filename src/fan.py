from device import Device

class Fan(Device):
    def __init__(self, *args) -> None:
        super().__init__(*args)

    def print_state(self) -> None:
        if self.state:
            print(f'Fan is on.')
        else:
            print(f'Fan is off.')
