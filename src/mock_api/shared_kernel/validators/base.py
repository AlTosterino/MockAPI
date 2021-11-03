from abc import ABC as Abstract, abstractmethod
from typing import Any

import attr


@attr.s(frozen=True, auto_attribs=True)
class BaseValidator(Abstract):
    to_validate: Any

    @abstractmethod
    def validate(self) -> None:
        pass
