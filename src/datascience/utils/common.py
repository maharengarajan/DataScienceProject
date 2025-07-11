import os
import yaml
import json
import joblib
import numpy as np
from typing import Any
from pathlib import Path
from box import ConfigBox
from box.exceptions import BoxValueError
from src.datascience import LoggerConfig


logger = LoggerConfig.get_logger()


def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

def create_directories(path_to_directories: list, verbose=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


def save_json(path: Path, data: dict):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")


def load_json(path: Path) -> ConfigBox:
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


def save_bin(data: Any, path: Path):
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


def load_bin(path: Path) -> Any:
    data = joblib.load(path)
    logger.info(f"binary file loaded successfully from: {path}")
    return data

    
if __name__ == "__main__":
    print(read_yaml(Path("params.yaml")))
    create_directories(["amma/raja"])
    save_json(Path("amma/raja/test.json"), {"name": "John", "age": 20})
    print(load_json(Path("amma/raja/test.json")))
    save_bin(data=np.array([1,2,3]), path=Path("amma/raja/test.joblib"))
    print(load_bin(Path("amma/raja/test.joblib")))