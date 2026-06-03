import streamlit as st
from jinja2.exceptions import TemplateError, TemplateSyntaxError

from app.services.config_loader import get_prompt_template_path
from app.services.form_validator import get_empty_required_fields
from app.services.local_template_loader import load_local_template
from app.services.template_renderer import render_template
from app.services.variable_extractor import extract_template_variables
from app.ui.clipboard_button import display_copy_button
from app.ui.form_builder import build_dynamic_form


def run_prompt_generator_mode(key_prefix: str) -> None:
    """
    Run the local prompt generation workflow.

    This mode loads a prompt template from the application configuration,
    generates a dynamic form from its Jinja2 variables, renders the final
    prompt, and allows the user to copy the result.
    """
    st.subheader("Génération de prompt")

    st.write(
        "Ce mode utilise un template local configuré pour générer un prompt structuré. "
        "Le résultat est destiné à être copié puis utilisé dans une IA."
    )

    try:
        prompt_template_path = get_prompt_template_path()
        template_content = load_local_template(prompt_template_path)
        variables = extract_template_variables(template_content)

        with st.expander("Voir le template utilisé"):
            st.text_area(
                "Template de prompt",
                value=template_content,
                height=300,
                disabled=True,
            )

        st.write("Variables détectées :")

        if variables:
            st.code(", ".join(variables))

            form_values = build_dynamic_form(
                variables,
                key_prefix=key_prefix,
            )

            if st.button("Générer le prompt", key="generate_prompt"):
                empty_fields = get_empty_required_fields(form_values)

                if empty_fields:
                    st.warning(
                        "Certains champs obligatoires sont vides : "
                        + ", ".join(empty_fields)
                    )
                else:
                    rendered_prompt = render_template(
                        template_content,
                        form_values,
                    )

                    st.subheader("Prompt généré")

                    st.text_area(
                        "Résultat",
                        value=rendered_prompt,
                        height=500,
                    )

                    display_copy_button(
                        rendered_prompt,
                        button_label="Copier le prompt",
                    )
        else:
            st.info("Aucune variable Jinja2 détectée dans le template de prompt.")

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