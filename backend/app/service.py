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


def answer_question(question: str) -> AnswerResponse:
    sections = load_documents()

    matches = retrieve_sections(question, sections)

    # No useful evidence: do not call model i.e retrieval before generation
    if not matches:
        return AnswerResponse(
            status="not_found",
            answer=(
                "I could not veirfy this information in the "
                "approved procedures available to me"
            ),
            sources=[],
            next_step=(
                "Contact the appropriate process owner listed"
                "in the relevant procedure, or ask your"
                "supervisor to identify the owner"
            ),
        )

    evidence = format_evidence(matches)

    result = generate_answer(
        question=question,
        evidence=evidence,
    )

    if not result.supported:
        return AnswerResponse(
            status="needs_review",
            answer=result.answer,
            sources=[],
            next_step=(
                "Ask the relevant process owner to confirm"
                "the procedure"
            ),
        )

    sources = [
        SourceReference(
            document_id=section.document_id,
            title=section.title,
            section=section.section,
            version=section.version

        )
        for section in matches
    ]

    return AnswerResponse(
        status="answered",
        answer=result.answer,
        sources=sources,
        next_step=None,
    )