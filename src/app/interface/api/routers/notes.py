from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Response

from app.application.note import NoteService
from app.application.ports.notes import INoteRepository
from app.domain.note import NoteId
from app.interface.dependencies import get_note_repository
from app.interface.schemas import NoteCreate, NoteResponse


router = APIRouter(prefix="/notes", tags=["notes"])


@router.post("")
def create_note(
    payload: NoteCreate,
    repository: Annotated[INoteRepository, Depends(get_note_repository)],
) -> Response:
    note = payload.to_note()
    NoteService.create(note=note, repository=repository)
    return Response(content="Note created.", status_code=201)


@router.get("")
def list_notes(
    repository: Annotated[INoteRepository, Depends(get_note_repository)],
) -> list[NoteResponse]:
    return [NoteResponse.from_note(n) for n in NoteService.list(repository)]


@router.get("/{note_id}")
def get_note(
    note_id: UUID,
    repository: Annotated[INoteRepository, Depends(get_note_repository)],
) -> NoteResponse:
    note = NoteService.get(note_id=NoteId(note_id), repository=repository)
    return NoteResponse.from_note(note)


@router.delete("/{note_id}")
def delete_note(
    note_id: UUID,
    repository: Annotated[INoteRepository, Depends(get_note_repository)],
) -> Response:
    NoteService.delete(note_id=NoteId(note_id), repository=repository)
    return Response(content="Note deleted.", status_code=204)
