import re

from app.knowledge import SopSection


STOP_WORDS = {
    "a", "an", "the", "is", "are", "was", "were",
    "what", "when", "where", "who", "why", "how",
    "do", "does", "did", "should", "can", "could",
    "i", "we", "you", "they", "it", "my", "our",
    "to", "for", "of", "in", "on", "at", "by",
    "and", "or", "but", "if", "with", "from",
    "me", "please", "provide", "tell", "explain",
    "about", "submit", "submitting",
}


def tokenize(text: str) -> set[str]:
    words = set(re.findall(r"[a-z0-9]+", text.lower()))
    return words - STOP_WORDS

def retrieve_sections(
        question: str,
        sections: list[SopSection],
        threshold: float = 0.15,
        limit: int = 3,
) -> list[SopSection]:

    


