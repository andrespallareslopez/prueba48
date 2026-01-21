from __future__ import annotations

import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..db import get_db

router = APIRouter(prefix="/clients", tags=["clients"])


@router.get("/", response_model=list[schemas.ClientOut])
def list_clients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.clients.list(db, skip=skip, limit=limit)


@router.get("/{client_id}", response_model=schemas.ClientOut)
def get_client(client_id: uuid.UUID, db: Session = Depends(get_db)):
    obj = crud.clients.get(db, client_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Client not found")
    return obj


@router.post("/", response_model=schemas.ClientOut, status_code=status.HTTP_201_CREATED)
def create_client(payload: schemas.ClientCreate, db: Session = Depends(get_db)):
    return crud.clients.create(db, payload)


@router.put("/{client_id}", response_model=schemas.ClientOut)
def update_client(
    client_id: uuid.UUID, payload: schemas.ClientUpdate, db: Session = Depends(get_db)
):
    obj = crud.clients.get(db, client_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Client not found")
    return crud.clients.update(db, obj, payload)


@router.delete("/{client_id}", response_model=schemas.ClientOut)
def delete_client(client_id: uuid.UUID, db: Session = Depends(get_db)):
    obj = crud.clients.remove(db, client_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Client not found")
    return obj
