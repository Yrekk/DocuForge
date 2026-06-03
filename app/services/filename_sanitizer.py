import re


def sanitize_filename(filename: str, default_name: str = "document_genere") -> str:
    """
    Sanitize a filename for safe local download.

    Args:
        filename: The raw filename provided by the user.
        default_name: The default filename to use if the provided name is empty.

    Returns:
        A safe filename without extension.
    """
    cleaned_filename = filename.strip()

    if not cleaned_filename:
        return default_name

    cleaned_filename = re.sub(r'[<>:"/\\|?*]', "_", cleaned_filename)
    cleaned_filename = re.sub(r"\s+", "_", cleaned_filename)

    return cleaned_filename