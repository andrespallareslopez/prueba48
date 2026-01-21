from __future__ import annotations

import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..db import get_db

router = APIRouter(prefix="/rag-databases", tags=["rag-databases"])


@router.get("/", response_model=list[schemas.RagDatabaseOut])
def list_rag_databases(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.rag_databases.list(db, skip=skip, limit=limit)


@router.get("/{rag_id}", response_model=schemas.RagDatabaseOut)
def get_rag_database(rag_id: uuid.UUID, db: Session = Depends(get_db)):
    obj = crud.rag_databases.get(db, rag_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Rag database not found")
    return obj


@router.post("/", response_model=schemas.RagDatabaseOut, status_code=status.HTTP_201_CREATED)
def create_rag_database(payload: schemas.RagDatabaseCreate, db: Session = Depends(get_db)):
    return crud.rag_databases.create(db, payload)


@router.put("/{rag_id}", response_model=schemas.RagDatabaseOut)
def update_rag_database(
    rag_id: uuid.UUID, payload: schemas.RagDatabaseUpdate, db: Session = Depends(get_db)
):
    obj = crud.rag_databases.get(db, rag_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Rag database not found")
    return crud.rag_databases.update(db, obj, payload)


@router.delete("/{rag_id}", response_model=schemas.RagDatabaseOut)
def delete_rag_database(rag_id: uuid.UUID, db: Session = Depends(get_db)):
    obj = crud.rag_databases.remove(db, rag_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Rag database not found")
    return obj
