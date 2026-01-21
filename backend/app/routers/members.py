from __future__ import annotations

import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..db import get_db

router = APIRouter(prefix="/members", tags=["members"])


@router.get("/", response_model=list[schemas.MemberOut])
def list_members(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.members.list(db, skip=skip, limit=limit)


@router.get("/{member_id}", response_model=schemas.MemberOut)
def get_member(member_id: uuid.UUID, db: Session = Depends(get_db)):
    obj = crud.members.get(db, member_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Member not found")
    return obj


@router.post("/", response_model=schemas.MemberOut, status_code=status.HTTP_201_CREATED)
def create_member(payload: schemas.MemberCreate, db: Session = Depends(get_db)):
    return crud.members.create(db, payload)


@router.put("/{member_id}", response_model=schemas.MemberOut)
def update_member(
    member_id: uuid.UUID, payload: schemas.MemberUpdate, db: Session = Depends(get_db)
):
    obj = crud.members.get(db, member_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Member not found")
    return crud.members.update(db, obj, payload)


@router.delete("/{member_id}", response_model=schemas.MemberOut)
def delete_member(member_id: uuid.UUID, db: Session = Depends(get_db)):
    obj = crud.members.remove(db, member_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Member not found")
    return obj
