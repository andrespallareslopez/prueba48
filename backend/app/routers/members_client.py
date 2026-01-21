from __future__ import annotations

import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..db import get_db

router = APIRouter(prefix="/members-client", tags=["members-client"])


@router.get("/", response_model=list[schemas.MemberClientOut])
def list_members_client(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.members_client.list(db, skip=skip, limit=limit)


@router.get("/{member_client_id}", response_model=schemas.MemberClientOut)
def get_member_client(member_client_id: uuid.UUID, db: Session = Depends(get_db)):
    obj = crud.members_client.get(db, member_client_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Member client not found")
    return obj


@router.post("/", response_model=schemas.MemberClientOut, status_code=status.HTTP_201_CREATED)
def create_member_client(payload: schemas.MemberClientCreate, db: Session = Depends(get_db)):
    return crud.members_client.create(db, payload)


@router.put("/{member_client_id}", response_model=schemas.MemberClientOut)
def update_member_client(
    member_client_id: uuid.UUID,
    payload: schemas.MemberClientUpdate,
    db: Session = Depends(get_db),
):
    obj = crud.members_client.get(db, member_client_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Member client not found")
    return crud.members_client.update(db, obj, payload)


@router.delete("/{member_client_id}", response_model=schemas.MemberClientOut)
def delete_member_client(member_client_id: uuid.UUID, db: Session = Depends(get_db)):
    obj = crud.members_client.remove(db, member_client_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Member client not found")
    return obj
