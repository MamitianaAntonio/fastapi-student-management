from fastapi import FastAPI
from database import engine, Base
from routers import students

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student management API", version="1.0.0")

app.include_router(students.router)


@app.get("/")
def root():
    return {"Message :Welcome to student management api"}
