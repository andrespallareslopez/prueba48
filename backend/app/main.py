from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import clients, projects, members_client, rag_databases, tools, members

app = FastAPI(title="EFFICIENCY API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(clients.router, prefix="/api")
app.include_router(projects.router, prefix="/api")
app.include_router(members_client.router, prefix="/api")
app.include_router(rag_databases.router, prefix="/api")
app.include_router(tools.router, prefix="/api")
app.include_router(members.router, prefix="/api")


@app.get("/")
def root():
    return {"status": "ok"}
