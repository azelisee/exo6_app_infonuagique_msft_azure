from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI()
# Allow all origins

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Name(BaseModel):
    num1: float
    num2: float

@app.post('/prod')
async def welcome(num: float):
    return {f"The product is {num.num1 * num.num2}"}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8802)
