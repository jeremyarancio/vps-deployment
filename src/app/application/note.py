from app.application.exceptions import NotFoundException
from app.application.ports.notes import INoteRepository
from app.domain.note import Note, NoteId


class NoteService:
    @staticmethod
    def create(note: Note, repository: INoteRepository) -> None:
        return repository.save(note=note)

    @staticmethod
    def list(repository: INoteRepository) -> list[Note]:
        return repository.list_all()

    @staticmethod
    def get(note_id: NoteId, repository: INoteRepository) -> Note:
        note = repository.get_by_id(note_id=note_id)
        if note:
            return note
        raise NotFoundException()

    @staticmethod
    def delete(note_id: NoteId, repository: INoteRepository) -> None:
        try:
            repository.delete(note_id=note_id)
        except Exception:
            raise NotFoundException
