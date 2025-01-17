from fastapi import APIRouter, Depends, status
from typing import List
from app.schemas import JobInput, JobResponse
from app.database import get_db
from sqlalchemy.orm import Session
from app.crud.jobs import (
    fetch_job, fetch_jobs, create_jobs, delete_jobs, update_jobs
    )


router = APIRouter(prefix="/jobs", tags=["Jobs"])


@router.get("/", response_model=JobResponse)
def get_jobs(db: Session =  Depends(get_db)):
    jobs = fetch_jobs(db)
    return jobs


@router.get("/{id}", response_model=JobResponse)
def get_job(id: int, db: Session = Depends(get_db)):
    job = fetch_job(id, db)
    return job


@router.post("/", response_model=JobResponse, status_code=status.HTTP_201_CREATED)
def create_job(job: JobInput, db: Session = Depends(get_db)):
    new_job_dict = job.model_dump()
    new_job = create_jobs(new_job_dict, db)
    return new_job


@router.put("/{id}", response_model=JobResponse)
def update_job(id: int, job: JobInput, db: Session = Depends(get_db)):
    updated_job_dict = job.model_dump()
    updated_job = update_jobs(id, updated_job_dict, db)
    return updated_job


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_job(id: int, db: Session = Depends(get_db)):
    delete_jobs(id, db)
    return {"message": f"Job with id {id} has been deleted successfully."}