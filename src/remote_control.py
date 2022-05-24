from device import Device
from singleton_decorator import singleton

@singleton
class Remote_control():
    _devices = {}
    _turn_on: type
    _turn_off: type
    _switch: type

    def __init__(self, command_on: type, command_off: type, command_switch: type) -> None:
        self._turn_on = command_on
        self._turn_off = command_off
        self._switch = command_switch

    def add_device(self, name: str, device: Device) -> None:
        self._devices[name] = device

    def get_device(self, name) -> Device:
        return self._devices[name]

    def set_turn_on(self, command: type) -> None:
        self._turn_on = command

    def set_turn_off(self, command: type) -> None:
        self._turn_off = command

    def set_switch(self, command: type) -> None:
        self._swtich = command

    def turn_on(self, name: str) -> None:
        turn_on_button = self._turn_on(self.get_device(name))
        turn_on_button.execute()

    def turn_off(self, name: str) -> None:
        turn_off_button = self._turn_off(self.get_device(name))
        turn_off_button.execute()

    def switch(self, name: str) -> None:
        switch_button = self._switch(self.get_device(name))
        switch_button.execute()
