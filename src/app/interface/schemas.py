from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from app.domain.note import Note


class NoteCreate(BaseModel):
    title: str
    content: str

    def to_note(self) -> Note:
        return Note(title=self.title, content=self.content)


class NoteUpdate(BaseModel):
    title: str | None = None
    content: str | None = None


class NoteResponse(BaseModel):
    id_: UUID
    title: str
    content: str
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_note(cls, note: Note) -> "NoteResponse":
        return cls(
            id_=note.id_,
            title=note.title,
            content=note.content,
            created_at=note.created_at,
            updated_at=note.updated_at,
        )
