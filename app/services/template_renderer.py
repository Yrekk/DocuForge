from jinja2 import Environment
from jinja2.exceptions import TemplateError


def render_template(template_content: str, context: dict[str, str]) -> str:
    """
    Render a Jinja2 template using the provided context.

    Args:
        template_content: The raw Jinja2 template content.
        context: A dictionary containing values for template variables.

    Returns:
        The rendered document as a string.

    Raises:
        ValueError: If the template content is empty.
        TemplateError: If an error occurs during Jinja2 rendering.
    """
    if not template_content.strip():
        raise ValueError("Le contenu du template est vide.")

    environment = Environment(
        autoescape=False,
        trim_blocks=True,
        lstrip_blocks=True,
    )

    template = environment.from_string(template_content)

    return template.render(context)