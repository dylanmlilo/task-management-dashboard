from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models import Job, Report, User


def fetch_jobs(db: Session):

    jobs = db.query(Job).all()

    return jobs


def fetch_job(id, db: Session):

    job = db.query(Job).filter(Job.id == id).first()
    if job is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Job with id of {id} was not found")
    
    return job


def create_jobs(job, db: Session):

    existing_report = db.query(Report).filter(Report.id == job["report_id"]).first()
    if existing_report is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Report with id of {job["report_id"]} was not found")
    
    existing_plumber = db.query(User).filter(User.id == job["plumber_id"]).first()
    if existing_plumber is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail=f"Plumber with id of {job["plumber_id"]} was not found")
    
    existing_job = db.query(Job).filter(Job.report_id == job['report_id']).first()
    if existing_job:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Job with id of {job['report_id']} exists")
    
    new_job = Job(**job)
    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return new_job


def update_jobs(id, updated_job, db: Session):

    job = db.query(Job).filter(Job.id == id).first()
    if job is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Job with id of {id} was not found")
    
    for key, value in updated_job.items():
        setattr(job, key, value)

    db.commit()
    db.refresh(job)

    return job
    

def delete_jobs(id, db: Session):

    job = db.query(Job).filter(Job.id == id).first()
    if job is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Job with id of {id} was not found")
    
    db.delete(job)
    db.commit()

    return HTTPException(status_code=status.HTTP_204_NO_CONTENT)