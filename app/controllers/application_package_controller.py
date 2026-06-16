import streamlit as st
from jinja2.exceptions import TemplateError, TemplateSyntaxError

from app.services.config_loader import get_application_template_path
from app.services.local_template_loader import load_local_template
from app.workflows.template_generation_workflow import run_template_generation_workflow


def run_application_package_mode(key_prefix: str) -> None:
    """
    Run the offline application package workflow.

    This mode loads a local application template from configuration,
    generates a dynamic form, renders the final application-oriented prompt
    or document, and allows the user to copy the result.
    """
    st.subheader("Assistant candidature offline")

    st.write(
        "Ce mode génère un document de travail ou un prompt structuré pour préparer "
        "un CV ATS, une lettre de motivation ou une candidature ciblée, sans appel IA."
    )

    try:
        application_template_path = get_application_template_path()
        template_content = load_local_template(application_template_path)

        with st.expander("Voir le template utilisé"):
            st.text_area(
                "Template candidature",
                value=template_content,
                height=300,
                disabled=True,
            )

        run_template_generation_workflow(
            template_content=template_content,
            key_prefix=key_prefix,
            generate_button_label="Générer la candidature",
            generate_button_key="generate_application_package",
            result_title="Candidature générée",
            result_area_label="Résultat",
            copy_button_label="Copier la candidature",
            result_height=500,
            enable_download=False,
        )

    except FileNotFoundError as error:
        st.error(str(error))

    except UnicodeDecodeError:
        st.error(
            "Impossible de lire le template candidature. "
            "Vérifie qu'il est encodé en UTF-8."
        )

    except TemplateSyntaxError as error:
        st.error(f"Erreur de syntaxe Jinja2 : {error}")

    except TemplateError as error:
        st.error(f"Erreur lors du rendu du template : {error}")

    except KeyError as error:
        st.error(f"Configuration invalide : {error}")

    except ValueError as error:
        st.error(str(error))