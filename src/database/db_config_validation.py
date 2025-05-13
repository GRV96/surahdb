from pathlib import Path

from jsonschema import validate

from src.file_io import load_json_file


_CONFIG_SCHEMA_PATH = Path(__file__).resolve().parent/"db_config_schema.json"


def validate_db_config(db_config):
	_db_config_schema = load_json_file(_CONFIG_SCHEMA_PATH)
	validate(db_config, _db_config_schema)


__all__ = [validate_db_config.__name__]
