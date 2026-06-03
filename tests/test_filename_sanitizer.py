from app.services.filename_sanitizer import sanitize_filename


def test_sanitize_filename_keeps_simple_name() -> None:
    assert sanitize_filename("prompt_candidature") == "prompt_candidature"


def test_sanitize_filename_replaces_spaces() -> None:
    assert sanitize_filename("prompt candidature ia") == "prompt_candidature_ia"


def test_sanitize_filename_replaces_invalid_windows_characters() -> None:
    assert sanitize_filename("prompt / candidature : ia") == "prompt___candidature___ia"


def test_sanitize_filename_returns_default_for_empty_name() -> None:
    assert sanitize_filename("") == "document_genere"


def test_sanitize_filename_returns_default_for_whitespace_only_name() -> None:
    assert sanitize_filename("   ") == "document_genere"