from fastapi import FastAPI
from model import *
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/")
async def predict_price(input_data: ModelInput):
    predict = Model(input_data).predict()
    return {"price": predict}


if __name__ == '__main__':
    print('FastAPI server is running...')