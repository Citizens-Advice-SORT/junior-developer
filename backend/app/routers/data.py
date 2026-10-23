import json
from pathlib import Path

from fastapi import APIRouter

from app.models import Data

router = APIRouter(tags=["data"])

DATA_FILE = Path(__file__).resolve().parents[2] / "data" / "mock.json"


@router.get("/data")
def get_data() -> list[Data]:
    items = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    return [Data.model_validate(item) for item in items]
