from __future__ import annotations

import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..db import get_db
from typing import List
from pprint import pprint


router = APIRouter( tags=["clients"])


@router.get("/clients/all", response_model=List[schemas.ClientOut], response_model_by_alias=True)
def list_clients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    #print(client._id for client in crud.clients.list(db, skip=skip, limit=limit))
    return crud.clients.list(db, skip=skip, limit=limit)


@router.get("/clients/{client_id}", response_model=schemas.ClientOut, response_model_by_alias=True)
def get_client(client_id: uuid.UUID, db: Session = Depends(get_db)):
    obj = crud.clients.get(db, client_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Client not found")
    return obj


@router.post(
    "/clients/insert", response_model=schemas.ClientOut, status_code=status.HTTP_201_CREATED, response_model_by_alias=True
)
def create_client(payload: schemas.ClientCreate, db: Session = Depends(get_db)):
    return crud.clients.create(db, payload)


@router.post("/clients/update", response_model=schemas.ClientOut, response_model_by_alias=True)
def update_client(
     payload: schemas.ClientUpdate, db: Session = Depends(get_db)
):
    
    obj = crud.clients.get(db, payload.id)
    pprint(obj.__dict__)
    
    if not obj:
        raise HTTPException(status_code=404, detail="Client not found")
    return crud.clients.update(db, obj, payload)


@router.delete("/clients/{client_id}", response_model=schemas.ClientOut, response_model_by_alias=True)
def delete_client(client_id: uuid.UUID, db: Session = Depends(get_db)):
    obj = crud.clients.remove(db, client_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Client not found")
    return obj
