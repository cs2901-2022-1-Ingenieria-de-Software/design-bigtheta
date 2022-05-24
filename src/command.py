from abc import ABC, abstractmethod
from device import Device

class Command(ABC):
    def __init__(self, device: Device) -> None:
        self.device = device

    @abstractmethod
    def execute(self) -> None:
        pass

class Command_turn_on(Command):
    def __init__(self, device: Device) -> None:
        super().__init__(device)

    def execute(self) -> None:
        self.device.turn_on()

class Command_turn_off(Command):
    def __init__(self, device: Device) -> None:
        super().__init__(device)

    def execute(self) -> None:
        self.device.turn_off()

class Command_switch(Command):
    def __init__(self, device: Device) -> None:
        super().__init__(device)

    def execute(self) -> None:
        self.device.switch()
