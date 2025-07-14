from pydantic import BaseModel
from pathlib import Path

class DataIngestionConfig(BaseModel):
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


class DataValidationConfig(BaseModel):
    root_dir:Path
    STATUS_FILE:str
    unzip_data_dir:Path
    all_schema:dict

class DataTransformationConfig(BaseModel):
    root_dir: Path
    data_path: Path

class ModelTrainerConfig(BaseModel):
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    alpha: float
    l1_ratio: float
    target_column: str

class ModelEvaluationConfig(BaseModel):
    root_dir: Path
    test_data_path: Path
    model_path: Path
    all_params: dict
    metric_file_name: Path
    target_column: str
    mlflow_uri: str