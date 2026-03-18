from abc import ABC, abstractmethod
from uuid import UUID

from vps_deployment.domain.entities.note import Note


class NoteRepository(ABC):

    @abstractmethod
    def save(self, note: Note) -> Note:
        ...

    @abstractmethod
    def get_by_id(self, note_id: UUID) -> Note | None:
        ...

    @abstractmethod
    def list_all(self) -> list[Note]:
        ...

    @abstractmethod
    def delete(self, note_id: UUID) -> bool:
        ...
