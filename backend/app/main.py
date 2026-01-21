from __future__ import annotations

from fastapi import FastAPI

from .routers import clients, projects, members_client, rag_databases, tools, members

app = FastAPI(title="EFFICIENCY API")

app.include_router(clients.router, prefix="/api")
app.include_router(projects.router, prefix="/api")
app.include_router(members_client.router, prefix="/api")
app.include_router(rag_databases.router, prefix="/api")
app.include_router(tools.router, prefix="/api")
app.include_router(members.router, prefix="/api")


@app.get("/")
def root():
    return {"status": "ok"}
