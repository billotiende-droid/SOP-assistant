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

    question_terms = tokenize(question)

    if not question_terms:
        return []

    scored = []

    for section in sections:
        searchable_text = (
            f"{section.section} {section.title} {section.content}"
        )

        section_terms = tokenize(searchable_text)
        overlap = question_terms & section_terms

        # how much of the questions meaningful vocabulary matches?
        score = len(overlap) / len(question_terms)

        if score >= threshold:
            score.append((score, section))

    


