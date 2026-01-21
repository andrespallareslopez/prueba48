from __future__ import annotations

import uuid
from datetime import datetime

from pydantic import BaseModel, EmailStr


class ClientBase(BaseModel):
    name: str
    description: str | None = None


class ClientCreate(ClientBase):
    pass


class ClientUpdate(BaseModel):
    name: str | None = None
    description: str | None = None


class ClientOut(ClientBase):
    id: uuid.UUID

    class Config:
        from_attributes = True


class ProjectBase(BaseModel):
    client_id: uuid.UUID
    name: str
    description: str | None = None
    rag_id: uuid.UUID | None = None
    tool_id: uuid.UUID | None = None


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(BaseModel):
    client_id: uuid.UUID | None = None
    name: str | None = None
    description: str | None = None
    rag_id: uuid.UUID | None = None
    tool_id: uuid.UUID | None = None


class ProjectOut(ProjectBase):
    id: uuid.UUID

    class Config:
        from_attributes = True


class MemberClientBase(BaseModel):
    client_id: uuid.UUID
    name: str
    email: EmailStr
    role: str | None = None
    status: str | None = None


class MemberClientCreate(MemberClientBase):
    pass


class MemberClientUpdate(BaseModel):
    client_id: uuid.UUID | None = None
    name: str | None = None
    email: EmailStr | None = None
    role: str | None = None
    status: str | None = None


class MemberClientOut(MemberClientBase):
    id: uuid.UUID

    class Config:
        from_attributes = True


class RagDatabaseBase(BaseModel):
    member_id: uuid.UUID
    project_id: uuid.UUID
    name: str
    type: str | None = None
    last_update: datetime | None = None


class RagDatabaseCreate(RagDatabaseBase):
    pass


class RagDatabaseUpdate(BaseModel):
    member_id: uuid.UUID | None = None
    project_id: uuid.UUID | None = None
    name: str | None = None
    type: str | None = None
    last_update: datetime | None = None


class RagDatabaseOut(RagDatabaseBase):
    id: uuid.UUID

    class Config:
        from_attributes = True


class ToolBase(BaseModel):
    member_id: uuid.UUID
    project_id: uuid.UUID
    name: str
    type: str | None = None
    permission: str | None = None


class ToolCreate(ToolBase):
    pass


class ToolUpdate(BaseModel):
    member_id: uuid.UUID | None = None
    project_id: uuid.UUID | None = None
    name: str | None = None
    type: str | None = None
    permission: str | None = None


class ToolOut(ToolBase):
    id: uuid.UUID

    class Config:
        from_attributes = True


class MemberBase(BaseModel):
    member_id: uuid.UUID
    project_id: uuid.UUID
    name: str
    email: EmailStr
    role: str | None = None
    status: str | None = None
    rag_id: uuid.UUID | None = None
    tool_id: uuid.UUID | None = None


class MemberCreate(MemberBase):
    pass


class MemberUpdate(BaseModel):
    member_id: uuid.UUID | None = None
    project_id: uuid.UUID | None = None
    name: str | None = None
    email: EmailStr | None = None
    role: str | None = None
    status: str | None = None
    rag_id: uuid.UUID | None = None
    tool_id: uuid.UUID | None = None


class MemberOut(MemberBase):
    id: uuid.UUID

    class Config:
        from_attributes = True
