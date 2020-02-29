from pydantic import BaseModel
from typing import List

class Question(BaseModel):
    id: int
    question: str

class Choice(BaseModel):
    id: int
    description: str

class Choices(BaseModel):
    choices: List[Choice]