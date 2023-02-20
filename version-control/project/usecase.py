from typing import Tuple
from sqlalchemy.orm import Session

from model import Project, ProjectVersion


class CreateProject:
    def __init__(self, db: Session):
        self.db = db

    def execute(self, name: str, version: str) -> Project:
        major, minor, patch = version.split(".")
        version_db = ProjectVersion(major=major, minor=minor, patch=patch)
        self.db.add(version_db)
        self.db.flush()
        project_db = Project(name=name, version_id=version_db.id)
        self.db.add(project_db)
        self.db.commit()
        self.db.refresh(project_db)
        return project_db


class GetProject:
    def __init__(self, db: Session):
        self.db = db

    def execute(self, name: str, version: str) -> Project:
        major, minor, patch = version.split(".")
        version_db = ProjectVersion(major=major, minor=minor, patch=patch)
        self.db.add(version_db)
        self.db.flush()
        project_db = Project(name=name, version_id=version_db.id)
        self.db.add(project_db)
        self.db.commit()
        self.db.refresh(project_db)
        return project_db