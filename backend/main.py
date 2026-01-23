import json
from fastapi import FastAPI
from models import Data
from pathlib import Path


app = FastAPI()


@app.get("/data", response_model=list[Data])
def get_data() -> list[Data]:
    data = Path("data/mock.json").read_text()
    list_of_data = [Data.model_validate(item) for item in json.loads(data)]
    return list_of_data