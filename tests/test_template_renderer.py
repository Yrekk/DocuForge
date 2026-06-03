import pytest

from app.services.template_renderer import render_template


def test_render_template_with_simple_context() -> None:
    template_content = "Bonjour {{ nom }}"
    context = {"nom": "Damien"}

    rendered_document = render_template(template_content, context)

    assert rendered_document == "Bonjour Damien"


def test_render_template_with_multiple_variables() -> None:
    template_content = (
        "Bonjour {{ nom }},\n\n"
        "Je candidate au poste de {{ poste }} chez {{ entreprise }}."
    )

    context = {
        "nom": "Damien",
        "poste": "Développeur IA",
        "entreprise": "Adeptus Data",
    }

    rendered_document = render_template(template_content, context)

    assert rendered_document == (
        "Bonjour Damien,\n\n"
        "Je candidate au poste de Développeur IA chez Adeptus Data."
    )


def test_render_template_with_condition_true() -> None:
    template_content = """
{% if mention_rqth %}
Mention RQTH activée.
{% endif %}
"""

    context = {"mention_rqth": True}

    rendered_document = render_template(template_content, context)

    assert "Mention RQTH activée." in rendered_document


def test_render_template_with_condition_false() -> None:
    template_content = """
{% if mention_rqth %}
Mention RQTH activée.
{% endif %}
"""

    context = {"mention_rqth": False}

    rendered_document = render_template(template_content, context)

    assert "Mention RQTH activée." not in rendered_document


def test_render_template_raises_value_error_for_empty_content() -> None:
    with pytest.raises(ValueError, match="Le contenu du template est vide."):
        render_template("", {})