from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ProjectVersion(Base):
    __tablename__ = "project_version"
    id = Column(Integer, primary_key=True)
    major = Column(Integer, nullable=False)
    minor = Column(Integer, nullable=False)
    patch = Column(Integer, nullable=False)


class Project(Base):
    __tablename__ = "project"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    version_id = Column(Integer, ForeignKey("project_version.id"), nullable=False)
