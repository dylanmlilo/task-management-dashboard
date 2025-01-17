from fastapi import APIRouter, Depends, status
from app.schemas import ReportInput, ReportResponse
from app.database import get_db
from sqlalchemy.orm import Session
from app.crud.reports import (
    fetch_reports, fetch_report, create_reports, update_reports, delete_reports
)
from typing import List


router = APIRouter(prefix="/reports", tags=["Reports"])


@router.get("/", response_model=List[ReportResponse])
def get_reports(db: Session = Depends(get_db)):
    reports = fetch_reports(db)
    return reports


@router.get("/{id}", response_model=ReportResponse)
def get_report(id: int, db: Session = Depends(get_db)):
    report = fetch_report(id, db)
    return report


@router.post("/", response_model=ReportResponse, status_code=status.HTTP_201_CREATED)
def create_report(report: ReportInput, db: Session = Depends(get_db)):
    new_report_dict = report.model_dump()
    new_report = create_reports(new_report_dict, db)
    return new_report


@router.put("/{id}", response_model=ReportResponse)
def update_report(id: int, report: ReportInput, db: Session = Depends(get_db)):
    updated_report_dict = report.model_dump()
    updated_report = update_reports(id, updated_report_dict, db)

    return updated_report


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_report(id: int, db: Session = Depends(get_db)):
    delete_reports(id, db)

    return {"message": f"Report with id {id} has been deleted successfully."}