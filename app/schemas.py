from pydantic import BaseModel
from datetime import datetime


class UserInput(BaseModel):
    fullname: str
    username: str
    email: str
    hashed_password: str
    role: str


class UserResponse(BaseModel):
    id: int
    fullname: str
    username: str
    email: str
    role: str
    created_at: datetime
    updated_at :datetime

    class Config:
        from_attributes = True  #used to be orm_mode = True
        json_encoders = {
            datetime: lambda v: v.isoformat(),
        }


class ReportInput(BaseModel):
    description: str
    address: str
    type: str
    zone: str
    manager_id: int


class ReportResponse(BaseModel):
    id: int
    manager_id: int
    description: str
    address: str
    type: str
    status: str
    zone: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        json_encoders = {
            datetime: lambda v: v.isoformat(),
        }
    


class JobInput(BaseModel):
    status: str
    report_id: int
    plumber_id: int


class JobResponse(BaseModel):
    id: int
    status: str
    report_id: int
    plumber_id: int
    created_at: datetime
    updated_at :datetime

    class Config:
        from_attributes = True
        json_encoders = {
            datetime: lambda v: v.isoformat(),
        }