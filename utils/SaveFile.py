import pandas as pd
from pathlib import Path


def save_csv(file: pd.DataFrame, name: str):
    temp_path = f"results/{name}.csv"
    file.to_csv(Path(temp_path), index=False)
