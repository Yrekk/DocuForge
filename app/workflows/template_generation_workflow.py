import streamlit as st

from app.services.filename_sanitizer import sanitize_filename
from app.services.form_validator import get_empty_required_fields
from app.services.template_renderer import render_template
from app.services.variable_extractor import extract_template_variables
from app.ui.clipboard_button import display_copy_button
from app.ui.form_builder import build_dynamic_form


def run_template_generation_workflow(
    template_content: str,
    key_prefix: str,
    generate_button_label: str,
    generate_button_key: str,
    result_title: str,
    result_area_label: str,
    copy_button_label: str,
    result_height: int = 400,
    enable_download: bool = False,
    download_filename: str | None = None,
) -> None:
    """
    Run the common template generation workflow.

    Args:
        template_content: The Jinja2 template content.
        key_prefix: Prefix used for Streamlit form field keys.
        generate_button_label: Label displayed on the generation button.
        generate_button_key: Unique Streamlit key for the generation button.
        result_title: Title displayed above the generated result.
        result_area_label: Label of the result text area.
        copy_button_label: Label of the copy button.
        result_height: Height of the generated result text area.
        enable_download: Whether to display a download button.
        download_filename: Raw filename used for the downloaded document.
    """
    variables = extract_template_variables(template_content)


    if not variables:
        st.info("Aucune variable Jinja2 détectée dans ce template.")
        return

    print(f"Variables détectées : {', '.join(variables)}")

    form_values = build_dynamic_form(
        variables,
        key_prefix=key_prefix,
    )

    if st.button(generate_button_label, key=generate_button_key):
        empty_fields = get_empty_required_fields(form_values)

        if empty_fields:
            st.warning(
                "Certains champs obligatoires sont vides : "
                + ", ".join(empty_fields)
            )
            return

        rendered_document = render_template(template_content, form_values)

        st.subheader(result_title)

        st.text_area(
            result_area_label,
            value=rendered_document,
            height=result_height,
        )

        display_copy_button(
            rendered_document,
            button_label=copy_button_label,
        )

        if enable_download:
            safe_filename = sanitize_filename(
                download_filename or "document_genere"
            )

            st.download_button(
                label="Télécharger le document",
                data=rendered_document,
                file_name=f"{safe_filename}.txt",
                mime="text/plain",
            )