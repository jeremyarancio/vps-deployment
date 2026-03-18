from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter(prefix="/notes", tags=["notes"])


@router.post("/")
def create_note(
    payload: NoteCreate,
    repository: NoteRepository = Depends(get_note_repository),
) -> NoteResponse:
    note = CreateNote(repository).execute(title=payload.title, content=payload.content)
    return NoteResponse(**note.__dict__)


@router.get("/", response_model=list[NoteResponse])
def list_notes(
    repository: NoteRepository = Depends(get_note_repository),
) -> list[NoteResponse]:
    notes = ListNotes(repository).execute()
    return [NoteResponse(**n.__dict__) for n in notes]


@router.get("/{note_id}", response_model=NoteResponse)
def get_note(
    note_id: UUID,
    repository: NoteRepository = Depends(get_note_repository),
) -> NoteResponse:
    note = GetNote(repository).execute(note_id)
    if note is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Note not found"
        )
    return NoteResponse(**note.__dict__)


@router.patch("/{note_id}", response_model=NoteResponse)
def update_note(
    note_id: UUID,
    payload: NoteUpdate,
    repository: NoteRepository = Depends(get_note_repository),
) -> NoteResponse:
    note = UpdateNote(repository).execute(
        note_id, title=payload.title, content=payload.content
    )
    if note is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Note not found"
        )
    return NoteResponse(**note.__dict__)


@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(
    note_id: UUID,
    repository: NoteRepository = Depends(get_note_repository),
) -> None:
    deleted = DeleteNote(repository).execute(note_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Note not found"
        )
