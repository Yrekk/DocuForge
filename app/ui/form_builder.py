import streamlit as st


def format_variable_label(variable_name: str) -> str:
    """
    Convert a template variable name into a readable form label.

    Args:
        variable_name: The raw variable name detected in the template.

    Returns:
        A human-readable label for the Streamlit form field.
    """
    return variable_name.replace("_", " ").capitalize()


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

        form_values[variable] = st.text_input(
            label=label,
            key=f"field_{variable}",
        )

    return form_values