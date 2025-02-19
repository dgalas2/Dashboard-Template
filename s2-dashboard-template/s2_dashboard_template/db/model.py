from pydantic import BaseModel

class Book(BaseModel):
    name: str
    isbn: str
    pageCount: int