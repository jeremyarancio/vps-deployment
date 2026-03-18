from uuid import UUID

from vps_deployment.domain.entities.note import Note
from vps_deployment.domain.repositories.note_repository import NoteRepository


class InMemoryNoteRepository(NoteRepository):

    def __init__(self) -> None:
        self._store: dict[UUID, Note] = {}

    def save(self, note: Note) -> Note:
        self._store[note.id] = note
        return note

    def get_by_id(self, note_id: UUID) -> Note | None:
        return self._store.get(note_id)

    def list_all(self) -> list[Note]:
        return list(self._store.values())

    def delete(self, note_id: UUID) -> bool:
        if note_id in self._store:
            del self._store[note_id]
            return True
        return False
