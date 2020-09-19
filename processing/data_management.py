# Internal modules
from config import config

# External libraries
import pandas as pd
import requests
import json
import datetime



# Read excel file locally
def load_dataset(*, file_name: str) -> pd.DataFrame:
    _data = pd.read_excel(f"{config.DATASET_DIR}/{file_name}")
    print(datetime.datetime.now())
    return _data

# Read data from API
def fetch_data_from_api(url, token):
    response = requests.get(url, headers={'Authorization': f'Token {token}'})
    print(response)
    print(datetime.datetime.now())
    return pd.read_json(response.text)

def load_geojson(*, file_name: str):
    with open(f"{config.DATASET_DIR}/{file_name}") as f:
        geojson = json.load(f)

        return geojson




