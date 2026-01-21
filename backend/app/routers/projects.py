from __future__ import annotations

import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..db import get_db

router = APIRouter(prefix="/projects", tags=["projects"])


@router.get("/", response_model=list[schemas.ProjectOut])
def list_projects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.projects.list(db, skip=skip, limit=limit)


@router.get("/{project_id}", response_model=schemas.ProjectOut)
def get_project(project_id: uuid.UUID, db: Session = Depends(get_db)):
    obj = crud.projects.get(db, project_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Project not found")
    return obj


@router.post("/", response_model=schemas.ProjectOut, status_code=status.HTTP_201_CREATED)
def create_project(payload: schemas.ProjectCreate, db: Session = Depends(get_db)):
    return crud.projects.create(db, payload)


@router.put("/{project_id}", response_model=schemas.ProjectOut)
def update_project(
    project_id: uuid.UUID, payload: schemas.ProjectUpdate, db: Session = Depends(get_db)
):
    obj = crud.projects.get(db, project_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Project not found")
    return crud.projects.update(db, obj, payload)


@router.delete("/{project_id}", response_model=schemas.ProjectOut)
def delete_project(project_id: uuid.UUID, db: Session = Depends(get_db)):
    obj = crud.projects.remove(db, project_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Project not found")
    return obj
