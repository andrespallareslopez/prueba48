from __future__ import annotations

import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..db import get_db
from typing import List

router = APIRouter( tags=["projects"])


@router.get("/projects/all", response_model=list[schemas.ProjectOut], response_model_by_alias=True)
def list_projects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.projects.list(db, skip=skip, limit=limit)


@router.get("/projects/{project_id}", response_model=schemas.ProjectOut, response_model_by_alias=True)
def get_project(project_id: uuid.UUID, db: Session = Depends(get_db)):
   
    obj = crud.projects.get(db, project_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Project not found")
    return obj

@router.get("/projects/list/{client_id}", response_model=List[schemas.ProjectOut], response_model_by_alias=True)
def list_projects_by_client(client_id: uuid.UUID, db: Session = Depends(get_db)):
    projects = db.query(crud.projects.model).filter_by(clientId=client_id).all()
    return projects

@router.get("/projects/members/{project_id}", response_model=List[schemas.MemberOut], response_model_by_alias=True)
def get_project_members(project_id: uuid.UUID, db: Session = Depends(get_db)):
    
    obj = db.query(crud.members.model).filter_by(projectId=project_id).all()
    
    
    return obj



@router.post(
    "/projects/insert", response_model=schemas.ProjectOut, status_code=status.HTTP_201_CREATED, response_model_by_alias=True
)
def create_project(payload: schemas.ProjectCreate, db: Session = Depends(get_db)):
    return crud.projects.create(db, payload)


@router.post("/projects/update", response_model=schemas.ProjectOut, response_model_by_alias=True)
def update_project(
    payload: schemas.ProjectUpdate, db: Session = Depends(get_db)
):
    obj = crud.projects.get(db, payload.id)
    if not obj:
        raise HTTPException(status_code=404, detail="Project not found")
    return crud.projects.update(db, obj, payload)


@router.delete("/projects/{project_id}", response_model=schemas.ProjectOut, response_model_by_alias=True)
def delete_project(project_id: uuid.UUID, db: Session = Depends(get_db)):
    obj = crud.projects.remove(db, project_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Project not found")
    return obj
