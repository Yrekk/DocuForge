from pathlib import Path
import json
from json import JSONDecodeError


DEFAULT_CONFIG_PATH = Path("app/config/templates_config.json")


def load_config(config_path: str | Path = DEFAULT_CONFIG_PATH) -> dict:
    """
    Load a JSON configuration file.

    Args:
        config_path: Path to the JSON configuration file.

    Returns:
        The parsed configuration as a dictionary.

    Raises:
        FileNotFoundError: If the config file does not exist.
        ValueError: If the config file is not valid JSON.
    """
    path = Path(config_path)

    if not path.exists():
        raise FileNotFoundError(f"Fichier de configuration introuvable : {path}")

    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)

    except JSONDecodeError as error:
        raise ValueError(f"Fichier de configuration JSON invalide : {path}") from error
    
def get_prompt_template_path() -> Path:
    config = load_config()
    prompt_template_path = config.get(
        "advanced_prompt_template_path",
        config.get("prompt_template_path"),
    )
    if "prompt_template_path" not in config:
        raise KeyError("La clé 'prompt_template_path' est absente du fichier de configuration.")

    return Path(prompt_template_path)