from pydantic import BaseModel
from typing import Union, Optional


class Blog(BaseModel):
    title: str
    brief: Union[str, None] = None
    body: str
    published: Optional[bool] = False
