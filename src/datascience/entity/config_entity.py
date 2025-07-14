from pydantic import BaseModel
from pathlib import Path

class DataIngestionConfig(BaseModel):
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path