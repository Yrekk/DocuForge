from typing import BinaryIO


def read_template_file(uploaded_file: BinaryIO) -> str:
    """
    Read an uploaded template file and return its text content.

    Args:
        uploaded_file: A file-like object uploaded through Streamlit.

    Returns:
        The decoded text content of the uploaded file.

    Raises:
        ValueError: If the uploaded file is empty.
        UnicodeDecodeError: If the file cannot be decoded as UTF-8.
    """
    raw_content = uploaded_file.read()

    if not raw_content:
        raise ValueError("Le fichier uploadé est vide.")

    return raw_content.decode("utf-8")