from __future__ import annotations

from enum import Enum, auto
from typing import Iterable


class FileType(Enum):
    JSON = auto()
    YAML = auto()

    @classmethod
    def all_types(cls) -> Iterable[FileType]:
        return tuple(file_type for file_type in cls)
