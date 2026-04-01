from abc import ABC, abstractmethod

from pybroker.model import Credentials


class AbstractAuthenticationProvider(ABC):
    @abstractmethod
    def authenticate(self, credentials: Credentials) -> bool:
        pass
