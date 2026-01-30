from __future__ import annotations

import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..db import get_db
from typing import List

router = APIRouter( tags=["rag-databases"])


@router.get("/rag-databases/all", response_model=list[schemas.RagDatabaseOut], response_model_by_alias=True)
def list_rag_databases(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.rag_databases.list(db, skip=skip, limit=limit)


@router.get("/rag-databases/{rag_id}", response_model=schemas.RagDatabaseOut, response_model_by_alias=True)
def get_rag_database(rag_id: uuid.UUID, db: Session = Depends(get_db)):
    obj = crud.rag_databases.get(db, rag_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Rag database not found")
    return obj

@router.get("/rag-databases/member/{member_id}", response_model=List[schemas.RagDatabaseOut], response_model_by_alias=True)
def get_rag_database_member(member_id: uuid.UUID, db: Session = Depends(get_db)):
    #obj = crud.rag_databases.get(db, member_id)
    obj = db.query(crud.rag_databases.model).filter_by(memberId=member_id).all()
    return obj

@router.get("/rag-databases/project/{project_id}", response_model=List[schemas.RagDatabaseOut], response_model_by_alias=True)
def get_rag_database_project(project_id: uuid.UUID, db: Session = Depends(get_db)):
    #obj = crud.rag_databases.get(db, rag_id)
    obj = db.query(crud.rag_databases.model).filter_by(projectId=project_id).all()    
    return obj

@router.post(
    "/rag-databases/insert", response_model=schemas.RagDatabaseOut, status_code=status.HTTP_201_CREATED, response_model_by_alias=True
)
def create_rag_database(payload: schemas.RagDatabaseCreate, db: Session = Depends(get_db)):
    return crud.rag_databases.create(db, payload)


@router.post("/rag-databases/update", response_model=schemas.RagDatabaseOut, response_model_by_alias=True)
def update_rag_database(
    payload: schemas.RagDatabaseUpdate, db: Session = Depends(get_db)
):
    obj = crud.rag_databases.get(db, payload.id)
    if not obj:
        raise HTTPException(status_code=404, detail="Rag database not found")
    return crud.rag_databases.update(db, obj, payload)


@router.delete("/rag-databases/{rag_id}", response_model=schemas.RagDatabaseOut, response_model_by_alias=True)
def delete_rag_database(rag_id: uuid.UUID, db: Session = Depends(get_db)):
    obj = crud.rag_databases.remove(db, rag_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Rag database not found")
    return obj
