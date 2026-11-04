from typing import Literal

from pydantic import BaseModel, Field

class QuestionRequest(BaseModel):
    question: str = Field(
        min_length=5,
        max_length=1000,
        strip_whitespace=True,
    )


class SourceReference(BaseModel):
    document_id: str
    title: str
    section: str
    version: str


class AnswerResponse(BaseModel):
    status: Literal[
        "answered",
        "not_found",
        "needs_review",
    ]
    answer:str
    sources: list[SourceReference]
    next_step: str | None = None



