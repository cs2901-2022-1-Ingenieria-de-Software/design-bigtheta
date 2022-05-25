from abc import ABC, abstractmethod
from device import Device

class Command(ABC):
    def __init__(self, device: Device) -> None:
        self.device = device

    @abstractmethod
    def execute(self) -> None:
        pass

class CommandTurnOn(Command):
    def __init__(self, device: Device) -> None:
        super().__init__(device)

    def execute(self) -> None:
        self.device.turn_on()

class CommandTurnOff(Command):
    def __init__(self, device: Device) -> None:
        super().__init__(device)

    def execute(self) -> None:
        self.device.turn_off()

class CommandSwitch(Command):
    def __init__(self, device: Device) -> None:
        super().__init__(device)

    def execute(self) -> None:
        self.device.switch()
