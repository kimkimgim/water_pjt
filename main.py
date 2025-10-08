from typing import Union

from fastapi import FastAPI


app = FastAPI(
    title="WaterPJT",
    description="Raspberry Pi Camera Monitor"
)



@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/")


# 실행 코드 : uvicorn main:app --reload