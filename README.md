# DataScienceProject

## install uv package
```
pip install uv
```

## create virtual environment
```
uv venv
```

## activate virtual environment
```
.venv\Scripts\activate
```

## inialize uv project
```
uv init
```

## install requirements
```
uv add -r requirements.txt
```

## run the project
```
python -m src.datascience.utils.common or uv run -m src.datascience.utils.common
```

## Workflows
```
1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update constants
5. Update the entity
6. Update the configuration manager in src config
7. Update the components
8. Update the pipeline 
9. Update the main.py
```