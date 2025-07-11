# __all__ declared at the module's end

from pathlib import Path

from jsonschema import validate

from src.file_io import load_json_file


_CONFIG_SCHEMA_PATH = Path(__file__).resolve().parent/"db_config_schema.json"


def validate_db_config(db_config: dict) -> None:
	"""
	Given a configuration for the connection to a MySQL server, this function
	validates it according to the schema. If no exception is raised, the
	configuration is valid.

	Args:
		db_config: the connection's configuration

	Raises:
		jsonschema.exceptions.ValidationError: if the connection configuration
			does not match the schema.
	"""
	db_config_schema = load_json_file(_CONFIG_SCHEMA_PATH)
	validate(db_config, db_config_schema)


__all__ = [validate_db_config.__name__]
