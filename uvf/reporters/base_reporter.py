from abc import ABC, abstractmethod

class BaseReporter(ABC):
    @abstractmethod
    def generate(self):
        """
        Generate report
        :return:
        """
        pass