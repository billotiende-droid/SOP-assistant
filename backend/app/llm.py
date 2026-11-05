from functools import lru_cache

from google import genai
from google.genai import types
from pydantic import BaseModel, Field



from app.config import get_settings



class AIAnswer(BaseModel):
    supported: bool
    answer: str = Field(min_length=1)


class AIServiceError(Exception):
    """ Raised when AI provider cant produce a usable result. """


@lru_cache
def get_gemini_client() -> genai.Client:
    settings = get_settings()
    return genai.Client(api_key=settings.gemini_api_key)


def generate_answer(
        question: str,
        evidence: str,
) -> AIAnswer:

    settings = get_settings()
    client = get_gemini_client()
