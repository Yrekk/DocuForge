import unicodedata

import streamlit as st


LONG_TEXT_KEYWORDS = [
    "contexte",
    "context",
    "objectif",
    "mission",
    "tache",
    "task",
    "description",
    "contrainte",
    "contraintes",
    "constraint",
    "constraints",
    "instruction",
    "instructions",
    "detail",
    "details",
    "exemple",
    "exemples",
    "example",
    "examples",
    "contenu",
    "content",
    "motivation",
    "format_attendu",
    "public_cible",
    "information",
    "informations",
    "feedback",
    "prompt",
    "reponse",
    "response",
    "analyse",
    "raisonnement",
]


def normalize_variable_name(variable_name: str) -> str:
    """
    Normalize a variable name to make keyword detection more reliable.

    Example:
        tâche_a_accomplir -> tache_a_accomplir

    Args:
        variable_name: The raw variable name detected in the template.

    Returns:
        The normalized variable name, lowercased and without accents.
    """
    normalized = unicodedata.normalize("NFKD", variable_name)
    without_accents = "".join(
        char for char in normalized if not unicodedata.combining(char)
    )

    return without_accents.lower()


def format_variable_label(variable_name: str) -> str:
    """
    Convert a template variable name into a readable form label.

    Args:
        variable_name: The raw variable name detected in the template.

    Returns:
        A human-readable label for the Streamlit form field.
    """
    return variable_name.replace("_", " ").capitalize()


def should_use_text_area(variable_name: str) -> bool:
    """
    Determine whether a variable should be rendered as a multiline text area.

    Args:
        variable_name: The raw variable name detected in the template.

    Returns:
        True if the field should use a text area, False otherwise.
    """
    normalized_name = normalize_variable_name(variable_name)

    if len(normalized_name) > 30:
        return True

    return any(keyword in normalized_name for keyword in LONG_TEXT_KEYWORDS)


def build_dynamic_form(variables: list[str]) -> dict[str, str]:
    """
    Build a dynamic Streamlit form from template variables.

    Args:
        variables: The list of variable names detected in the template.

    Returns:
        A dictionary mapping variable names to user-provided values.
    """
    form_values: dict[str, str] = {}

    st.subheader("Champs à remplir")

    for variable in variables:
        label = format_variable_label(variable)

        if should_use_text_area(variable):
            form_values[variable] = st.text_area(
                label=label,
                key=f"field_{variable}",
                height=180,
            )
        else:
            form_values[variable] = st.text_input(
                label=label,
                key=f"field_{variable}",
            )

    return form_values