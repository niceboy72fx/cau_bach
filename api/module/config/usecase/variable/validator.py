from typing import Optional

from ninja import Schema


class CreateVariableInput(Schema):
    key: str
    value: str
    description: str = ""
    type: int


class UpdateVariableInput(Schema):
    key: Optional[str]
    value: Optional[str]
    description: Optional[str]
    type: Optional[int]
