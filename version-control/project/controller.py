from typing import Tuple

from fastapi import HTTPException, Depends, APIRouter, Request
from pydantic import BaseModel
from sqlalchemy.orm import Session

from connection import get_db
from usecase import CreateProject

router = APIRouter()


class ProjectCreate(BaseModel):
    name: str
    version: str


@router.post("/project")
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    try:
        project = CreateProject(db).execute(project.name, project.version)
        return {"id": project.id}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error creating project")

