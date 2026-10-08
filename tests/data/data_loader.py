import json
from pathlib import Path


def load_data(file_name):
    base_dir = Path(__file__).resolve().parent
    with open(base_dir / file_name, encoding="utf-8") as file:
        return json.load(file)
