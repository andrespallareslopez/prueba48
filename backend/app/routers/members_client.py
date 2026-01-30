from __future__ import annotations

import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..db import get_db
from typing import List

router = APIRouter( tags=["members-client"])


@router.get("/client/project/all", response_model=list[schemas.MemberClientOut], response_model_by_alias=True)
def list_members_client(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.members_client.list(db, skip=skip, limit=limit)


@router.get("/client/project/{member_client_id}", response_model=schemas.MemberClientOut, response_model_by_alias=True)
def get_member_client(member_client_id: uuid.UUID, db: Session = Depends(get_db)):
    obj = crud.members_client.get(db, member_client_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Member client not found")
    return obj
@router.get("/client/project/list/{member_client_id}", response_model=List[schemas.MemberClientOut], response_model_by_alias=True)
def get_member_client(member_client_id: uuid.UUID, db: Session = Depends(get_db)):
    obj =db.query(crud.members_client.model).filter_by(clientId=member_client_id).all()
    return obj


@router.post(
    "/client/project/insert", response_model=schemas.MemberClientOut, status_code=status.HTTP_201_CREATED, response_model_by_alias=True
)
def create_member_client(payload: schemas.MemberClientCreate, db: Session = Depends(get_db)):
    return crud.members_client.create(db, payload)


@router.post(
    "/client/project/update", response_model=schemas.MemberClientOut, response_model_by_alias=True
)
def update_member_client(
    payload: schemas.MemberClientUpdate,
    db: Session = Depends(get_db),
):
    obj = crud.members_client.get(db, payload.id)
    if not obj:
        raise HTTPException(status_code=404, detail="Member client not found")
    return crud.members_client.update(db, obj, payload)


@router.delete(
    "/client/project/{member_client_id}", response_model=schemas.MemberClientOut, response_model_by_alias=True
)
def delete_member_client(member_client_id: uuid.UUID, db: Session = Depends(get_db)):
    obj = crud.members_client.remove(db, member_client_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Member client not found")
    return obj
