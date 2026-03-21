from dataclasses import dataclass, field
from datetime import datetime
from typing import NewType
from uuid import UUID, uuid4


NoteId = NewType("NoteId", UUID)


@dataclass
class Note:
    title: str
    content: str
    id_: NoteId = field(default_factory=lambda: NoteId(uuid4()))
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
