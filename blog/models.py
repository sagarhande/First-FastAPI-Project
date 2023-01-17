from pydantic import BaseModel
from typing import Union, Optional


class Blog(BaseModel):
    name: str
    brief: Union[str, None] = None
    body: str
    published: Optional[bool]
