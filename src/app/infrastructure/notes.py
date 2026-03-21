from app.application.ports.notes import INoteRepository
from app.domain.note import Note, NoteId


class InMemoryNoteRepository(INoteRepository):
    _notes: dict[NoteId, Note]

    @classmethod
    def init(cls) -> None:
        cls._notes = {}

    def save(self, note: Note) -> None:
        self._notes[note.id_] = note

    def get_by_id(self, note_id: NoteId) -> Note | None:
        return self._notes.get(note_id)

    def list_all(self) -> list[Note]:
        return list(self._notes.values())

    def delete(self, note_id: NoteId) -> None:
        try:
            self._notes.pop(note_id)
        except KeyError:
            raise
