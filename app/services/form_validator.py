def get_empty_required_fields(form_values: dict[str, str]) -> list[str]:
    """
    Return the list of required fields that are empty.

    Args:
        form_values: A dictionary mapping template variable names to user-provided values.

    Returns:
        A list of variable names with empty values.
    """
    empty_fields: list[str] = []

    for field_name, field_value in form_values.items():
        if not field_value.strip():
            empty_fields.append(field_name)

    return empty_fields