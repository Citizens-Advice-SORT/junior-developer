from pydantic import BaseModel


class Source(BaseModel):
    id: str
    title: str
    source: str


class Data(BaseModel):
    category: str
    question: str
    sources: list[Source]
    content: str
