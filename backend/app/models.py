from __future__ import annotations

import uuid

from sqlalchemy import MetaData, String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    metadata = MetaData(schema="ibiols")


class Clients(Base):
    __tablename__ = "clients"

    id: Mapped[uuid.UUID] = mapped_column("_id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(90), nullable=False)
    description: Mapped[str | None] = mapped_column(String(255))


class ProjectsClient(Base):
    __tablename__ = "projects_client"

    id: Mapped[uuid.UUID] = mapped_column("_id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    clientId: Mapped[uuid.UUID] = mapped_column(
        "clientid",
        UUID(as_uuid=True),
        ForeignKey("ibiols.clients._id", ondelete="CASCADE"),
        nullable=False,
    )
    name: Mapped[str] = mapped_column(String(90), nullable=False)
    description: Mapped[str | None] = mapped_column(String(255))
   


class MembersClient(Base):
    __tablename__ = "members_client"
    
    id: Mapped[uuid.UUID] = mapped_column("_id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    clientId: Mapped[uuid.UUID] = mapped_column(
        "clientid",
        UUID(as_uuid=True),
        ForeignKey("ibiols.clients._id", ondelete="CASCADE"),
        nullable=False,
    )
    name: Mapped[str] = mapped_column(String(90), nullable=False)
    email: Mapped[str] = mapped_column(String(120), nullable=False)
    role: Mapped[str | None] = mapped_column(String(90))
    status: Mapped[str | None] = mapped_column(String(90))
    

class RagDatabases(Base):
    __tablename__ = "rag_databases"

    id: Mapped[uuid.UUID] = mapped_column("_id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    memberId: Mapped[uuid.UUID] = mapped_column(
        "memberid",
        UUID(as_uuid=True),
        ForeignKey("ibiols.members_client._id", ondelete="CASCADE"),
        nullable=False,
    )
    projectId: Mapped[uuid.UUID] = mapped_column(
        "projectid",
        UUID(as_uuid=True),
        ForeignKey("ibiols.projects_client._id", ondelete="CASCADE"),
        nullable=False,
    )
    name: Mapped[str] = mapped_column(String(90), nullable=False)
    type: Mapped[str | None] = mapped_column(String(90))
    lastUpdate: Mapped[DateTime | None] = mapped_column("last_update",DateTime)


class Tools(Base):
    __tablename__ = "tools"

    id: Mapped[uuid.UUID] = mapped_column("_id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    memberId: Mapped[uuid.UUID] = mapped_column(
        "memberid",
        UUID(as_uuid=True),
        ForeignKey("ibiols.members_client._id", ondelete="CASCADE"),
        nullable=False,
    )
    projectId: Mapped[uuid.UUID] = mapped_column(
        "projectid",
        UUID(as_uuid=True),
        ForeignKey("ibiols.projects_client._id", ondelete="CASCADE"),
        nullable=False,
    )
    name: Mapped[str] = mapped_column(String(90), nullable=False)
    type: Mapped[str | None] = mapped_column(String(90))
    permission: Mapped[str | None] = mapped_column(String(90))


class Members(Base):
    __tablename__ = "members"

    id: Mapped[uuid.UUID] = mapped_column("_id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    memberId: Mapped[uuid.UUID] = mapped_column(
        "memberid",
        UUID(as_uuid=True),
        ForeignKey("ibiols.members_client._id", ondelete="CASCADE"),
        nullable=False,
    )
    projectId: Mapped[uuid.UUID] = mapped_column(
        "projectid",
        UUID(as_uuid=True),
        ForeignKey("ibiols.projects_client._id", ondelete="CASCADE"),
        nullable=False,
    )
    name: Mapped[str] = mapped_column(String(90), nullable=False)
    email: Mapped[str] = mapped_column(String(120), nullable=False)
    role: Mapped[str | None] = mapped_column(String(90))
    status: Mapped[str | None] = mapped_column(String(90))
   
