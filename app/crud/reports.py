from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models import Report


def fetch_reports(db: Session):
    reports =  db.query(Report).all()
    return reports

def fetch_report(id, db: Session):
    report = db.query(Report).filter(Report.id == id).first()
    if report is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Report with id of {id} was not found")
    return report

def create_reports(report, db: Session):
    new_report = Report(**report)
    db.add(new_report)
    db.commit()
    db.refresh(new_report)

    return new_report

def update_reports(id, updated_report, db: Session):
    report = db.query(Report).filter(Report.id == id). first()
    if report is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Report with id of {id} was not found")
    
    for key, value in updated_report.items():
        setattr(report, key, value)

    db.commit()
    db.refresh(report)

    return report

def delete_reports(id, db: Session):
    report = db.query(Report).filter(Report.id == id).first()

    if report is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Report with id of {id} was not found")
    
    db.delete(report)
    db.commit()

    return HTTPException(status_code=status.HTTP_204_NO_CONTENT)