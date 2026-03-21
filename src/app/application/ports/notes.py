from abc import ABC, abstractmethod

from app.domain.note import Note, NoteId


class INoteRepository(ABC):
    @abstractmethod
    def save(self, note: Note) -> None: ...

    @abstractmethod
    def get_by_id(self, note_id: NoteId) -> Note | None: ...

    @abstractmethod
    def list_all(self) -> list[Note]: ...

    @abstractmethod
    def delete(self, note_id: NoteId) -> None: ...
