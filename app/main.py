from fastapi import FastAPI
from app.routers import users, reports
from app.database import engine, Base


Base.metadata.create_all(bind=engine)


app = FastAPI()


@app.get("/")
def index():
    return {"message": "welcome"}


app.include_router(users.router)
app.include_router(reports.router)