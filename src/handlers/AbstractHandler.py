from abc import ABC, abstractmethod


class AbstractHandler(ABC):
    @abstractmethod
    def handle_event(self, event):
        pass
