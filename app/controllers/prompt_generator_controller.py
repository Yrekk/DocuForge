import streamlit as st
from jinja2.exceptions import TemplateError, TemplateSyntaxError

from app.services.config_loader import get_prompt_template_path
from app.services.local_template_loader import load_local_template
from app.workflows.template_generation_workflow import run_template_generation_workflow


def run_prompt_generator_mode(key_prefix: str) -> None:
    """
    Run the local prompt generation workflow.

    This mode loads a prompt template from configuration, generates a dynamic
    form from its variables, renders the final prompt, and allows copy only.
    """
    st.subheader("Génération de prompt")

    st.write(
        "Ce mode utilise un template local configuré pour générer un prompt structuré. "
        "Le résultat est destiné à être copié puis utilisé dans une IA."
    )

    try:
        prompt_template_path = get_prompt_template_path()
        template_content = load_local_template(prompt_template_path)

        with st.expander("Voir le template utilisé"):
            st.text_area(
                "Template de prompt",
                value=template_content,
                height=300,
                disabled=True,
            )

        run_template_generation_workflow(
            template_content=template_content,
            key_prefix=key_prefix,
            generate_button_label="Générer le prompt",
            generate_button_key="generate_prompt",
            result_title="Prompt généré",
            result_area_label="Résultat",
            copy_button_label="Copier le prompt",
            result_height=500,
            enable_download=False,
        )

    except FileNotFoundError as error:
        st.error(str(error))

    except UnicodeDecodeError:
        st.error(
            "Impossible de lire le template de prompt. "
            "Vérifie qu'il est encodé en UTF-8."
        )

    except TemplateSyntaxError as error:
        st.error(f"Erreur de syntaxe Jinja2 : {error}")

    except TemplateError as error:
        st.error(f"Erreur lors du rendu du template : {error}")

    except KeyError as error:
        st.error(f"Configuration invalide : clé manquante {error}")

    except ValueError as error:
        st.error(str(error))