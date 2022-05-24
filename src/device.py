from __future__ import annotations
from abc import ABC, abstractmethod

class Device(ABC):
    # NOTE: False state means off while True means on
    def __init__(self) -> None:
        self.state = False

    def set_state(self, state: bool) -> None:
        if self.state != state:
            self.state = state

    def get_state(self) -> bool:
        return self.state

    def turn_on(self) -> None:
        self.set_state(True)
        print(f'Device turn on, state: {self.state}.')

    def turn_off(self) -> None:
        self.set_state(False)
        print(f'Device turn off, state: {self.state}.')

    def switch(self) -> None:
        self.state = not self.state
        print(f'Device switch, state: {self.state}.')

    @abstractmethod
    def print_state(self) -> None:
        pass
