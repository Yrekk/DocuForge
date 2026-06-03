from app.services.form_validator import get_empty_required_fields


def test_get_empty_required_fields_returns_empty_list_when_all_fields_are_filled() -> None:
    form_values = {
        "nom": "Damien",
        "poste": "Développeur IA",
        "entreprise": "Adeptus Data",
    }

    empty_fields = get_empty_required_fields(form_values)

    assert empty_fields == []


def test_get_empty_required_fields_detects_empty_strings() -> None:
    form_values = {
        "nom": "Damien",
        "poste": "",
        "entreprise": "Adeptus Data",
    }

    empty_fields = get_empty_required_fields(form_values)

    assert empty_fields == ["poste"]


def test_get_empty_required_fields_detects_whitespace_only_values() -> None:
    form_values = {
        "nom": "   ",
        "poste": "Développeur IA",
        "entreprise": "\t",
    }

    empty_fields = get_empty_required_fields(form_values)

    assert empty_fields == ["nom", "entreprise"]


def test_get_empty_required_fields_detects_multiple_empty_fields() -> None:
    form_values = {
        "nom": "",
        "poste": "",
        "entreprise": "Adeptus Data",
        "signature": "",
    }

    empty_fields = get_empty_required_fields(form_values)

    assert empty_fields == ["nom", "poste", "signature"]