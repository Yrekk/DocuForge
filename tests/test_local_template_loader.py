from pathlib import Path

import pytest

from app.services.local_template_loader import load_local_template


def test_load_local_template_returns_file_content(tmp_path: Path) -> None:
    template_path = tmp_path / "template.txt"
    template_path.write_text("Bonjour {{ nom }}", encoding="utf-8")

    content = load_local_template(template_path)

    assert content == "Bonjour {{ nom }}"


def test_load_local_template_raises_file_not_found_error(tmp_path: Path) -> None:
    missing_path = tmp_path / "missing_template.txt"

    with pytest.raises(FileNotFoundError, match="Template local introuvable"):
        load_local_template(missing_path)


def test_load_local_template_raises_value_error_for_empty_file(tmp_path: Path) -> None:
    template_path = tmp_path / "empty_template.txt"
    template_path.write_text("", encoding="utf-8")

    with pytest.raises(ValueError, match="Le template local est vide"):
        load_local_template(template_path)


def test_load_local_template_raises_value_error_for_whitespace_only_file(tmp_path: Path) -> None:
    template_path = tmp_path / "blank_template.txt"
    template_path.write_text("   \n\t", encoding="utf-8")

    with pytest.raises(ValueError, match="Le template local est vide"):
        load_local_template(template_path)