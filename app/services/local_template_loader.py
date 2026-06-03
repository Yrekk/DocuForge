from pathlib import Path


def load_local_template(template_path: str | Path) -> str:
    """
    Load a local template file and return its text content.

    Args:
        template_path: Path to the local template file.

    Returns:
        The template content as a string.

    Raises:
        FileNotFoundError: If the template file does not exist.
        ValueError: If the template file is empty.
    """
    path = Path(template_path)

    if not path.exists():
        raise FileNotFoundError(f"Template local introuvable : {path}")

    content = path.read_text(encoding="utf-8")

    if not content.strip():
        raise ValueError(f"Le template local est vide : {path}")

    return content