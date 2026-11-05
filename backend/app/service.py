from app.knowledge import SopSection, load_documents
from app.llm import generate_answer
from app.retrieval import retrieve_sections
from app.schemas import AnswerResponse, SourceReference


def format_evidence(sections: list[SopSection]) -> str:
    blocks = []

    for section in sections:
        blocks.append(
            f"Document: {section.title}\n"
            f"Document ID: {section.document_id}\n"
            f"version: {section.version}\n"
            f"Section: {section.section}\n"
            f"Owner: {section.owner}\n"
            f"Content: \n{section.content}"
        )

    return "\n\n---\n\n".join(blocks)
