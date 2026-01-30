from __future__ import annotations

import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..db import get_db

router = APIRouter(tags=["members"])


@router.get("/members/all", response_model=list[schemas.MemberOut], response_model_by_alias=True)
def list_members(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.members.list(db, skip=skip, limit=limit)


@router.get("/members/{member_id}", response_model=schemas.MemberOut, response_model_by_alias=True)
def get_member(member_id: uuid.UUID, db: Session = Depends(get_db)):
    obj = crud.members.get(db, member_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Member not found")
    return obj


@router.post(
    "/members/insert", response_model=schemas.MemberOut, status_code=status.HTTP_201_CREATED, response_model_by_alias=True
)
def create_member(payload: schemas.MemberCreate, db: Session = Depends(get_db)):
    return crud.members.create(db, payload)


@router.post("/members/update", response_model=schemas.MemberOut, response_model_by_alias=True)
def update_member(
    payload: schemas.MemberUpdate, db: Session = Depends(get_db)
):
    obj = crud.members.get(db, payload.id)
    if not obj:
        raise HTTPException(status_code=404, detail="Member not found")
    return crud.members.update(db, obj, payload)


@router.delete("/members/{member_id}", response_model=schemas.MemberOut, response_model_by_alias=True)
def delete_member(member_id: uuid.UUID, db: Session = Depends(get_db)):
    obj = crud.members.remove(db, member_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Member not found")
    return obj
