from typing import Iterable

import attr

from mock_api.shared_kernel.types import FileType
from mock_api.shared_kernel.validators import BaseValidator


@attr.s(frozen=True, auto_attribs=True)
class FileValidator(BaseValidator):
    file_types: Iterable[FileType] = attr.ib(default=FileType.all_types())

    def validate(self) -> None:
        pass
