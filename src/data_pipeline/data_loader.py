import pandas as pd
from pathlib import Path

class DataLoader:
    
    def __init__(self, base_path="data"):
        self.base_path = Path(base_path)

    def load_csv(self, file_name: str) -> pd.DataFrame:
        path = self.base_path / file_name
        return pd.read_csv(path)

    def load_excel(self, file_name: str) -> pd.DataFrame:
        path = self.base_path / file_name
        return pd.read_excel(path)

    def load_json(self, file_name: str) -> pd.DataFrame:
        path = self.base_path / file_name
        return pd.read_json(path)

    def save_csv(self, df: pd.DataFrame, file_name: str):

        output_path = self.base_path / file_name
        df.to_csv(output_path, index=False)

    def list_files(self):

        return [f.name for f in self.base_path.iterdir()]
