from app.application.ports.notes import INoteRepository
from app.infrastructure.notes import InMemoryNoteRepository


def get_note_repository() -> INoteRepository:
    return InMemoryNoteRepository()
