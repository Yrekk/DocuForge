import pytest
from jinja2.exceptions import TemplateSyntaxError

from app.services.variable_extractor import extract_template_variables


def test_extract_template_variables_from_simple_template() -> None:
    template_content = """
    Bonjour {{ nom }},

    Je candidate au poste de {{ poste }} chez {{ entreprise }}.

    {{ motivation }}

    Cordialement,
    {{ signature }}
    """

    variables = extract_template_variables(template_content)

    assert variables == [
        "entreprise",
        "motivation",
        "nom",
        "poste",
        "signature",
    ]


def test_extract_template_variables_returns_empty_list_without_variables() -> None:
    template_content = "Bonjour, ceci est un template sans variable."

    variables = extract_template_variables(template_content)

    assert variables == []


def test_extract_template_variables_raises_value_error_for_empty_content() -> None:
    with pytest.raises(ValueError, match="Le contenu du template est vide."):
        extract_template_variables("")


def test_extract_template_variables_raises_template_syntax_error() -> None:
    broken_template = "Bonjour {{ nom"

    with pytest.raises(TemplateSyntaxError):
        extract_template_variables(broken_template)


def test_extract_template_variables_with_for_loop() -> None:
    template_content = """
    {% for competence in competences %}
    - {{ competence }}
    {% endfor %}
    """

    variables = extract_template_variables(template_content)

    assert variables == ["competences"]