from jinja2 import Environment, meta
from jinja2.exceptions import TemplateSyntaxError


def extract_template_variables(template_content: str) -> list[str]:
    """
    Extract undeclared variables from a Jinja2 template.

    Args:
        template_content: The raw Jinja2 template content.

    Returns:
        A sorted list of variable names found in the template.

    Raises:
        ValueError: If the template content is empty.
        TemplateSyntaxError: If the Jinja2 template syntax is invalid.
    """
    if not template_content.strip():
        raise ValueError("Le contenu du template est vide.")

    environment = Environment()
    parsed_content = environment.parse(template_content)

    variables = meta.find_undeclared_variables(parsed_content)

    return sorted(variables)